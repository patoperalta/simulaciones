#! Flux2D 18.1

## increasing the current density seems rather linear
startMacroTransaction()
Scenario['3_JTORQUE'].pilots['JT_RMS']=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                   intervals=[IntervalStepValue(minValue=0.0,
                                                                                maxValue=25.0,
                                                                                stepValue=1.0)])
endMacroTransaction()

## excite, and make the stator thinner...
## thinner stator seems to increase the torque
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

Scenario(name='8_D_ST_OPT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['8_D_ST_OPT'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_ST'],
                                                  intervals=[IntervalStepValue(minValue=3.0,
                                                                               maxValue=7.0,
                                                                               stepValue=0.5)]))

endMacroTransaction()


startMacroTransaction()

Scenario['9_D_AGAP_OPT'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                                    intervals=[IntervalStepValue(minValue=2.0,
                                                                                 maxValue=8.0,
                                                                                 stepValue=0.25)]))

endMacroTransaction()
