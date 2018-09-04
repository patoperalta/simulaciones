#! Flux3D 12.0

#########################################################################################################################################################
##active scenarios
#########################################################################################################################################################	

alpha_min = 1.4
alpha_max = 2
d_alpha= 0.2
 
beta_b_min = 0.1
beta_b_max = 0.3
d_beta_b= 0.1

beta_d_min = 0.5
beta_d_max = 0.7
d_beta_d= 0.1

d_gap_d_min=2
d_gap_d_max=3
d_d_gap_d=.5

j=6

############################		 	

Scenario(name='6_JT')

startMacroTransaction()

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))																 

Scenario['6_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DRV_JT_RMS'],
                                          value=j))																	 

endMacroTransaction()

############################

Scenario(name='7_JF')

startMacroTransaction()

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))
																		 
Scenario['7_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['BNG_JF_RMS'],
                                          value=j))			

endMacroTransaction()