#! Flux3D 12.0
# some change of definitions because airgap is now directly fixed				

##auxiliary quantities which are not copied				
lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')
						  
lastInstance = VariationParameterFormula(name='D_ROT_PH : rotor thickness',
                          formula='K_D_ROT*R_ROT_OUT')						  
						  
lastInstance = VariationParameterFormula(name='D_MAG_PH',
                          formula='K_D_MAG*R_ROT_OUT')						  

lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ROT_OUT*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')
						  
lastInstance = VariationParameterFormula(name='D_AGAP_PH',
                          formula='DEF_AGAP*FIX_AGAP+(1-FIX_AGAP)*K_AGAP*R_ROT_OUT')	

lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ROT_OUT-D_ROT_PH-D_MAG_PH-D_AGAP_PH')
						  
lastInstance = VariationParameterFormula(name='D_ST_PH',
                          formula='K_D_ST*R_ROT_OUT')	

lastInstance = VariationParameterFormula(name='R_ROT_IN_PH',
                          formula='R_ROT_OUT-D_ROT_PH')	

lastInstance = VariationParameterFormula(name='H_ST_PH',
                          formula='2*R_ROT_OUT*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')

lastInstance = VariationParameterFormula(name='R_IN_PM',
                          formula='R_ROT_IN_PH-D_MAG_PH')				  

## now volume outputs							  
lastInstance = VariationParameterFormula(name='V_FE_ROT : volume of the iron of rotor',
                          formula='pi()*((R_ROT_OUT)^2-(R_ROT_OUT-D_ROT_PH)^2)*H_ROT_PH')					  

lastInstance = VariationParameterFormula(name='V_FE_ST : volume of the iron of rotor',
                          formula='pi()*((R_ST_OUT_PH)^2-(R_ST_OUT_PH-D_ST_PH)^2)*H_ST_PH')

lastInstance = VariationParameterFormula(name='V_PM : volume of the magnet in rotor',
                          formula='pi()*((R_ROT_IN_PH)^2-(R_IN_PM)^2)*H_ROT_PH*4*THETA_MAG/360')

## FE_ROT						  
lastInstance = VariationParameterFormula(name='I_XX_FE_ROT_AUX : multiply by rho',
                          formula='(H_ROT_PH^2+3*(R_ROT_OUT^2+R_ROT_IN_PH^2))')
						  
lastInstance = VariationParameterFormula(name='I_XX_FE_ROT : multiply by rho',
                          formula='pi()/12*(R_ROT_OUT^2-R_ROT_IN_PH^2)*H_ROT_PH*I_XX_FE_ROT_AUX')

lastInstance = VariationParameterFormula(name='I_YY_FE_ROT : multiply by rho',
                          formula='I_XX_FE_ROT')						  
						  
lastInstance = VariationParameterFormula(name='I_ZZ_FE_ROT : multiply by rho',
                          formula='pi()*H_ROT_PH/2*(R_ROT_OUT^4-R_ROT_IN_PH^4)')						  

## V_PM
lastInstance = VariationParameterFormula(name='I_XX_PM_AUX : multiply by rho',
                          formula='(H_ROT_PH^2+3*(R_ROT_IN_PH^2+R_IN_PM^2))')
						  
lastInstance = VariationParameterFormula(name='I_XX_PM : multiply by rho',
                          formula='1/6*H_ROT_PH*(R_ROT_IN_PH^2-R_IN_PM^2)*I_XX_PM_AUX*THETA_MAG*pi()/180')

lastInstance = VariationParameterFormula(name='I_YY_PM : multiply by rho, see inertia_calculations_revA',
                          formula='I_XX_PM')						  
						  
lastInstance = VariationParameterFormula(name='I_ZZ_PM : multiply by rho',
                          formula='H_ROT_PH*pi()/2*(R_ROT_IN_PH^4-R_IN_PM^4)')						  