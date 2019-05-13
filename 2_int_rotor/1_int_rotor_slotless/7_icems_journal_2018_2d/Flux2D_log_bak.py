#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotless_2d.FLU')

EvolutiveCurve2D(name='TZ_ROT_vs_JT',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

DeleteAllResults(deletePostprocessingResults='yes')

startMacroTransaction()
Scenario['3_JTORQUE'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                                 intervals=[IntervalStepValue(minValue=1.0,
                                                                              maxValue=7.0,
                                                                              stepValue=0.5)]))
Scenario['3_JTORQUE'].pilots['JT_RMS']=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                 value=10.0)
endMacroTransaction()

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotless_2d.FLU')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
                                                                                 limitMin=2.5,
                                                                                 limitMax=7.0),
                                                           SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=10.0)]),
                 formula=['TZ_ROT'])

closeProject()

exit()
