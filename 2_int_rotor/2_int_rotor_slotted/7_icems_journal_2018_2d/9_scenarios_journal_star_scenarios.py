#! Flux2D 18.1

Scenario(name='7_D_ST',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['7_D_ST'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_ST'],
                                              intervals=[IntervalStepValue(minValue=3.0,
                                                                           maxValue=7.0,
                                                                           stepValue=0.5)]))

endMacroTransaction()

cenario(name='8_L_SLOT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['8_L_SLOT'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                              value=10.0))

Scenario['8_L_SLOT'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                                intervals=[IntervalStepValue(minValue=2.0,
                                                                             maxValue=10.0,
                                                                             stepValue=0.5)]))

endMacroTransaction()
startMacroTransaction()
Scenario['8_L_SLOT'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                              value=5.5))
endMacroTransaction()

