#! Flux3D 12.0
# some change of definitions

##rev B has new copper area, see 2.2.2017

##revE is for homopolar bearing inner rotor slotless

##for aesthetic purposes
lastInstance = ParameterGeom(name='BNG_M_R_THEO : m * x + n',
              expression='.15')	
			  
lastInstance = ParameterGeom(name='BNG_N_R_THEO : m * x + n',
              expression='0')			  

lastInstance = ParameterGeom(name='BNG_COIL_R_THEO : theoretical coil radial thickness, see excel',
              expression='BNG_M_R_THEO*R_B_ST_OUT+BNG_N_R_THEO')	
			  
lastInstance = ParameterGeom(name='BNG_COIL_R_CASE : if 0, max coil thickness is limited by airgap',
              expression='Valid(BNG_COIL_R_THEO,0,D_AGAP_B-1)')				  

lastInstance = ParameterGeom(name='BNG_COIL_R : real coil radial thickness, see excel v2',
              expression='BNG_COIL_R_CASE*BNG_COIL_R_THEO+(1-BNG_COIL_R_CASE)*(D_AGAP_B-1)')	
			  
lastInstance = ParameterGeom(name='BNG_COIL_WCOIL : toroidal coil width, motor is very small, so width also',
              expression='2*pi()/6*(R_B_ST_OUT-D_ST_B-BNG_COIL_R)*0+3')				  

## now start with the theoretical parameters of the radially oriented coils
lastInstance = VariationParameterFormula(name='BNG_TH_COIL_CIRC : theoretical thickness, see 2.2.2018',
                          formula='D_AGAP_B-1')	

lastInstance = VariationParameterFormula(name='BNG_R_ST_IN_PH',
                          formula='R_B_PM_ROT_OUT+D_AGAP_B')	

lastInstance = VariationParameterFormula(name='BNG_A_COIL : area of each coil',
                          formula='pi()/6*(BNG_R_ST_IN_PH^2-(BNG_R_ST_IN_PH-BNG_TH_COIL_CIRC)^2)')	

lastInstance = VariationParameterFormula(name='BNG_A_CU',
                          formula='BNG_A_COIL*COIL_KCU')	

lastInstance = VariationParameterFormula(name='BNG_ALPHA_CASE_PH : needed for stator height',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')	

# lastInstance = VariationParameterFormula(name='BNG_R_B_ST_OUT : as auxiliary, once again',
                          # formula='R_B_PM_ROT_OUT+D_AGAP_B+D_ST_B')							  

##now the length and therefore resistance
lastInstance = VariationParameterFormula(name='BNG_H_L_PH : height of the bearing coil',
                          formula='2*BNG_R_B_ST_OUT*(BNG_ALPHA_CASE_PH*BETA_B+(1-BNG_ALPHA_CASE_PH)*BETA_B/ALPHA_H)')	

lastInstance = VariationParameterFormula(name='BNG_L_BAR_PH',
                          formula='2*(BNG_H_L_PH+D_ST_B)+2*pi()*BNG_TH_COIL_CIRC/2')	

##everything ready for the resistance						  
lastInstance = VariationParameterFormula(name='BNG_R_COIL',
                          formula='rho_cu*BNG_H_L_PH*1e-3/(BNG_A_CU*1e-6)')			

##force
lastInstance = VariationParameterPilot(name='BNG_I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='BNG_THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=0)

lastInstance = VariationParameterPilot(name='BNG_THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
						
lastInstance = VariationParameterFormula(name='BNG_THETA_F : force direction angle degrees',
                        formula='BNG_THETA_F0-BNG_THETA_F_DIR')						
	
lastInstance = VariationParameterPilot(name='BNG_JF_RMS : force current density',
                        referenceValue=0.0)						  						
						
lastInstance = VariationParameterFormula(name='BNG_IF_HAT',
                          formula='(BNG_I_F_PEAK+BNG_JF_RMS*BNG_A_CU*sqrt(2))')		

##coordinate systems, currents and coils
for i in range(1,7):
	## coordinate system for coils
	lastInstance = CoordSysCartesian(name='COORD_COIL_BNG_'+str(i),
					parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
												angleUnit=AngleUnit['DEGREE']),
					origin=['(R_B_ST_OUT-1/2*D_ST_B)*cosd(60*'+str(i-1)+')',
							'(R_B_ST_OUT-1/2*D_ST_B)*sind(60*'+str(i-1)+')',
							'0'],
					rotationAngles=RotationAngles(angleX='90',
													angleY='60*'+str(i-1)+'',
													angleZ='0'),
					visibility=Visibility['VISIBLE'])				
	##### equations for force current							  
	lastInstance = VariationParameterFormula(name='I_F_'+str(i),
							  formula='BNG_IF_HAT*Cosd(2*DTHETA-BNG_THETA_F+'+str((i-1)*60)+')')
	##### 	define current							
	lastInstance = CurrentStrandedCoil(name='I_BNG_'+str(i)+' : current in first drive coil',
						rmsModulus='I_F_'+str(i))							  
	##### 	do coils
	lastInstance = CoilRectangular(name='Coil_BNG_'+str(i),
                strandedCoil=CoilConductor['I_BNG_'+str(i)],
                turnNumber='1',
                seriesOrParallel=AllInSeries(),
                coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
                coordSys=CoordSys['COORD_COIL_BNG_'+str(i)],
                center=['0',
                        '0',
                        '0'],
                dimensions=['D_ST_B+BNG_COIL_R',
                            'H_B_ST+BNG_COIL_R'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='BNG_COIL_WCOIL',
                                                       width='BNG_COIL_R'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])							  