#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario['5_THETA_TORQUE'].solve(projectName='../../../../../../Desktop/03_flux_int_rotor_slotless/9_icems_2d/20190509_slotless_2d_1.FLU')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=6.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['THETA_T'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=175.0)]),
                 formula=['TZ_ROT'])

startMacroTransaction()
Scenario['3_JTORQUE'].pilots['JT_RMS']=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                   intervals=[IntervalStepValue(minValue=2.0,
                                                                                maxValue=12.0,
                                                                                stepValue=1.0)])
endMacroTransaction()

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Desktop/03_flux_int_rotor_slotless/9_icems_2d/20190509_slotless_2d_1.FLU')

CurveVariation2D['TZ_ROT_1'].delete()
displayIsovalues()

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=2.0,
                                                                                 limitMax=12.0)]),
                 formula=['TZ_ROT'])

displayIsovalues()

lastInstance = IsovalueSpatialGroup(name='ISOVAL_1',
                     formula='Comp(3,J)',
                     forceVisibility='yes',
                     smoothValues='yes',
                     group=[Groupspatial['4_NO_INFINITE']])

DeleteAllResults(deletePostprocessingResults='yes')

startMacroTransaction()
Scenario['3_JTORQUE'].pilots['JT_RMS']=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                   intervals=[IntervalStepValue(minValue=0.0,
                                                                                maxValue=25.0,
                                                                                stepValue=1.0)])
endMacroTransaction()

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Desktop/03_flux_int_rotor_slotless/9_icems_2d/20190509_slotless_2d_1.FLU')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

displayIsovalues()

Scenario(name='7_JTORQUE_DST',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['7_JTORQUE_DST'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_ST'],
                                                     intervals=[IntervalStepValue(minValue=1.0,
                                                                                  maxValue=8.0,
                                                                                  stepValue=0.5)]))

Scenario['7_JTORQUE_DST'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                   value=10.0))

endMacroTransaction()

Scenario['7_JTORQUE_DST'].solve(projectName='../../../../../../Desktop/03_flux_int_rotor_slotless/9_icems_2d/20190509_slotless_2d_1.FLU')

EvolutiveCurve2D(name='TZ_ROT_2',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['D_ST'],
                                                                                 limitMin=1.0,
                                                                                 limitMax=8.0),
                                                           SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=10.0)]),
                 formula=['TZ_ROT'])

selectCurrentStep(activeScenario=Scenario['7_JTORQUE_DST'],
                  parameterValue=['D_ST=2.0',
                                  'JT_RMS=10.0'])

saveProject()

closeProject()

exit()
