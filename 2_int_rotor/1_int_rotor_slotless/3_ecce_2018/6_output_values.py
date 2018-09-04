#! Flux3D 12.0
# some change of definitions			  

## auxs		
lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')	

lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ST_OUT*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')

lastInstance = VariationParameterFormula(name='H_ST_PH',
                          formula='2*R_ST_OUT*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')

lastInstance = VariationParameterFormula(name='D_ST_PH',
                          formula='K_D_ST*R_ST_OUT')	

lastInstance = VariationParameterFormula(name='R_ST_IN_PH',
                          formula='R_ST_OUT-D_ST_PH')

lastInstance = VariationParameterFormula(name='D_AGAP_PH : airgap thickness for both cases',
              formula='DEF_AGAP*FIX_AGAP+(1-FIX_AGAP)*K_AGAP*R_ST_OUT')
			  
lastInstance = VariationParameterFormula(name='R_ROT_OUT_PH',
                          formula='R_ST_IN_PH-D_AGAP_PH')	

lastInstance = VariationParameterFormula(name='D_ROT_PH',
                          formula='K_D_ROT*R_ST_OUT')						  

lastInstance = VariationParameterFormula(name='R_ROT_IN_PH',
                          formula='R_ROT_OUT_PH-D_ROT_PH')			  
						  
## now volume outputs				  
						  
lastInstance = VariationParameterFormula(name='V_PM : PM volume',
                          formula='pi()*(R_ROT_OUT_PH^2-R_ROT_IN_PH^2)*H_ROT_PH')		

lastInstance = VariationParameterFormula(name='I_Z_V_PM : inertia over mass in z',
                          formula='1/2*(R_ROT_OUT_PH^2+R_ROT_IN_PH^2)')	

lastInstance = VariationParameterFormula(name='I_XY_V_PM : inertia over mass in x or y',
                          formula='1/12*(3*(R_ROT_OUT_PH^2+R_ROT_IN_PH^2)+H_ROT_PH^2)')						  