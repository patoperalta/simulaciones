#! Flux3D 12.0
# some change of definitions

##rev D has square, 'realistic' coils

##rev E will, on the other hand, use radial coils, which give more space
##it will also be compacter 

##revF was used for... sonceboz CTI #5 or #6

##rev G is made for the ICEMS paper, now considering a D_MECHGAP which can be changed

##these parameters were taken from rev D, and are there for aesthetic purposes only
lastInstance = ParameterGeom(name='M_R_THEO : m for theoretical radial thickness',
              expression='.3394')	
			  
lastInstance = ParameterGeom(name='N_R_THEO : n for theoretical radial thickness',
              expression='0')				  

lastInstance = ParameterGeom(name='COIL_R_THEO : theoretical coil radial thickness, see excel',
              expression='M_R_THEO*R_ST_OUT+N_R_THEO')	
			  
lastInstance = ParameterGeom(name='COIL_R_CASE : if 0, max coil thickness is limited by airgap',
              expression='Valid(COIL_R_THEO,0,D_AGAP-D_MECHGAP)')				  

lastInstance = ParameterGeom(name='COIL_R : real coil radial thickness, see excel v2',
              expression='COIL_R_CASE*COIL_R_THEO+(1-COIL_R_CASE)*(D_AGAP-D_MECHGAP)')	
			  
lastInstance = ParameterGeom(name='COIL_WCOIL : toroidal coil width',
              expression='2*pi()/6*(R_ST_IN-COIL_R)*0+3')	
			  
lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')	

## now start with the theoretical parameters of the radially oriented coils
lastInstance = VariationParameterFormula(name='TH_COIL_CIRC : theoretical thickness, see 2.2.2018',
                          formula='D_AGAP-D_MECHGAP')	

lastInstance = VariationParameterFormula(name='R_ST_IN_PH',
                          formula='R_ROT_OUT+D_AGAP')
						  
lastInstance = VariationParameterFormula(name='A_COIL : area of each coil',
                          formula='pi()/6*(R_ST_IN_PH^2-(R_ST_IN_PH-TH_COIL_CIRC)^2)')	
						  
lastInstance = VariationParameterFormula(name='A_CU',
                          formula='A_COIL*COIL_KCU')		

##now the length and therefore resistance
lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')
if tuning==1:
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='5+4*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*7/2')
elif tuning==2:
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='8+6*ValidLR(R_ROT_OUT,11,21,1,1)+6*ValidLR(R_ROT_OUT,19,21,1,1)')
elif tuning==3:
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='6+5*ValidLR(R_ROT_OUT,11,21,1,1)+6*ValidLR(R_ROT_OUT,19,21,1,1)')			  
elif tuning==4:
	lastInstance = VariationParameterFormula(name='D_ST_PH : r=(10,15,20)->d=(6,11,17)',
							  formula='D_ST')

## displacements as output							  
lastInstance = VariationParameterFormula(name='DALPHA_OUT',
						  formula='DALPHA_MULT*R_ROT_OUT/4')	

lastInstance = VariationParameterFormula(name='DBETA_OUT',
						  formula='DBETA_MULT*R_ROT_OUT/4')	

lastInstance = VariationParameterFormula(name='DX_OUT',
						  formula='DX_MULT*R_ROT_OUT/12')		

lastInstance = VariationParameterFormula(name='DY_OUT',
						  formula='DY_MULT*R_ROT_OUT/12')							  
						  
lastInstance = VariationParameterFormula(name='DZ_OUT',
						  formula='DZ_MULT*R_ROT_OUT/5')						  							  
							  
lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ROT_OUT+D_AGAP+D_ST_PH')						  

lastInstance = VariationParameterFormula(name='H_ST_PH',
                          formula='2*R_ST_OUT_PH*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')	
						  
lastInstance = VariationParameterFormula(name='L_BAR_PH',
                          formula='2*(H_ST_PH+D_ST_PH)+2*pi()*TH_COIL_CIRC/2')	
						  
lastInstance = VariationParameterFormula(name='R_ROT_PH',
                          formula='R_ROT_OUT')							  

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
                        referenceValue=150)

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

## now volume outputs	
lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ST_OUT_PH*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')
						  
lastInstance = VariationParameterFormula(name='V_FE_ST : volume of the iron of rotor',
                          formula='pi()*((R_ST_OUT_PH)^2-(R_ST_IN_PH)^2)*H_ST_PH')					  
						  
lastInstance = VariationParameterFormula(name='V_PM : PM volume',
                          formula='pi()*R_ROT_PH^2*H_ROT_PH')		

lastInstance = VariationParameterFormula(name='V_CU : copper volume',
                          formula='6*L_BAR_PH*A_CU/COIL_KCU')
						  
lastInstance = VariationParameterFormula(name='DENS_NO12 : no12 cogent google in g/mm^3',
                          formula='7.65/1000')							  
						  
lastInstance = VariationParameterFormula(name='DENS_CU : cu wiki in g/mm^3',
                          formula='8.96/1000')		

lastInstance = VariationParameterFormula(name='DENS_NDFEB : ndfeb wiki in g/mm^3',
                          formula='1/2*(7.3+7.7)/1000')	

lastInstance = VariationParameterFormula(name='MASS_ST',
                          formula='V_FE_ST*DENS_NO12')
						  
lastInstance = VariationParameterFormula(name='MASS_CU',
                          formula='V_CU*DENS_CU')
						  
lastInstance = VariationParameterFormula(name='MASS_PM',
                          formula='V_PM*DENS_NDFEB')							  						  

##now loop what is needed for each coil	
##define coordinate system, current types, their sum and coils						  
for i in range(1,7):
	## coordinate system for coils
	lastInstance = CoordSysCartesian(name='COORD_COIL_'+str(i),
					parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
												angleUnit=AngleUnit['DEGREE']),
					origin=['1/2*(R_ST_OUT+r_st_in)*cosd(30+60*'+str(i-1)+')',
							'1/2*(R_ST_OUT+r_st_in)*sind(30+60*'+str(i-1)+')',
							'0'],
					rotationAngles=RotationAngles(angleX='90',
													angleY='30+60*'+str(i-1)+'',
													angleZ='0'),
					visibility=Visibility['VISIBLE'])
	# equations for torque current
	lastInstance = VariationParameterFormula(name='I_T_'+str(i),
							  formula='IT_HAT*Cosd(1*DTHETA-THETA_T+'+str((i-1)*60)+')')					
	# equations for force current							  
	lastInstance = VariationParameterFormula(name='I_F_'+str(i),
							  formula='IF_HAT*Cosd(1*DTHETA-THETA_F+'+str((i-1)*120)+')')
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