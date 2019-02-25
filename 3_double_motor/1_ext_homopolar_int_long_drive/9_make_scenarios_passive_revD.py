#! Flux3D 12.0

#########################################################################################################################################################
##passive scenarios
#########################################################################################################################################################	

alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_b_min = 0.1
beta_b_max = 0.3
d_beta_b= 0.1

beta_d_min = 0.5
beta_d_max = 0.7
d_beta_d= 0.1

r_sep_min = 2
r_sep_max = 4
r_sep_d= 1

d_gap_d_min=2
d_gap_d_max=3
d_d_gap_d=.5

##############################		 	
Scenario(name='0_FIELD')

startMacroTransaction()

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))
																		 
Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_SEP'],
                                            intervals=[IntervalStepValue(minValue=r_sep_min,
                                                                         maxValue=r_sep_max,
                                                                         stepValue=r_sep_d)]))																		 

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))				
endMacroTransaction()

##############################

Scenario(name='1_DZ')

startMacroTransaction()

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))

Scenario['1_DZ'].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ'],
                                          value=0.5))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))
																		 
Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_SEP'],
                                            intervals=[IntervalStepValue(minValue=r_sep_min,
                                                                         maxValue=r_sep_max,
                                                                         stepValue=r_sep_d)]))
																		 
Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))

endMacroTransaction()

##############################

Scenario(name='2_DALPHA')

startMacroTransaction()

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))

Scenario['2_DALPHA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA'],
                                          value=5))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))
																		 
Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_SEP'],
                                            intervals=[IntervalStepValue(minValue=r_sep_min,
                                                                         maxValue=r_sep_max,
                                                                         stepValue=r_sep_d)]))																		 

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))

endMacroTransaction()

##############################

Scenario(name='3_DBETA')

startMacroTransaction()

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))
																		 
Scenario['3_DBETA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA'],
                                          value=5))							  			  

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))
																		 
Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_SEP'],
                                            intervals=[IntervalStepValue(minValue=r_sep_min,
                                                                         maxValue=r_sep_max,
                                                                         stepValue=r_sep_d)]))																			 

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))

endMacroTransaction()

##############################


Scenario(name='4_DX')

startMacroTransaction()

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))

Scenario['4_DX'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX'],
                                          value=.5))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))
																		 
Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_SEP'],
                                            intervals=[IntervalStepValue(minValue=r_sep_min,
                                                                         maxValue=r_sep_max,
                                                                         stepValue=r_sep_d)]))																			 

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))

endMacroTransaction()

##############################


Scenario(name='5_DY')

startMacroTransaction()

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_B'],
                                            intervals=[IntervalStepValue(minValue=beta_b_min,
                                                                         maxValue=beta_b_max,
                                                                         stepValue=d_beta_b)]))
																		 
Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_SEP'],
                                            intervals=[IntervalStepValue(minValue=r_sep_min,
                                                                         maxValue=r_sep_max,
                                                                         stepValue=r_sep_d)]))																			 

Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX'],
                                          value=.5))
										  
Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA_D'],
                                            intervals=[IntervalStepValue(minValue=beta_d_min,
                                                                         maxValue=beta_d_max,
                                                                         stepValue=d_beta_d)]))

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP_D'],
                                            intervals=[IntervalStepValue(minValue=d_gap_d_min,
                                                                         maxValue=d_gap_d_max,
                                                                         stepValue=d_d_gap_d)]))

endMacroTransaction()
