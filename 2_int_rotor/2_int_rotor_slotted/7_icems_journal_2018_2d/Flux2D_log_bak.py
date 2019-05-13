#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Desktop/slotted_2d_1.FLU')

selectCurrentStep(activeScenario=Scenario['3_JTORQUE'],
                  parameterValue=['JT_RMS=0.0'])

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


EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

Scenario(name='3_JTORQUE_1',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['3_JTORQUE_1'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                 value=10.0))

Scenario['3_JTORQUE_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                                   intervals=[IntervalStepValue(minValue=8.0,
                                                                                maxValue=15.0,
                                                                                stepValue=0.5)]))

endMacroTransaction()

Scenario['3_JTORQUE_1'].solve(projectName='../../../../../../Desktop/slotted_2d_1.FLU')

EvolutiveCurve2D(name='TZ_ROT_2',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['L_SLOT'],
                                                                                 limitMin=8.0,
                                                                                 limitMax=15.0),
                                                           SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=10.0)]),
                 formula=['TZ_ROT'])

saveProject()

selectCurrentStep(activeScenario=Scenario['3_JTORQUE_1'],
                  parameterValue=['L_SLOT=9.0',
                                  'JT_RMS=10.0'])

saveProject()

closeProject()

exit()
