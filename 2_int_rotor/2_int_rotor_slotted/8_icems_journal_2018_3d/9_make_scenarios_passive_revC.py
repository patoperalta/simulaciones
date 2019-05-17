#! Flux3D 12.0

#########################################################################################################################################################
##passive scenarios
#########################################################################################################################################################	

alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

dgap_min = 2
dgap_max = 7 
d_dgap= 1

r_rot_min=10
r_rot_max=20
d_rot=5

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

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))
																		 
Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                               intervals=[IntervalStepValue(minValue=r_rot_min,
                                                                            maxValue=r_rot_max,
                                                                            stepValue=d_rot)]))																		 
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

Scenario['1_DZ'].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ_MULT'],
                                          value=1.0))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))
																		 
Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                               intervals=[IntervalStepValue(minValue=r_rot_min,
                                                                            maxValue=r_rot_max,
                                                                            stepValue=d_rot)]))			 
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

Scenario['2_DALPHA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1.0))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                               intervals=[IntervalStepValue(minValue=r_rot_min,
                                                                            maxValue=r_rot_max,
                                                                            stepValue=d_rot)]))																		 
																		 
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

Scenario['3_DBETA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1.0))								  			  

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))
																		 
Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                               intervals=[IntervalStepValue(minValue=r_rot_min,
                                                                            maxValue=r_rot_max,
                                                                            stepValue=d_rot)]))																				 

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

Scenario['4_DX'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                          value=1))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))
																		 
Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                               intervals=[IntervalStepValue(minValue=r_rot_min,
                                                                            maxValue=r_rot_max,
                                                                            stepValue=d_rot)]))												 
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

Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DY_MULT'],
                                          value=1))

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))
																		 
Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                               intervals=[IntervalStepValue(minValue=r_rot_min,
                                                                            maxValue=r_rot_max,
                                                                            stepValue=d_rot)]))																				 

endMacroTransaction()
