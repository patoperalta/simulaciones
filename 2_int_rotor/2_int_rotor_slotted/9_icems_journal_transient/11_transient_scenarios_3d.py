##scenario
##general values
alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

n=1

##changing values
r_rot=10
wslot=7
dst=8
lslot=7

Scenario(name='PJ_ROT_'+str(r_rot)+'_N'+str(10*n))

startMacroTransaction()

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=60.0,
                                                                               stepValue=1.0)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                                  intervals=[IntervalStepValue(minValue=alpha_min,
                                                                               maxValue=alpha_max,
                                                                               stepValue=d_alpha)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                                  intervals=[IntervalStepValue(minValue=beta_min,
                                                                               maxValue=beta_max,
                                                                               stepValue=d_beta)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                                value=dst))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                                value=lslot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['N_PROP'],
                                                value=n))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=r_rot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                                value=wslot))

endMacroTransaction()

##changing values
r_rot=15
wslot=12
dst=13
lslot=9

Scenario(name='PJ_ROT_'+str(r_rot)+'_N'+str(10*n))

startMacroTransaction()

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=60.0,
                                                                               stepValue=1.0)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                                  intervals=[IntervalStepValue(minValue=alpha_min,
                                                                               maxValue=alpha_max,
                                                                               stepValue=d_alpha)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                                  intervals=[IntervalStepValue(minValue=beta_min,
                                                                               maxValue=beta_max,
                                                                               stepValue=d_beta)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                                value=dst))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                                value=lslot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['N_PROP'],
                                                value=n))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=r_rot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                                value=wslot))

endMacroTransaction()

##changing values
r_rot=20
wslot=16
dst=18
lslot=11

Scenario(name='PJ_ROT_'+str(r_rot)+'_N'+str(10*n))

startMacroTransaction()

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=60.0,
                                                                               stepValue=1.0)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                                  intervals=[IntervalStepValue(minValue=alpha_min,
                                                                               maxValue=alpha_max,
                                                                               stepValue=d_alpha)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                                  intervals=[IntervalStepValue(minValue=beta_min,
                                                                               maxValue=beta_max,
                                                                               stepValue=d_beta)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                                value=dst))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                                value=lslot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['N_PROP'],
                                                value=n))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=r_rot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                                value=wslot))

endMacroTransaction()