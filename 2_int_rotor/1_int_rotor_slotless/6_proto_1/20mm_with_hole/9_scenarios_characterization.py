#! Flux3D 12.0

#########################################################################################################################################################
##passive scenarios
#########################################################################################################################################################	
Scenario(name='00_FIELDS',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['00_FIELDS'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                 intervals=[IntervalStepValue(minValue=0.0,
                                                                              maxValue=350.0,
                                                                              stepValue=10.0)]))

endMacroTransaction()

Scenario(name='01_DX',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['01_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['DX'],
                                             intervals=[IntervalStepValue(minValue=0.2,
                                                                          maxValue=1,
                                                                          stepValue=0.2)]))

endMacroTransaction()

Scenario(name='02_DY',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['02_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['DY'],
                                             intervals=[IntervalStepValue(minValue=0.2,
                                                                          maxValue=1,
                                                                          stepValue=0.2)]))

endMacroTransaction()

Scenario(name='03_DZ',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['03_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['DZ'],
                                             intervals=[IntervalStepValue(minValue=0.1,
                                                                          maxValue=1.5,
                                                                          stepValue=0.1)]))

endMacroTransaction()

Scenario(name='04_DALPHA',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['04_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['DALPHA'],
                                                 intervals=[IntervalStepValue(minValue=1.0,
                                                                              maxValue=10.0,
                                                                              stepValue=1.0)]))

endMacroTransaction()

Scenario(name='05_DBETA',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['05_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['DBETA'],
                                                intervals=[IntervalStepValue(minValue=1.0,
                                                                             maxValue=10.0,
                                                                             stepValue=1.0)]))

endMacroTransaction()

Scenario(name='06_JTORQUE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['06_JTORQUE'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                  intervals=[IntervalStepValue(minValue=2.0,
                                                                               maxValue=8.0,
                                                                               stepValue=2.0)]))

endMacroTransaction()

Scenario(name='07_JFORCE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['07_JFORCE'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                 intervals=[IntervalStepValue(minValue=2.0,
                                                                              maxValue=8.0,
                                                                              stepValue=2.0)]))

endMacroTransaction()
