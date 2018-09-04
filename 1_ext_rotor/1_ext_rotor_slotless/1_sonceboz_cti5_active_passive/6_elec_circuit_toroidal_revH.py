#! Flux3D 12.0
# some change of definitions because airgap is now directly fixed

# ParameterGeom['COIL_PHI','COIL_PHI_PER','COIL_PSI','COIL_ST_PER'].delete()
## rev G has changes from 18.01.2018

##rev H now considers "radial" coils inside the airgap, which is then filled with it
##what happens in the inner radius, and how their area is fitted is still misterious, but it is more equivalent to
##the case of the slotless motor, see 2.2.2018

##these parameters were taken from rev G, and are there for aesthetic purposes only
lastInstance = ParameterGeom(name='D_COIL_R_THEO : theoretical coil radial thickness, see mathematica',
              expression='-.5')	
			  
lastInstance = ParameterGeom(name='R_COIL_R_THEO : theoretical coil radial thickness, see mathematica',
              expression='67/280')				  

lastInstance = ParameterGeom(name='COIL_R_THEO : theoretical coil radial thickness, see mathematica',
              expression='D_COIL_R_THEO*D_AGAP+R_COIL_R_THEO*R_ROT_OUT')	
			  
lastInstance = ParameterGeom(name='COIL_R_CASE : if 0, max coil thickness is limited',
              expression='Valid(COIL_R_THEO,0,D_AGAP-1)')				  

lastInstance = ParameterGeom(name='COIL_R : real coil radial thickness, see mathematica',
              expression='COIL_R_CASE*COIL_R_THEO+(1-COIL_R_CASE)*(D_AGAP-1)')				  
			  
lastInstance = ParameterGeom(name='COIL_WCOIL : toroidal coil width',
              expression='2*pi()/6*(R_ST_IN-COIL_R)')	
			  		  
##now start writing the parameters of the real coils
lastInstance = VariationParameterFormula(name='TH_COIL_CIRC : theoretical thickness, see 2.2.2018',
                          formula='D_AGAP-1')

lastInstance = VariationParameterFormula(name='D_ROT_PH : rotor thickness',
                          formula='K_D_ROT*R_ROT_OUT')							

lastInstance = VariationParameterFormula(name='R_ROT_IN_PH',
                          formula='R_ROT_OUT-D_ROT_PH')											
						
lastInstance = VariationParameterFormula(name='D_MAG_PH',
                          formula='K_D_MAG*R_ROT_OUT')
						  
lastInstance = VariationParameterFormula(name='D_AGAP_PH',
                          formula='D_AGAP')						  
						
lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ROT_IN_PH-D_MAG_PH-D_AGAP_PH')			

lastInstance = VariationParameterFormula(name='A_COIL : considering radial coils see 2.2.2018',
                          formula='pi()/6*((R_ST_OUT_PH+TH_COIL_CIRC)^2-R_ST_OUT_PH^2)')
						  
lastInstance = VariationParameterFormula(name='A_CU',
                          formula='A_COIL*COIL_KCU')						  

##now the length 
lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = VariationParameterFormula(name='H_ST_PH',
                          formula='2*R_ROT_OUT*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')						  
lastInstance = VariationParameterFormula(name='D_ST_PH',
                          formula='K_D_ST*R_ROT_OUT')
						  
lastInstance = VariationParameterFormula(name='L_BAR_PH',
                          formula='2*(H_ST_PH+D_ST_PH)+2*pi()*TH_COIL_CIRC/2')		

##everything ready for the resistance						  
lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')

lastInstance = VariationParameterFormula(name='R_COIL',
                          formula='rho_cu*L_BAR_PH*1e-3/(A_CU*1e-6)')
						  
##now parameters for currents
##torque	
lastInstance = VariationParameterPilot(name='I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
						
lastInstance = VariationParameterPilot(name='THETA_T : torque generation angle degrees',
                        referenceValue=180)

lastInstance = VariationParameterPilot(name='JT_RMS : torque current density',
                        referenceValue=0.0)			

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(I_T_PEAK+JT_RMS*A_CU*sqrt(2))')							

##force
lastInstance = VariationParameterPilot(name='I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=30)

lastInstance = VariationParameterPilot(name='THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
						
lastInstance = VariationParameterFormula(name='THETA_F : force direction angle degrees',
                        formula='THETA_F0-THETA_F_DIR')
						
lastInstance = VariationParameterPilot(name='JF_RMS : force current density',
                        referenceValue=0.0)						  						
						
lastInstance = VariationParameterFormula(name='IF_HAT',
                          formula='(I_F_PEAK+JF_RMS*A_CU*sqrt(2))')								
							

						
##now, copper losses
lastInstance = VariationParameterFormula(name='P_CU_TOT',
                          formula='6/2*R_COIL*(IF_HAT+IT_HAT)^2')	

##define coordinate system, current types, their sum and coils						  
for i in range(1,7):
	## coordinate system for coils
	lastInstance = CoordSysCartesian(name='COORD_COIL_'+str(i),
					parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
												angleUnit=AngleUnit['DEGREE']),
					origin=['1/2*(R_ST_OUT+r_st_in)*cosd(60*'+str(i-1)+')',
							'1/2*(R_ST_OUT+r_st_in)*sind(60*'+str(i-1)+')',
							'0'],
					rotationAngles=RotationAngles(angleX='90',
													angleY='60*'+str(i-1)+'',
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
                        '0'],
                dimensions=['R_ST_OUT-R_ST_IN+COIL_R',
                            'h_ST+COIL_R'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='COIL_WCOIL',
                                                       width='COIL_R'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])	
				
## now volume outputs	

lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ROT_OUT*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')		

lastInstance = VariationParameterFormula(name='V_FE_ROT : volume of the iron of rotor',
                          formula='pi()*((R_ROT_OUT)^2-(R_ROT_OUT-D_ROT_PH)^2)*H_ROT_PH')	

lastInstance = VariationParameterFormula(name='V_FE_ST : volume of the iron of rotor',
                          formula='pi()*((R_ST_OUT_PH)^2-(R_ST_OUT_PH-D_ST_PH)^2)*H_ST_PH')

lastInstance = VariationParameterFormula(name='V_PM : volume of the magnet in rotor',
                          formula='pi()*((R_ROT_IN_PH)^2-(R_ROT_IN_PH-D_MAG_PH)^2)*H_ROT_PH*4*THETA_MAG/360')

lastInstance = VariationParameterFormula(name='V_COIL : volume of the coils ',
                          formula='6*L_BAR_PH*A_CU/COIL_KCU')							  