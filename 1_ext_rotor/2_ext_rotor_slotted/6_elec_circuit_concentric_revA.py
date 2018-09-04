#! Flux3D 12.0
					
##parameters of winding
lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')	

lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')						
					
##geometric parameters of coil as IO parameters, slots are now filled !!!
lastInstance = VariationParameterFormula(name='R_SC : radius stator center, pg 36 reichert',
                          formula='(K_W_SLOT*R_ROT_OUT)/2*1/Sin(pi()/6)')

lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ROT_OUT*(1-K_D_ROT-K_D_MAG)-D_AGAP')

lastInstance = VariationParameterFormula(name='A_TOOTH : see reichert pg36',
                          formula='R_ROT_OUT*K_W_SLOT*(R_ST_OUT_PH-R_SC)')

lastInstance = VariationParameterFormula(name='A_SLOT : =2*A_COIL, pg 36 reichert',
                          formula='pi()*R_ST_OUT_PH^2/6-A_TOOTH-pi()*R_SC^2/6')

lastInstance = VariationParameterFormula(name='A_COIL : half of a slot area',
                          formula='A_SLOT/2')
						  
lastInstance = VariationParameterFormula(name='R_M : mean radius of stator',
                          formula='(R_ST_OUT_PH+R_SC)/2')						  
						  
lastInstance = VariationParameterFormula(name='TH_COIL : medium thickness, see 2.2.2018',
                          formula='(R_M*Sind(30)-R_ROT_OUT*K_W_SLOT/2)/2')	

lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH : needed for stator height',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')							  
						  
lastInstance = VariationParameterFormula(name='H_ST_PH : needed for coil length',
                          formula='2*R_ROT_OUT*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')
						  
lastInstance = VariationParameterFormula(name='L_BAR_PH',
                          formula='2*(H_ST_PH+R_ROT_OUT*K_W_SLOT)+2*pi()*TH_COIL/2') 
						  
lastInstance = VariationParameterFormula(name='A_CU : half of a slot area',
                          formula='A_COIL*COIL_KCU')						  
						  
lastInstance = VariationParameterFormula(name='R_COIL',
                          formula='rho_cu*L_BAR_PH*1e-3/(A_CU*1e-6)')					  
					
## parameters for torque
lastInstance = VariationParameterPilot(name='I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
						
lastInstance = VariationParameterPilot(name='THETA_T : torque generation angle degrees',
                        referenceValue=30)

lastInstance = VariationParameterPilot(name='JT_RMS : torque current density',
                        referenceValue=0.0)	

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(I_T_PEAK+JT_RMS*A_CU*sqrt(2))')				  						  

## parameters for force

lastInstance = VariationParameterPilot(name='I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=270)

lastInstance = VariationParameterPilot(name='THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
						
lastInstance = VariationParameterFormula(name='THETA_F : force direction angle degrees',
                        formula='THETA_F0-THETA_F_DIR')
						  
lastInstance = VariationParameterPilot(name='JF_RMS : force current density',
                        referenceValue=0.0)		

lastInstance = VariationParameterFormula(name='IF_HAT',
                          formula='(I_F_PEAK+JF_RMS*A_CU*sqrt(2))')		

ParameterGeom(name='K_COIL : thickness of coil, only for virtual purposes',
              expression='1/14')
			  
## output parameters
			  
lastInstance = VariationParameterFormula(name='P_CU_TOT',
                          formula='6*R_COIL*(IF_HAT+IT_HAT)^2/2')				  
						  
						  
			 			  
						    
for i in range(1,7):
	## coordinate system for coils
	lastInstance = CoordSysCartesian(name='COORD_COIL_'+str(i),
					parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
												angleUnit=AngleUnit['DEGREE']),
					origin=['R_ST_OUT*cosd(30+60*'+str(i-1)+')',
							'R_ST_OUT*sind(30+60*'+str(i-1)+')',
							'0'],
					rotationAngles=RotationAngles(angleX='90',
													angleY='120+60*'+str(i-1)+'',
													angleZ='0'),
					visibility=Visibility['VISIBLE'])
	# equations for torque current
	lastInstance = VariationParameterFormula(name='I_T_'+str(i),
							  formula='IT_HAT*Cosd(2*DTHETA-THETA_T+'+str((i-1)*120)+')')					
	# equations for force current							  
	lastInstance = VariationParameterFormula(name='I_F_'+str(i),
							  formula='IF_HAT*Cosd(2*DTHETA-THETA_F+'+str((i-1)*60)+')')
	# define current							
	lastInstance = CurrentStrandedCoil(name='I_'+str(i)+' : current in first drive coil',
						rmsModulus='I_T_'+str(i)+'+I_F_'+str(i))							  
	#do coils
	lastInstance = CoilRectangular(name='Coil_'+str(i),
                strandedCoil=CoilConductor['I_'+str(i)],
                turnNumber='1',
                seriesOrParallel=AllInSeries(),
                coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
                coordSys=CoordSys['COORD_COIL_'+str(i)],
                center=['0',
                        '0',
                        '-1/2*K_COIL*R_ROT_OUT'],
                dimensions=['W_SLOT+K_COIL*R_ROT_OUT/2',
                            'H_ST+K_COIL*R_ROT_OUT'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='K_COIL*R_ROT_OUT',
                                                       width='K_COIL*R_ROT_OUT'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])				

##material parameters	
lastInstance = VariationParameterFormula(name='D_ROT_PH : rotor thickness',
                          formula='K_D_ROT*R_ROT_OUT')	
						  
lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ROT_OUT*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')						  
lastInstance = VariationParameterFormula(name='V_FE_ROT : volume of the iron of rotor',
                          formula='pi()*((R_ROT_OUT)^2+(R_ROT_OUT-D_ROT_PH)^2)*H_ROT_PH')	
						  
lastInstance = VariationParameterFormula(name='R_ROT_IN_PH',
                          formula='R_ROT_OUT-D_ROT_PH')		

lastInstance = VariationParameterFormula(name='D_MAG_PH',
                          formula='K_D_MAG*R_ROT_OUT')						  

lastInstance = VariationParameterFormula(name='V_PM : volume of the magnet in rotor',
                          formula='pi()*((R_ROT_IN_PH)^2-(R_ROT_IN_PH-D_MAG_PH)^2)*H_ROT_PH*4*THETA_MAG/360')
						  
lastInstance = VariationParameterFormula(name='V_COIL : volume of the coils ',
                          formula='6*L_BAR_PH*A_CU/COIL_KCU')							  
						  
lastInstance = VariationParameterFormula(name='D_AGAP_PH',
                          formula='D_AGAP')						  	

lastInstance = VariationParameterFormula(name='V_FE_ST : stator iron volume',
                          formula='(pi()*R_ROT_OUT^2-A_SLOT*6)*H_ST_PH')
						  