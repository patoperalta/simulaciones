#! Flux3D 18.1

#########################################################################################################################################################
##passive scenarios
#########################################################################################################################################################	

alpha_min = 1.4
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

##only change stator pm / fe proportions
h_per_pm_min = .6
h_per_pm_max = .8 
d_h_per_pm_st= 0.1

rmot_min = 6.5
rmot_max = 7.5
d_rmot= 0.5

##############################		 	
Scenario(name='0_FIELD')

startMacroTransaction()

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['beta_b'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['H_PERCENT_PM_TO_FE_BNG_ST'],
                                            intervals=[IntervalStepValue(minValue=h_per_pm_min,
                                                                         maxValue=h_per_pm_max,
                                                                         stepValue=d_h_per_pm_st)]))

# Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()

##############################

Scenario(name='1_DZ')

startMacroTransaction()

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['beta_b'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['1_DZ'].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ'],
                                          value=1.0))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['H_PERCENT_PM_TO_FE_BNG_ST'],
                                            intervals=[IntervalStepValue(minValue=h_per_pm_min,
                                                                         maxValue=h_per_pm_max,
                                                                         stepValue=d_h_per_pm_st)]))

# Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()

##############################

Scenario(name='2_DALPHA')

startMacroTransaction()

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['beta_b'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA'],
                                          value=2.5))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['H_PERCENT_PM_TO_FE_BNG_ST'],
                                            intervals=[IntervalStepValue(minValue=h_per_pm_min,
                                                                         maxValue=h_per_pm_max,
                                                                         stepValue=d_h_per_pm_st)]))

# Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()

##############################

Scenario(name='3_DBETA')

startMacroTransaction()

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['beta_b'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA'],
                                          value=2.5))
										  
Scenario['3_DBETA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=45))								  			  

Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['H_PERCENT_PM_TO_FE_BNG_ST'],
                                            intervals=[IntervalStepValue(minValue=h_per_pm_min,
                                                                         maxValue=h_per_pm_max,
                                                                         stepValue=d_h_per_pm_st)]))

# Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()

##############################


Scenario(name='4_DX')

startMacroTransaction()

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['beta_b'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['4_DX'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX'],
                                          value=.5))

Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['H_PERCENT_PM_TO_FE_BNG_ST'],
                                            intervals=[IntervalStepValue(minValue=h_per_pm_min,
                                                                         maxValue=h_per_pm_max,
                                                                         stepValue=d_h_per_pm_st)]))

# Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()

##############################


Scenario(name='5_DY')

startMacroTransaction()

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['beta_b'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DX'],
                                          value=.5))
										  
Scenario['5_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=45))										  

Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['H_PERCENT_PM_TO_FE_BNG_ST'],
                                            intervals=[IntervalStepValue(minValue=h_per_pm_min,
                                                                         maxValue=h_per_pm_max,
                                                                         stepValue=d_h_per_pm_st)]))

# Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['R_ROT_OUT'],
                                            # intervals=[IntervalStepValue(minValue=rmot_min,
                                                                         # maxValue=rmot_max,
                                                                         # stepValue=d_rmot)]))

endMacroTransaction()
