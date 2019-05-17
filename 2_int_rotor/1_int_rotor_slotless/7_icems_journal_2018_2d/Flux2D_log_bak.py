#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario(name='TORQUE_JT10',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['TORQUE_JT10'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                 value=10.0))

Scenario['TORQUE_JT10'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                                   intervals=[IntervalStepValue(minValue=10.0,
                                                                                maxValue=20.0,
                                                                                stepValue=5.0)]))

endMacroTransaction()

Scenario['TORQUE_JT10'].solve(projectName='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/2d/post 3d/20160516_slotless_lslot_tuning_alpha15')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['R_ROT_OUT'],
                                                                                 limitMin=10.0,
                                                                                 limitMax=20.0),
                                                           SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=10.0)]),
                 formula=['TZ_ROT'])

closeProject()

exit()
