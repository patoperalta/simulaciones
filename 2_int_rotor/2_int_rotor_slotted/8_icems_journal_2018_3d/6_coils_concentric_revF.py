#! Flux3D 12.0

##see 2.2.2018					
##parameters of winding

##rev F is for ICEMS, no whole and stator outer radius is defined 18.05.2018

lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')	

lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')	

# ##geometry of coil			  
# lastInstance = VariationParameterFormula(name='D_ST_PH : stator thickness',
                          # formula='6+4*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')

# lastInstance = VariationParameterFormula(name='L_SLOT_PH : slot length',
                          # formula='7+ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*1.25')

# lastInstance = VariationParameterFormula(name='W_SLOT_PH',
                          # formula='6+3*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')

## now i have to define them otherwise...  since they are defined through functions (and not hard coded)			  
## copied from the checked 2d version of the slotted...
if tuning==1:
	lastInstance = VariationParameterFormula(name='L_SLOT_PH',
							  formula='7+ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*5/4')							  			  
							  
	lastInstance = VariationParameterFormula(name='W_SLOT_PH',
							  formula='6+3*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')							  			  						  
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='6+4*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')
elif tuning==2:								  
	lastInstance = VariationParameterFormula(name='L_SLOT_PH',
							  formula='9.25+3/2*ValidLR(R_ROT_OUT,11,21,1,1)+2.25*ValidLR(R_ROT_OUT,19,21,1,1)')
							  
	lastInstance = VariationParameterFormula(name='W_SLOT_PH',
							  formula='10+4*ValidLR(R_ROT_OUT,11,21,1,1)+6*ValidLR(R_ROT_OUT,19,21,1,1)')							  			  						  
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='10+5*ValidLR(R_ROT_OUT,11,21,1,1)+7*ValidLR(R_ROT_OUT,19,21,1,1)')
elif tuning==3:								  
	lastInstance = VariationParameterFormula(name='L_SLOT_PH',
							  formula='7.5+2*ValidLR(R_ROT_OUT,11,21,1,1)+1*ValidLR(R_ROT_OUT,19,21,1,1)')
							  
	lastInstance = VariationParameterFormula(name='W_SLOT_PH',
							  formula='7+5*ValidLR(R_ROT_OUT,11,21,1,1)+4*ValidLR(R_ROT_OUT,19,21,1,1)')							  			  						  
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='8+5*ValidLR(R_ROT_OUT,11,21,1,1)+5*ValidLR(R_ROT_OUT,19,21,1,1)')		
elif tuning==4:					
				#free to roll with the parameters
	lastInstance = VariationParameterFormula(name='L_SLOT_PH',
							  formula='L_SLOT')
							  
	lastInstance = VariationParameterFormula(name='W_SLOT_PH',
							  formula='W_SLOT')
							  
	lastInstance = VariationParameterFormula(name='D_ST_PH',
							  formula='D_ST')						  

lastInstance = VariationParameterFormula(name='R_ST_IN_PH',
                          formula='R_ROT_OUT+D_AGAP+L_SLOT_PH')	
						  
lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ST_IN_PH+D_ST_PH')						  

lastInstance = VariationParameterFormula(name='ST_A_SLOT : stator area/slot',
                          formula='pi()*(R_ST_OUT_PH^2-(R_ST_OUT_PH-D_ST_PH-L_SLOT_PH)^2)/6')

lastInstance = VariationParameterFormula(name='ST_BI_SLOT : backiron area / slot',
                          formula='Pi()*(R_ST_OUT_PH**2-(R_ST_OUT_PH-D_ST_PH)**2)/6')

lastInstance = VariationParameterFormula(name='ST_TOOTH_A : tooth',
                          formula='W_SLOT_PH*L_SLOT_PH')

lastInstance = VariationParameterFormula(name='A_SLOT : = 2*A_COIL',
                          formula='ST_A_SLOT-ST_BI_SLOT-ST_TOOTH_A')

lastInstance = VariationParameterFormula(name='A_COIL',
                          formula='A_SLOT/2')

lastInstance = VariationParameterFormula(name='A_CU',
                          formula='A_COIL*COIL_KCU')
						  
lastInstance = VariationParameterFormula(name='TH_COIL : coil thickness to the sides, see 2.2.2018',
                          formula='((R_ST_IN_PH-W_SLOT_PH/2)*pi()/3-W_SLOT_PH)/2')

lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH : needed for stator height',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')							  
						  
lastInstance = VariationParameterFormula(name='H_ST_PH : needed for coil length',
                          formula='2*R_ST_OUT_PH*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')	
						  
lastInstance = VariationParameterFormula(name='L_BAR_PH',
                          formula='2*(H_ST_PH+W_SLOT_PH)+2*pi()*TH_COIL/2') 						  
						  
## parameters for torque
lastInstance = VariationParameterPilot(name='I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
						
lastInstance = VariationParameterPilot(name='THETA_T : torque generation angle degrees',
                        referenceValue=270)

lastInstance = VariationParameterPilot(name='JT_RMS : torque current density',
                        referenceValue=0.0)	

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(I_T_PEAK+JT_RMS*A_CU*sqrt(2))')				  						  

## parameters for force

lastInstance = VariationParameterPilot(name='I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=180)

lastInstance = VariationParameterPilot(name='THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
						
lastInstance = VariationParameterFormula(name='THETA_F : force direction angle degrees',
                        formula='THETA_F0-THETA_F_DIR')
						  
lastInstance = VariationParameterPilot(name='JF_RMS : force current density',
                        referenceValue=0.0)		

lastInstance = VariationParameterFormula(name='IF_HAT',
                          formula='(I_F_PEAK+JF_RMS*A_CU*sqrt(2))')	

lastInstance = VariationParameterFormula(name='R_COIL',
                          formula='rho_cu*L_BAR_PH*1e-3/(A_CU*1e-6)')	  
##losses						  
lastInstance = VariationParameterFormula(name='P_CU_TOT',
                          formula='6*R_COIL*(IF_HAT+IT_HAT)^2/2')	
						  
##do the coils nicely as in the last version
lastInstance = ParameterGeom(name='TH_COIL_OFFSET : space between stator and coil start',
              expression='R_ST_IN-Sqrt(R_ST_IN^2-(W_SLOT/2+TH_COIL)^2)+.1*0')

ParameterGeom(name='L_COIL : radial depth of coil',
              expression='R_ST_IN-sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)-TH_COIL_OFFSET')

# ParameterGeom(name='M_TH_COIL : m for radial thickness of coil',
              # expression='.184')					
			  
# ParameterGeom(name='N_TH_COIL : n for radial thickness of coil',
              # expression='0')				  

# ParameterGeom(name='TH_COIL : width obtained with matlab + excel',
              # expression='M_TH_COIL*r_st_out+N_TH_COIL')			  

for i in range(1,7):
	## coordinate system for coils
	lastInstance = CoordSysCartesian(name='COORD_COIL_'+str(i),
					parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
												angleUnit=AngleUnit['DEGREE']),
					origin=['R_ST_IN*cosd(30*0+60*'+str(i-1)+')',
							'R_ST_IN*sind(30*0+60*'+str(i-1)+')',
							'0*H_ST'],
					rotationAngles=RotationAngles(angleX='90',
													angleY='-90+60*'+str(i-1)+'',
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
                        'TH_COIL_OFFSET+L_COIL/2'],
                dimensions=['W_SLOT+TH_COIL',
                            'H_ST+TH_COIL'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='L_COIL',
                                                       width='TH_COIL'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])							  
				
## calculate volumes of different materials
lastInstance = VariationParameterFormula(name='V_FE_ST_RING : volume of iron ring of stator',
                          formula='pi()*(R_ST_OUT^2-(R_ST_OUT-D_ST_PH)^2)*H_ST_PH')	
				  
lastInstance = VariationParameterFormula(name='V_FE_ST_SLOTS : square volume of iron ring of stator',
                          formula='6*W_SLOT_PH*L_SLOT_PH*H_ST')	

lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ST_OUT*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')		
						  
lastInstance = VariationParameterFormula(name='V_PM : volume of pm ring',
                          formula='pi()*R_ROT_OUT^2*H_ROT_PH')		
						  
lastInstance = VariationParameterFormula(name='V_CU : volume of copper',
                          formula='6*L_BAR*A_CU')							  
						  
lastInstance = VariationParameterFormula(name='DENS_NO12 : no12 cogent google in g/mm^3',
                          formula='7.65/1000')							  
						  
lastInstance = VariationParameterFormula(name='DENS_CU : cu wiki in g/mm^3',
                          formula='8.96/1000')		

lastInstance = VariationParameterFormula(name='DENS_NDFEB : ndfeb wiki in g/mm^3',
                          formula='1/2*(7.3+7.7)/1000')		

lastInstance = VariationParameterFormula(name='MASS_ST',
                          formula='(V_FE_ST_RING+V_FE_ST_SLOTS)*DENS_NO12')
						  
lastInstance = VariationParameterFormula(name='MASS_CU',
                          formula='V_CU*DENS_CU')
						  
lastInstance = VariationParameterFormula(name='MASS_PM',
                          formula='V_PM*DENS_NDFEB')							  