alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

dgap_min = 3
dgap_max = 6 
dgap_gap= 1
####################################
## specific for motor size
r_rot=10
dst=6

Scenario(name='2_DALPHA2_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=0.8))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=dgap_gap)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	


Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

Scenario(name='3_DBETA2_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=0.8))								  			  

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=dgap_gap)]))
																		 
Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()

####################################

## specific for motor size
r_rot=15
dst=11

Scenario(name='2_DALPHA2_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=0.8))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=dgap_gap)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	


Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

Scenario(name='3_DBETA2_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=0.8))								  			  

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=dgap_gap)]))
																		 
Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()


####################################
## specific for motor size
r_rot=20
dst=17

Scenario(name='2_DALPHA2_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=0.8))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=dgap_gap)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	


Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

Scenario(name='3_DBETA2_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=0.8))								  			  

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=dgap_gap)]))
																		 
Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()
####################################