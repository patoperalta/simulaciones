#! Flux3D 12.0

#########################################################################################################################################################
##active scenarios
#########################################################################################################################################################	
j=8

############################		 	

Scenario(name='6_JT')

startMacroTransaction()

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))

Scenario['6_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                          value=j))																	 

endMacroTransaction()

############################

Scenario(name='7_JF')

startMacroTransaction()

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))

Scenario['7_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                          value=j))																										
endMacroTransaction()