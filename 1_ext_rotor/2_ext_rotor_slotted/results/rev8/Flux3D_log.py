#! Flux3D 12.0
loadProject('C:/Users/jperalta/Desktop/05_extrot_slotted/3_sonceboz_cti_5/sims/rev8/20180411_slotted_ext_rotor_rev8_n42_no12.FLU')

Scenario(name='8_ROUND_FORCE')

startMacroTransaction()

Scenario['8_ROUND_FORCE'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                   value=1.4))

Scenario['8_ROUND_FORCE'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                   value=0.5))

Scenario['8_ROUND_FORCE'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                   value=1.5))

Scenario['8_ROUND_FORCE'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                                   value=10.0))

Scenario['8_ROUND_FORCE'].addPilot(pilot=MultiValues(parameter=VariationParameter['THETA_F_DIR'],
                                                     intervals=[IntervalStepValue(minValue=0.0,
                                                                                  maxValue=350.0,
                                                                                  stepValue=10.0)]))

endMacroTransaction()

Scenario['8_ROUND_FORCE'].solve(projectName='C:/Users/jperalta/Desktop/05_extrot_slotted/3_sonceboz_cti_5/sims/rev8/20180411_slotted_ext_rotor_rev8_n42_no12.FLU')

EvolutiveCurve2D(name='F_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['ALPHA_H'],
                                                                             currentValue=1.4),
                                                           SetParameterFixed(paramEvol=VariationParameter['BETA'],
                                                                             currentValue=0.5),
                                                           SetParameterFixed(paramEvol=VariationParameter['D_AGAP'],
                                                                             currentValue=1.5),
                                                           SetParameterFixed(paramEvol=VariationParameter['JF_RMS'],
                                                                             currentValue=10.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['THETA_F_DIR'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=350.0)]),
                 formula=['SENSOR[F_ROT]'])

saveProject()

closeProject()

exit()
