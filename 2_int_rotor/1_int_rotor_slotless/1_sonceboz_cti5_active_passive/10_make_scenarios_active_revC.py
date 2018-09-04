#! Flux3D 12.0

#########################################################################################################################################################
##active scenarios
#########################################################################################################################################################	

alpha_min = 1.4
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.5
d_beta= 0.1

dgap_min = 1.5
dgap_max = 3 
d_dgap= 0.5

rmot_min = 6.5
rmot_max = 7.5
d_rmot= 0.5

j=6

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

# Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                            # intervals=[IntervalStepValue(minValue=2.0,
                                                                         # maxValue=4.0,
                                                                         # stepValue=2.0)]))
Scenario['6_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                          value=j))																	 

# Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

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

# Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                            # intervals=[IntervalStepValue(minValue=2.0,
                                                                         # maxValue=4.0,
                                                                         # stepValue=2.0)]))
Scenario['7_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                          value=j))																																		 
# Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()