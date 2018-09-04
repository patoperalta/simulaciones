#! Flux3D 12.0

#########################################################################################################################################################
##active scenarios
#########################################################################################################################################################	

# alpha_min = 1.0
# alpha_max = 2
# d_alpha= 0.2
 
# beta_min = 0.1
# beta_max = 0.5
# d_beta= 0.1

# lslot_min = 2
# lslot_max = 4 
# d_dgap= 1

# rmot_min = 15
# rmot_max = 25
# d_rmot= 5

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

Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))

Scenario['6_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                          value=j))																	 
Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
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

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))

Scenario['7_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                          value=j))		

Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
endMacroTransaction()