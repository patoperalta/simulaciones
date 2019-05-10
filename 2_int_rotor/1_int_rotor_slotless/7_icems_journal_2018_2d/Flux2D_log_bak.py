#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Desktop/03_flux_int_rotor_slotless/9_icems_2d/20190510_slotless_2d.FLU')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

closeProject()

exit()
