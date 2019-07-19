#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

lastInstance = VariationParameterFormula(name='N_PROP',
                          formula='1')

lastInstance = VariationParameterFormula(name='N',
                          formula='N_PROP*161/(R_ROT_OUT/1000)*(60/(2*pi()))')

closeProject()

exit()
