#! Flux2D 18.1

##define regions without current
#########
lastInstance = RegionFace(name='IRON_ST',
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['NO12']),
           color=Color['Black'],
           visibility=Visibility['VISIBLE'])

lastInstance = RegionFace(name='PM',
           magneticDC2D=MagneticDC2DFaceMagnetic(material=Material['BMT_42UH']),
           color=Color['Red'],
           visibility=Visibility['VISIBLE'])
		   
lastInstance = RegionFace(name='AIRGAP',
           magneticDC2D=MagneticDC2DFaceVacuum(),
           color=Color['Turquoise'],
           visibility=Visibility['VISIBLE'])
	   		   
## coil geometric parameters
lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')	

## now i have to define them otherwise...  since they are defined through functions (and not hard coded)			  
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
			  
lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ROT_OUT+D_AGAP+L_SLOT_PH+D_ST_PH')			  
			  
lastInstance = VariationParameterFormula(name='ST_A_SLOT : stator area / slot',
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

##currents
##torque
lastInstance = VariationParameterPilot(name='I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
						
lastInstance = VariationParameterPilot(name='THETA_T : torque generation angle degrees',
                        referenceValue=270)

lastInstance = VariationParameterPilot(name='JT_RMS : torque current density',
                        referenceValue=0.0)			

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(I_T_PEAK+JT_RMS*A_CU*sqrt(2))')	

##force
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

##define currents
for i in range(1,7):
	# equations for torque current
	lastInstance = VariationParameterFormula(name='I_T_'+str(i),
							  formula='IT_HAT*Cosd(1*DTHETA-THETA_T+'+str((i-1)*60)+')')					
	# equations for force current							  
	lastInstance = VariationParameterFormula(name='I_F_'+str(i),
							  formula='IF_HAT*Cosd(1*DTHETA-THETA_F+'+str((i-1)*120)+')')
	# define current							
	lastInstance = CurrentStrandedCoil(name='I_'+str(i)+' : current in first drive coil',
						rmsModulus='I_T_'+str(i)+'+I_F_'+str(i))	 						  
	# define the coil face region
	lastInstance = RegionFace(name='COIL_PLUS_'+str(i),
			   magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='1',
																								seriesParallel=AllInSeries(),
																								electricComponent=CoilConductor['I_'+str(i)],
																								fillFactor='1'),
														  material=Material['AIR']),
			   color=Color['Green'],
			   visibility=Visibility['VISIBLE'])
	# define the coil face region
	lastInstance = RegionFace(name='COIL_MINUS_'+str(i),
			   magneticDC2D=MagneticDC2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='1',
																								seriesParallel=AllInSeries(),
																								electricComponent=CoilConductor['I_'+str(i)],
																								fillFactor='1'),
														  material=Material['AIR']),
			   color=Color['Yellow'],
			   visibility=Visibility['VISIBLE'])			   

##assign
assignRegionToFaces(face=[Face[5]],
                    region=RegionFace['INFINITE'])

assignRegionToFaces(face=[Face[1]],
                    region=RegionFace['IRON_ST'])

assignRegionToFaces(face=[Face[2]],
                    region=RegionFace['AIRGAP'])

assignRegionToFaces(face=[Face[16]],
                    region=RegionFace['PM'])

assignRegionToFaces(face=[Face[15]],
                    region=RegionFace['COIL_PLUS_1'])

assignRegionToFaces(face=[Face[10]],
                    region=RegionFace['COIL_MINUS_1'])

assignRegionToFaces(face=[Face[4]],
                    region=RegionFace['COIL_PLUS_2'])

assignRegionToFaces(face=[Face[3]],
                    region=RegionFace['COIL_MINUS_2'])

assignRegionToFaces(face=[Face[11]],
                    region=RegionFace['COIL_PLUS_3'])

assignRegionToFaces(face=[Face[6]],
                    region=RegionFace['COIL_MINUS_3'])

assignRegionToFaces(face=[Face[12]],
                    region=RegionFace['COIL_PLUS_4'])

assignRegionToFaces(face=[Face[7]],
                    region=RegionFace['COIL_MINUS_4'])

assignRegionToFaces(face=[Face[13]],
                    region=RegionFace['COIL_PLUS_5'])

assignRegionToFaces(face=[Face[8]],
                    region=RegionFace['COIL_MINUS_5'])

assignRegionToFaces(face=[Face[14]],
                    region=RegionFace['COIL_PLUS_6'])

assignRegionToFaces(face=[Face[9]],
                    region=RegionFace['COIL_MINUS_6'])

InfiniteBoxDisc['InfiniteBoxDisc'].setInvisible()
##PM direction
##orient PM
orientRegSurfMaterial(region=RegionFace['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')	