#! Flux3D 12.0

#########################################################################################################################################################
##active scenarios
#########################################################################################################################################################	

alpha = 2
 
beta = 0.3

dgap = 3

j=6

###########################################################################################################		 	
#no radial displacement, turning rotor, no torque current

Scenario(name='DISP_0_ANGLE')

startMacroTransaction()

Scenario['DISP_0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                           value=alpha))

Scenario['DISP_0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                           value=beta))

Scenario['DISP_0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                           value=0.0))

Scenario['DISP_0_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=350.0,
                                                                                          stepValue=10.0)]))

Scenario['DISP_0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                           value=0.0))

Scenario['DISP_0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                           value=dgap))

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current

Scenario(name='DISP_0_ANGLE_JT')

startMacroTransaction()

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                           value=alpha))

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                           value=beta))

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                           value=0.0))

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=350.0,
                                                                                          stepValue=10.0)]))

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                           value=0.0))

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                           value=dgap))

Scenario['DISP_0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                           value=j))

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current

Scenario(name='DISP_0_ANGLE_JF')

startMacroTransaction()

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                           value=alpha))

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                           value=beta))

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                           value=0.0))

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=350.0,
                                                                                          stepValue=10.0)]))

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                           value=0.0))

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                           value=dgap))

Scenario['DISP_0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                                           value=j))

endMacroTransaction()


###########################################################################################################		 	
#no radial displacement, turning rotor, no torque current

Scenario(name='DISP_ANGLE')

startMacroTransaction()

Scenario['DISP_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                           value=alpha))

Scenario['DISP_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                           value=beta))

Scenario['DISP_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                           value=0.5))

Scenario['DISP_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=350.0,
                                                                                          stepValue=10.0)]))

Scenario['DISP_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=300.0,
                                                                                          stepValue=60.0)]))

Scenario['DISP_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                           value=dgap))

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current

Scenario(name='DISP_ANGLE_JT')

startMacroTransaction()

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                           value=alpha))

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                           value=beta))

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                           value=0.5))

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=350.0,
                                                                                          stepValue=10.0)]))

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=300.0,
                                                                                          stepValue=60.0)]))

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                           value=dgap))

Scenario['DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                           value=j))

endMacroTransaction()

###########################################################################################################

#no radial displacement, turning rotor, torque current

Scenario(name='DISP_ANGLE_JF')

startMacroTransaction()

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                                           value=alpha))

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                                           value=beta))

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                           value=0.5))

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=350.0,
                                                                                          stepValue=10.0)]))

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
                                                             intervals=[IntervalStepValue(minValue=0.0,
                                                                                          maxValue=300.0,
                                                                                          stepValue=60.0)]))

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['D_AGAP'],
                                                           value=dgap))

Scenario['DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                                           value=j))

endMacroTransaction()