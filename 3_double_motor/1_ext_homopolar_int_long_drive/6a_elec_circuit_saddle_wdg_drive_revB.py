#! Flux3D 12.0
					
##parameters of copper
lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')	

lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')		

lastInstance = ParameterGeom(name='RHO_V_CU : wikipedia',
              expression='8.96*1000')		

##aesthetic parameters of coil
lastInstance = ParameterGeom(name='DRV_WDG_ANG_STR_P',
              expression='50')		
			  
lastInstance = ParameterGeom(name='DRV_WDG_ANG_CYL_P',
              expression='10')		
			  
lastInstance = ParameterGeom(name='DRV_COIL_ANG_TOT',
              expression='120')					  			  

lastInstance = ParameterGeom(name='DRV_COIL_L_STR_P',
              expression='.4*H_DRV')

lastInstance = VariationParameterFormula(name='BNG_R_B_ST_OUT : as auxiliary, define now instead of after',
                          formula='R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG')				  
			  			  
lastInstance = ParameterGeom(name='DRV_COIL_HALFHEIGHT_SADDLES',
              expression='.5*H_DRV')				  
			  
lastInstance = VariationParameterFormula(name='DRV_COIL_HALFHEIGHT_SADDLES_PH : as auxiliary, define now instead of after',
                          formula='.5*(2*BNG_R_B_ST_OUT)*beta_d')				  			  
			  
lastInstance = ParameterGeom(name='DRV_COIL_R_SADDLES',
              expression='R_OUT_ST_DRV-D_DRV_ST-.1')				  

lastInstance = ParameterGeom(name='DRV_COIL_TOTAL_ANGLE',
              expression='118')					  
			  
# lastInstance = ParameterGeom(name='DRV_COIL_NPOLES',
              # expression='1')		
			  
##parameters of real coil
lastInstance = VariationParameterFormula(name='DRV_COIL_R_TH : radial thickness drv coil',
                          formula='D_AGAP_D-.5')	

lastInstance = VariationParameterFormula(name='DRV_R_ST_IN_PH',
                          formula='R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP-D_ST_BNG')
						  
lastInstance = VariationParameterFormula(name='DRV_A_COIL : area of EACH coil, also S in 4.37 in pfister',
                          formula='(DRV_R_ST_IN_PH^2-(DRV_R_ST_IN_PH-DRV_COIL_R_TH)^2)*DRV_WDG_ANG_STR_P/360*pi()')
						  
lastInstance = VariationParameterFormula(name='DRV_A_CU',
                          formula='DRV_A_COIL*COIL_KCU')			  
						  
lastInstance = VariationParameterFormula(name='DRV_DELTA_1 : part of pg 59, 4.38 pfister ',
                          formula='(DRV_WDG_ANG_CYL_P/2+DRV_COIL_ANG_TOT/2)')							  

lastInstance = VariationParameterFormula(name='DRV_DELTA_2 : part of pg 59, 4.38 pfister ',
                          formula='DRV_R_ST_IN_PH+(DRV_R_ST_IN_PH-DRV_COIL_R_TH)')		
						  
lastInstance = VariationParameterFormula(name='DRV_DELTA : part of pg 59, 4.38 pfister ',
                          formula='1/4*DRV_DELTA_1*DRV_DELTA_2')							  

lastInstance = VariationParameterFormula(name='DRV_LCA : 4.39 pfister ',
                          formula='2*(2*DRV_COIL_HALFHEIGHT_SADDLES_PH)+2*pi()*DRV_DELTA')						  
						  
lastInstance = VariationParameterFormula(name='DRV_R_COIL',
                          formula='rho_cu*DRV_LCA*1e-3/(DRV_A_CU*1e-6)')							  
						  
## parameters for torque
lastInstance = VariationParameterPilot(name='DRV_I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
						
lastInstance = VariationParameterPilot(name='DRV_THETA_T : torque generation angle degrees',
                        referenceValue=90)

lastInstance = VariationParameterPilot(name='DRV_JT_RMS : torque current density',
                        referenceValue=0.0)	

lastInstance = VariationParameterFormula(name='DRV_IT_HAT',
                          formula='(DRV_I_T_PEAK+DRV_JT_RMS*DRV_A_CU*sqrt(2))')			

##now, copper losses
lastInstance = VariationParameterFormula(name='P_CU_TOT',
                          formula='3/2*DRV_R_COIL*(DRV_IT_HAT)^2')							  

#create coil and its things						  
for i in range(1,4):
	lastInstance = CoordSysCartesian(name='COORD_SYS_DRV_COIL_'+str(i),
					  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
					  origin=['0',
							  '0',
							  '0'],
					  rotationAngles=RotationAngles(angleX='0',
													angleY='0',
													angleZ='120*'+str(i-1)+''),
					  visibility=Visibility['VISIBLE'])					  
	# equations for torque current
	lastInstance = VariationParameterFormula(name='I_T_'+str(i),
							  formula='DRV_IT_HAT*Cosd(1*DTHETA-DRV_THETA_T+'+str((i-1)*120)+')')					
	# define current							
	lastInstance = CurrentStrandedCoil(name='I_DRV_'+str(i)+' : current in first drive coil',
						rmsModulus='I_T_'+str(i))						
	#create SADDLE coil
	lastInstance = SaddleCoil(name='Coil_DRV_'+str(i),
			   strandedCoil=CoilConductor['I_DRV_'+str(i)],
			   turnNumber='1',
			   seriesOrParallel=AllInSeries(),
			   coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
			   coordSys=CoordSys['COORD_SYS_DRV_COIL_'+str(i)],
			   center=['0',
					   '0',
					   '0'],
			   straightPartAngle='DRV_WDG_ANG_STR_P',
			   cylindricalPartAngle='DRV_WDG_ANG_CYL_P',
			   straightPartLength='DRV_COIL_L_STR_P',
			   semiInternalHeight='DRV_COIL_HALFHEIGHT_SADDLES',
			   radius='DRV_COIL_R_SADDLES',
			   totalAngle='DRV_COIL_ANG_TOT',
			   fillFactor='1',
			   resistivity='1',
			   volumicMass='1',
			   color=Color['White'],
			   visibility=Visibility['VISIBLE'])
				
## MISSING LOSSES, see pfister pg 49,59,101