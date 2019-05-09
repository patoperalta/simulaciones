#! Flux3D 18.1
					
##parameters of winding
lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')	

lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')						
					
##geometric parameters of coil as IO parameters, slots are now filled !!!
lastInstance = VariationParameterFormula(name='DRV_R_SC : radius stator center, pg 36 reichert',
                          formula='(K_W_SLOT*R_OUT_PM_ROT_BNG)/2*1/Sin(pi()/6)')

lastInstance = VariationParameterFormula(name='DRV_R_DR_ROT_OUT_PH : drv rot outer radius, auxiliary actually',
                          formula='R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP')
						  
lastInstance = VariationParameterFormula(name='DRV_R_ST_OUT_PH : outer radius of teeth',
                          formula='DRV_R_DR_ROT_OUT_PH-R_OUT_PM_ROT_BNG*(K_D_DR_FE_ROT+K_D_DR_PM)-D_AGAP_D')
						  
lastInstance = VariationParameterFormula(name='DRV_A_TOOTH : see reichert pg36',
                          formula='R_OUT_PM_ROT_BNG*K_W_SLOT*(DRV_R_ST_OUT_PH-DRV_R_SC)')		

lastInstance = VariationParameterFormula(name='DRV_A_SLOT : =2*A_COIL, pg 36 reichert',
                          formula='pi()*DRV_R_ST_OUT_PH^2/6-DRV_A_TOOTH-pi()*DRV_R_SC^2/6')		
						  
lastInstance = VariationParameterFormula(name='DRV_A_COIL : half of a slot area',
                          formula='DRV_A_SLOT/2')						  

lastInstance = VariationParameterFormula(name='DRV_R_M : mean radius of stator',
                          formula='(DRV_R_DR_ROT_OUT_PH+DRV_R_SC)/2')	

lastInstance = VariationParameterFormula(name='DRV_TH_COIL : medium thickness, see 2.2.2018',
                          formula='(DRV_R_M*Sind(30)-R_OUT_PM_ROT_BNG*K_W_SLOT/2)/2')			

lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH : needed for stator height',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = VariationParameterFormula(name='R_OUT_PM_ROT_BNG_AUX : as auxiliary, once again',
                          formula='R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG')						  

lastInstance = VariationParameterFormula(name='DRV_H_L_PH : needed for coil length',
                          formula='2*R_OUT_PM_ROT_BNG_AUX*beta_d')	

lastInstance = VariationParameterFormula(name='DRV_L_BAR_PH',
                          formula='2*(DRV_H_L_PH+R_OUT_PM_ROT_BNG*K_W_SLOT)+2*pi()*DRV_TH_COIL/2') 
						  
lastInstance = VariationParameterFormula(name='DRV_A_CU : half of a slot area',
                          formula='DRV_A_COIL*COIL_KCU')						  
						  
lastInstance = VariationParameterFormula(name='DRV_R_COIL',
                          formula='rho_cu*DRV_L_BAR_PH*1e-3/(DRV_A_CU*1e-6)')							  
						  
## parameters for torque
lastInstance = VariationParameterPilot(name='DRV_I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
						
lastInstance = VariationParameterPilot(name='DRV_THETA_T : torque generation angle degrees',
                        referenceValue=30)

lastInstance = VariationParameterPilot(name='DRV_JT_RMS : torque current density',
                        referenceValue=0.0)	

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(DRV_I_T_PEAK+DRV_JT_RMS*DRV_A_CU*sqrt(2))')	
						  
ParameterGeom(name='K_COIL : thickness of coil, only for virtual purposes',
              expression='1/20')						  

## output parameters
lastInstance = VariationParameterFormula(name='DRV_P_CU_TOT',
                          formula='6*DRV_R_COIL*(IT_HAT)^2/2')

for i in range(1,7):
	## coordinate system for coils
	lastInstance = CoordSysCartesian(name='COORD_COIL_DRV_'+str(i),
					parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
												angleUnit=AngleUnit['DEGREE']),
					origin=['R_DR_ST_OUT*cosd(30+60*'+str(i-1)+')',
							'R_DR_ST_OUT*sind(30+60*'+str(i-1)+')',
							'0'],
					rotationAngles=RotationAngles(angleX='90',
													angleY='120+60*'+str(i-1)+'',
													angleZ='0'),
					visibility=Visibility['VISIBLE'])
	# equations for torque current
	lastInstance = VariationParameterFormula(name='I_T_'+str(i),
							  formula='IT_HAT*Cosd(2*DTHETA-DRV_THETA_T+'+str((i-1)*120)+')')					

	# define current							
	lastInstance = CurrentStrandedCoil(name='I_DRV_'+str(i)+' : current in first drive coil',
						rmsModulus='I_T_'+str(i))							  
	#do coils
	lastInstance = CoilRectangular(name='Coil_DRV_'+str(i),
                strandedCoil=CoilConductor['I_DRV_'+str(i)],
                turnNumber='1',
                seriesOrParallel=AllInSeries(),
                coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
                coordSys=CoordSys['COORD_COIL_DRV_'+str(i)],
                center=['0',
                        '0',
                        '-1/2*K_COIL*R_DR_ST_OUT'],
                dimensions=['W_SLOT+K_COIL*R_OUT_ST_BNG/2',
                            'H_DRV+K_COIL*R_OUT_ST_BNG'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='K_COIL*R_OUT_ST_BNG',
                                                       width='K_COIL*R_OUT_ST_BNG'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])						  