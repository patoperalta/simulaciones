#! Flux3D 12.0

###########################################################################################################		 	
#no radial displacement, turning rotor, no torque current

Scenario(name='08_DISP0_ANGLE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['08_DISP0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.0))

Scenario['08_DISP0_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))

Scenario['08_DISP0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                    value=0.0))

endMacroTransaction()

# startMacroTransaction()
# Scenario['08_DISP0_ANGLE'].pilots['DR_0']=MonoValue(parameter=VariationParameter['DR_0'],
                                                    # value=0.0)
# Scenario['08_DISP0_ANGLE'].pilots['DTHETA_0']=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                        # value=0.0)
# endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current

Scenario(name='09_DISP0_ANGLE_JT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                       value=0.0))

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                         intervals=[IntervalStepValue(minValue=0.0,
                                                                                      maxValue=350.0,
                                                                                      stepValue=10.0)]))

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                       value=0.0))

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, bearing current

Scenario(name='10_DISP0_ANGLE_JF',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                       value=0.0))

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                         intervals=[IntervalStepValue(minValue=0.0,
                                                                                      maxValue=350.0,
                                                                                      stepValue=10.0)]))

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                       value=0.0))

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))

endMacroTransaction()

###########################################################################################################		 	
#radial displacement, turning rotor

Scenario(name='11_DISP_ANGLE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['11_DISP_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.5))

Scenario['11_DISP_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))
																				   
Scenario['11_DISP_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
													  intervals=[IntervalStepValue(minValue=0.0,
																					  maxValue=300.0,
																					  stepValue=60.0)]))

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current

Scenario(name='12_DISP_ANGLE_JT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.5))

Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))
																				   
Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
													  intervals=[IntervalStepValue(minValue=0.0,
																					  maxValue=300.0,
																					  stepValue=60.0)]))
																					  
Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))																					  

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current
Scenario(name='13_DISP_ANGLE_JF',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.5))

Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))
																				   
Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
													  intervals=[IntervalStepValue(minValue=0.0,
																					  maxValue=300.0,
																					  stepValue=60.0)]))
																					  
Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))																					  

endMacroTransaction()