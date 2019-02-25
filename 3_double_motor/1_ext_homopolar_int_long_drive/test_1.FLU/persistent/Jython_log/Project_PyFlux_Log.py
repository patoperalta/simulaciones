saveProject()

#! Mon Feb 25 10:00:32 CET 2019 loadProject('C:/Users/jperalta/Documents/github_pato/flux/3_double_motor/1_ext_homopolar_int_long_drive/test_1.FLU')

#other outputs which may be interesting to export

lastInstance = VariationParameterFormula(name='OUT_R_ROT_OUT_BNG : out radius of bng rotor',
                          formula='R_OUT_PM_ROT_BNG')

lastInstance = VariationParameterFormula(name='OUT_R_ROT_OUT_DRV : out radius of drv rotor',
                          formula='(R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP)')
                                
lastInstance = VariationParameterFormula(name='R_IN_PM_ROT_BNG : inner radius bng rotor',
                          formula='R_OUT_PM_ROT_BNG-D_ST_B')     

lastInstance = VariationParameterFormula(name='H_PM_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_PM_BNG_ST')

saveProject()

#! Mon Feb 25 10:03:44 CET 2019 loadProject('C:/Users/jperalta/Documents/github_pato/flux/3_double_motor/1_ext_homopolar_int_long_drive/test_1.FLU')

saveProject()

