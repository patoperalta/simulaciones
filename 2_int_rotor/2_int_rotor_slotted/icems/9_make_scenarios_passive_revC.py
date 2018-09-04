#! Flux3D 12.0

#########################################################################################################################################################
##passive scenarios
#########################################################################################################################################################	

alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.5
d_beta= 0.1

lslot_min = 2
lslot_max = 4 
d_lslot= 1

rmot_min = 15
rmot_max = 25
d_rmot= 5

##############################		 	
Scenario(name='0_FIELD')

startMacroTransaction()

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
																		 
Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))

Scenario['0_FIELD'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                                           value=30.0))

endMacroTransaction()

##############################

Scenario(name='1_DZ')

startMacroTransaction()

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['1_DZ'].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ'],
                                          value=.5))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))
																		 
Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
																		 
endMacroTransaction()

##############################

Scenario(name='2_DALPHA')

startMacroTransaction()

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA'],
                                          value=5))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
																		 
endMacroTransaction()

##############################

Scenario(name='3_DBETA')

startMacroTransaction()

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA'],
                                          value=5))									  			  

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))
																		 
Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
endMacroTransaction()

##############################


Scenario(name='4_DX')

startMacroTransaction()

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['4_DX'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX'],
                                          value=.5))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))
																		 
Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
endMacroTransaction()

##############################


Scenario(name='5_DY')

startMacroTransaction()

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX'],
                                          value=.5))
										  
Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ST_OUT'],
                                            intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         maxValue=rmot_max,
                                                                         stepValue=d_rmot)]))
																		 
Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=d_lslot)]))

endMacroTransaction()
