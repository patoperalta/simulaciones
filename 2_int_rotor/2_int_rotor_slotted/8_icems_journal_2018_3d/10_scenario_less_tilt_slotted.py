alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

j=8
## specific for motor size
r_rot=10
wslot=7
dst=8

lslot_min = 7
lslot_max = 10 
lslot_dgap= 1

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

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

##############################

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

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()

####################################

## specific for motor size
r_rot=15
wslot=12
dst=13

lslot_min = 9
lslot_max = 12 
lslot_dgap= 1

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

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

##############################

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

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()

####################################
## specific for motor size
r_rot=20
wslot=16
dst=18

lslot_min = 11
lslot_max = 14 
lslot_dgap= 1

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

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['2_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

##############################

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

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['3_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()

####################################