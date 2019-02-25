#! Flux3D 18.1
newProject()

GeomMeshOptions[1].methodAutomaticMeshVolume=OptimizeMeshGemsActivated(level=OptimizationStandard())

openModelerContext()


executeBatchSpy('1_param_revJ.py')                         # Defines different parameters

closeModelerContext()

executeBatchSpy('2_app_def.py')                              # Defines different parameters

executeBatchSpy('3_mesh_info.py')                         # Defines different parameters

executeBatchSpy('4_geom_revI.py')                             # Defines different parameters

executeBatchSpy('5_mat_def.py')                              # Defines different parameters

executeBatchSpy('6a_elec_circuit_saddle_wdg_drive_revB.py')      # Defines different parameters

executeBatchSpy('6b_bearing_coil_toroidal_revE.py')      # Defines different parameters



saveProjectAs('test_2.FLU')

lastInstance = VariationParameterFormula(name='D_MOT_AUX : ',
                          formula='2*(R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG)')     

saveProject()

lastInstance = VariationParameterFormula(name='ALPHA_CASE_AUX : ',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = VariationParameterFormula(name='H_ST_BNG_AUX : height of one rotor BNG PM',
                          formula='D_MOT_AUX*(ALPHA_CASE_AUX*BETA_B+(1-ALPHA_CASE_AUX)*BETA_B/ALPHA_H)')     

lastInstance = VariationParameterFormula(name='H_PM_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_PERCENT_PM_TO_FE_BNG_ST*H_ST_BNG_AUX/2')

lastInstance = VariationParameterFormula(name='V_PM_BNG_ST : means ONE magnet, so count double the volume at end x2',
                          formula='pi()*(R_OUT_PM_ROT_BNG^2-R_IN_PM_ROT_BNG^2)*H_PM_BNG_ST_AUX')

saveProject()

lastInstance = VariationParameterFormula(name='H_FE_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_ST_BNG_AUX-2*H_PM_BNG_ST_AUX')     

lastInstance = VariationParameterFormula(name='V_FE_BNG_ST : whole height minus two magnets',
                          formula='pi()*(R_OUT_PM_ROT_BNG^2-R_IN_PM_ROT_BNG^2)*H_FE_BNG_ST_AUX')

closeProject()

exit()
