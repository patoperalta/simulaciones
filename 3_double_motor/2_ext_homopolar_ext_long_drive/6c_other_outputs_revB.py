#! Flux3D 18.1
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

############################ drive rotor, fe

lastInstance = VariationParameterFormula(name='D_DR_FE_ROT_PH : aux for fe_drv_rot',
                          formula='K_D_DR_FE_ROT*R_OUT_PM_ROT_BNG')

lastInstance = VariationParameterFormula(name='R_ROT_OUT_DRV_AUX : out radius of drv rotor',
                          formula='(R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP)')						  
						  
lastInstance = VariationParameterFormula(name='A_FE_DRV_ROT : area of drive rotor FE ',
                          formula='pi()*(R_ROT_OUT_DRV_AUX^2-(R_ROT_OUT_DRV_AUX-D_DR_FE_ROT_PH)^2)')						  
						  
lastInstance = VariationParameterFormula(name='V_FE_DRV_ROT : volume iron in drive rotor',
                          formula='A_FE_DRV_ROT*D_MOT_AUX*beta_d')

############################ drive rotor, PM						  
						  
lastInstance = VariationParameterFormula(name='D_DR_PM_PH : aux for pm_drv_rot, pm drive rotor thickness',
                          formula='K_D_DR_PM*R_OUT_PM_ROT_BNG')	

lastInstance = VariationParameterFormula(name='R_OUT_PM : aux once again, outer radius drive pms',
                          formula='R_ROT_OUT_DRV_AUX-D_DR_FE_ROT_PH')

lastInstance = VariationParameterFormula(name='V_PM_DRV_ROT : already the 4 magnets',
                          formula='pi()*(R_OUT_PM-(R_OUT_PM-D_DR_PM_PH)^2)*D_MOT_AUX*beta_d*THETA_MAG/90')	
						  
################## stator FE	

lastInstance = VariationParameterFormula(name='V_FE_DRV_ST : stator iron volume',
                          formula='(pi()*DRV_R_ST_OUT_PH^2-DRV_A_SLOT*6)*D_MOT_AUX*beta_d')						  
						  
# volumes
lastInstance = VariationParameterFormula(name='OUT_V_FE',
                          formula='V_FE_BNG_ST+V_FE_BNG_ROT+V_FE_DRV_ROT+V_FE_DRV_ST')

lastInstance = VariationParameterFormula(name='OUT_V_PM',
                          formula='V_PM_BNG_ROT*2+V_PM_BNG_ST*2+V_PM_DRV_ROT')

lastInstance = VariationParameterFormula(name='OUT_V_CU',
                          formula='6*(BNG_A_CU*BNG_L_BAR_PH+DRV_A_CU*DRV_L_BAR_PH)/COIL_KCU')						  