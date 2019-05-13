#! Flux2D 18.1

###################################################################################################################
Scenario(name='0_FIELDS',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['0_FIELDS'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                intervals=[IntervalStepValue(minValue=0.0,
                                                                             maxValue=350.0,
                                                                             stepValue=5.0)]))

endMacroTransaction()
###################################################################################################################
Scenario(name='1_DX',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['1_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['DX'],
                                            intervals=[IntervalStepValue(minValue=0.1,
                                                                         maxValue=1.0,
                                                                         stepValue=0.1)]))

endMacroTransaction()
###################################################################################################################
Scenario(name='2_DY',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['2_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['DY'],
                                            intervals=[IntervalStepValue(minValue=0.1,
                                                                         maxValue=1.0,
                                                                         stepValue=0.1)]))

endMacroTransaction()
###################################################################################################################
Scenario(name='3_JTORQUE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['3_JTORQUE'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=25.0,
                                                                               stepValue=0.5)]))

endMacroTransaction()
###################################################################################################################
Scenario(name='4_JFORCE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['4_JFORCE'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                 intervals=[IntervalStepValue(minValue=0.0,
                                                                              maxValue=25.0,
                                                                              stepValue=0.5)]))

endMacroTransaction()
###################################################################################################################
Scenario(name='5_THETA_TORQUE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['5_THETA_TORQUE'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                    value=6.0))

Scenario['5_THETA_TORQUE'].addPilot(pilot=MultiValues(parameter=VariationParameter['THETA_T'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=175.0,
                                                                                   stepValue=5.0)]))

endMacroTransaction()

###################################################################################################################
Scenario(name='6_THETA_FORCE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['6_THETA_FORCE'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                                   value=6.0))


Scenario['6_THETA_FORCE'].addPilot(pilot=MultiValues(parameter=VariationParameter['THETA_F0'],
                                                     intervals=[IntervalStepValue(minValue=0.0,
                                                                                  maxValue=175.0,
                                                                                  stepValue=5.0)]))

endMacroTransaction()
