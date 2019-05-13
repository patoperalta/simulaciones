#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Desktop/slotless_2d_1.FLU')

selectCurrentStep(activeScenario=Scenario['3_JTORQUE'],
                  parameterValue=['JT_RMS=0.0'])

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

lastInstance = IsovalueSpatialGroup(name='ISOVAL_1',
                     formula='B',
                     forceVisibility='yes',
                     smoothValues='yes',
                     group=[Groupspatial['S_AIRGAP'],
                            Groupspatial['S_COIL_MINUS_1'],
                            Groupspatial['S_COIL_MINUS_2'],
                            Groupspatial['S_COIL_MINUS_3'],
                            Groupspatial['S_COIL_MINUS_4'],
                            Groupspatial['S_COIL_MINUS_5'],
                            Groupspatial['S_COIL_MINUS_6'],
                            Groupspatial['S_COIL_PLUS_1'],
                            Groupspatial['S_COIL_PLUS_2'],
                            Groupspatial['S_COIL_PLUS_3'],
                            Groupspatial['S_COIL_PLUS_4'],
                            Groupspatial['S_COIL_PLUS_5'],
                            Groupspatial['S_COIL_PLUS_6'],
                            Groupspatial['S_IRON_ST'],
                            Groupspatial['S_PM']])


saveProject()

closeProject()

exit()
