alpha=2
beta=0.1
l_slot=11
rrot=20
n=151

Scenario(name='BRMS_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

endMacroTransaction()