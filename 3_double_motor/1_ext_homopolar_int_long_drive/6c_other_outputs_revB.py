#! Flux3D 12.0
# some change of definitions

#other outputs which may be interesting to export

lastInstance = VariationParameterFormula(name='OUT_R_ROT_OUT_BNG : out radius of bng rotor',
                          formula='R_B_PM_ROT_OUT')

lastInstance = VariationParameterFormula(name='OUT_R_ROT_OUT_DRV : out radius of drv rotor',
                          formula='(R_B_PM_ROT_OUT-D_PM_B_ROT-R_SEP)')

## BNG_H_L_PH is the height of the stator anyways
lastInstance = VariationParameterFormula(name='V_PM_BNG_ST : so at the end x2',
                          formula='pi()*(R_B_PM_ROT_OUT^2-(R_B_PM_ROT_OUT-D_ST_B)^2)*BNG_H_L_PH*H_PER_PM_ST_B/2')

lastInstance = VariationParameterFormula(name='V_FE_BNG_ST',
                          formula='pi()*(R_B_PM_ROT_OUT**2-(R_B_PM_ROT_OUT-D_ST_B)**2)*BNG_H_L_PH*(1-H_PER_PM_ST_B)')

lastInstance = VariationParameterFormula(name='A_BNG_ROT : circular base area of bearing rotor',
                          formula='pi()*(OUT_R_ROT_OUT_BNG^2-(OUT_R_ROT_OUT_BNG-D_PM_B_ROT)^2)')
						  
## DRV_H_L_PH is the height of the stator anyways						  
lastInstance = VariationParameterFormula(name='V_PM_BNG_ROT : considers only one pm ring',
                          formula='A_BNG_ROT*DRV_H_L_PH*H_PER_PM_ROT_B/2')

lastInstance = VariationParameterFormula(name='V_FE_BNG_ROT : fe ring ',
                          formula='A_BNG_ROT*DRV_H_L_PH*(1-H_PER_PM_ROT_B)')
## aux
lastInstance = VariationParameterFormula(name='D_DR_FE_ROT_PH : aux for fe_drv_rot',
                          formula='K_D_DR_FE_ROT*R_B_PM_ROT_OUT')

lastInstance = VariationParameterFormula(name='V_FE_DRV_ROT : iron in drive rotor',
                          formula='pi()*(OUT_R_ROT_OUT_DRV^2-(OUT_R_ROT_OUT_DRV-D_DR_FE_ROT_PH)^2)*DRV_H_L_PH')

## aux
lastInstance = VariationParameterFormula(name='D_DR_PM_PH : aux for pm_drv_rot, pm drive rotor thickness',
                          formula='K_D_DR_PM*R_B_PM_ROT_OUT')	
## aux
lastInstance = VariationParameterFormula(name='R_OUT_PM : aux once again, outer radius drive pms',
                          formula='OUT_R_ROT_OUT_DRV-D_DR_FE_ROT_PH')

lastInstance = VariationParameterFormula(name='V_PM_DRV_ROT',
                          formula='pi()*(R_OUT_PM-(R_OUT_PM-D_DR_PM_PH)^2)*DRV_H_L_PH*THETA_MAG/90')

lastInstance = VariationParameterFormula(name='V_FE_DRV_ST : stator iron volume',
                          formula='(pi()*DRV_R_ST_OUT_PH^2-DRV_A_SLOT*6)*DRV_H_L_PH')	

## volumes
lastInstance = VariationParameterFormula(name='OUT_V_FE',
                          formula='V_FE_BNG_ST+V_FE_DRV_ROT+V_FE_DRV_ST+V_FE_BNG_ROT')

lastInstance = VariationParameterFormula(name='OUT_V_PM',
                          formula='V_PM_BNG_ROT*2+V_PM_BNG_ST*2+V_PM_DRV_ROT')

lastInstance = VariationParameterFormula(name='OUT_V_CU',
                          formula='6*(BNG_A_CU*BNG_L_BAR_PH+DRV_A_CU*DRV_L_BAR_PH)/COIL_KCU')

						  