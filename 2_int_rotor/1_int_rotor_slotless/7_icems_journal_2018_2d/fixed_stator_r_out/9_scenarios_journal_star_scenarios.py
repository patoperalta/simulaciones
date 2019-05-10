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


