#! Flux3D 12.0

#########################################################################################################################################################
##passive scenarios
#########################################################################################################################################################	

##############################		 	
Scenario(name='0_FIELD_R'+str(r_rot))

startMacroTransaction()

Scenario['0_FIELD_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['0_FIELD_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['0_FIELD_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['0_FIELD_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['0_FIELD_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['0_FIELD_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))											  
endMacroTransaction()

##############################
Scenario(name='1_DZ_R'+str(r_rot))

startMacroTransaction()

Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ_MULT'],
                                          value=1.0))

Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['1_DZ_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))	 
endMacroTransaction()

##############################

Scenario(name='2_DALPHA_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1.0))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

##############################

Scenario(name='3_DBETA_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1.0))								  			  

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																				 

endMacroTransaction()

##############################


Scenario(name='4_DX_R'+str(r_rot))

startMacroTransaction()

Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                          value=1))

Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['4_DX_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))	

##############################


Scenario(name='5_DY_R'+str(r_rot))

startMacroTransaction()

Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                          value=1))
										  
Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['5_DY_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																					 

endMacroTransaction()

############################		 	

Scenario(name='6_JT_R'+str(r_rot))

startMacroTransaction()

Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))	

Scenario['6_JT_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                          value=j))

endMacroTransaction()

############################

Scenario(name='7_JF_R'+str(r_rot))

startMacroTransaction()

Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                          value=j))

Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
																		 
Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['7_JF_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))										  
endMacroTransaction()