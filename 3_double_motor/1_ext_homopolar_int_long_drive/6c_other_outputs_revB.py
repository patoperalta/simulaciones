#! Flux3D 12.0
# some change of definitions

#other outputs which may be interesting to export

######BNG STATOR

lastInstance = VariationParameterFormula(name='R_OUT_ST_BNG_AUX : aux for outer radius of bearing stator',
                          formula='R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG')

lastInstance = VariationParameterFormula(name='A_BNG_ST : circular base area of bearing rotor',
                          formula='pi()*(R_OUT_ST_BNG_AUX^2-(R_OUT_ST_BNG_AUX-D_ST_BNG)^2)')
						  
lastInstance = VariationParameterFormula(name='D_MOT_AUX : ',
                          formula='2*(R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG)')	

lastInstance = VariationParameterFormula(name='ALPHA_CASE_AUX : ',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')							  

lastInstance = VariationParameterFormula(name='H_ST_BNG_AUX : height of BNG stator',
                          formula='D_MOT_AUX*(ALPHA_CASE_AUX*BETA_B+(1-ALPHA_CASE_AUX)*BETA_B/ALPHA_H)')						  
						  
lastInstance = VariationParameterFormula(name='H_PM_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_PERCENT_PM_TO_FE_BNG_ST*H_ST_BNG_AUX/2')						  
						  
lastInstance = VariationParameterFormula(name='H_FE_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_ST_BNG_AUX-2*H_PM_BNG_ST_AUX')						  

lastInstance = VariationParameterFormula(name='V_PM_BNG_ST : means ONE magnet, so count double the volume at end x2',
                          formula='A_BNG_ST*H_PM_BNG_ST_AUX')

lastInstance = VariationParameterFormula(name='V_FE_BNG_ST : ',
                          formula='A_BNG_ST*H_FE_BNG_ST_AUX')
						  
############################### BNG ROTOR
						  
lastInstance = VariationParameterFormula(name='A_BNG_ROT : circular base area of bearing rotor',
                          formula='pi()*(R_OUT_PM_ROT_BNG^2-(R_OUT_PM_ROT_BNG-D_PM_B_ROT)^2)')

lastInstance = VariationParameterFormula(name='H_ROT_B_AUX : height of BNG rotor',
                          formula='D_MOT_AUX*(ALPHA_CASE_AUX*ALPHA_H*BETA_B+(1-ALPHA_CASE_AUX)*BETA_B)')						  						  
						  
lastInstance = VariationParameterFormula(name='H_PM_ROT_B_AUX : height of one rotor BNG PM',
                          formula='H_ROT_B_AUX*H_PERCENT_PM_TO_FE_BNG_ROT/2')	
						  
lastInstance = VariationParameterFormula(name='V_PM_BNG_ROT : considers only one pm ring',
                          formula='A_BNG_ROT*H_PM_ROT_B_AUX')
						  
lastInstance = VariationParameterFormula(name='V_FE_BNG_ROT : ',
                          formula='A_BNG_ROT*H_ROT_B_AUX*(1-H_PERCENT_PM_TO_FE_BNG_ROT)')						  

############################		DRIVE	
			
lastInstance = VariationParameterFormula(name='R_OUT_ST_DRV_AUX : out radius of drv rotor',
                          formula='R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP')
						  
lastInstance = VariationParameterFormula(name='A_DRV_ST : circular base area of bearing rotor',
                          formula='pi()*(R_OUT_ST_DRV_AUX^2-(R_OUT_ST_DRV_AUX-D_ST_BNG)^2)')						  
						  
lastInstance = VariationParameterFormula(name='V_FE_DRV_ST : iron in drive stator',
                          formula='A_DRV_ST*(D_MOT_AUX*BETA_D)')

lastInstance = VariationParameterFormula(name='R_ROT_DRV_AUX : aux once again, outer radius drive pms',
                          formula='R_OUT_ST_DRV_AUX-D_DRV_ST-D_AGAP_D')

lastInstance = VariationParameterFormula(name='V_PM_DRV_ROT',
                          formula='pi()*(R_ROT_DRV_AUX^2)*(D_MOT_AUX*BETA_D)')

###########################

lastInstance = VariationParameterFormula(name='OUT_V_FE',
                          formula='V_FE_BNG_ST+V_FE_BNG_ROT+V_FE_DRV_ST')

lastInstance = VariationParameterFormula(name='OUT_V_PM',
                          formula='V_PM_BNG_ROT*2+V_PM_BNG_ST*2+V_PM_DRV_ROT')

lastInstance = VariationParameterFormula(name='OUT_V_CU',
                          formula='(6*BNG_A_CU*BNG_L_BAR_PH+3*DRV_A_CU*DRV_LCA)/COIL_KCU')