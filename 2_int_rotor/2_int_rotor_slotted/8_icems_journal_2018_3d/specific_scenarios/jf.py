j=8

# alpha=2
# beta=0.1
# l_slot=11
# rrot=20
# n=151

# alpha=1.6
# beta=0.2
# l_slot=13
# rrot=20
# n=191

alpha=1.8
beta=0.2
l_slot=13
rrot=20
n=192

Scenario(name='JF_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['JF_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['JF_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['JF_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['JF_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['JF_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['JF_RMS'],
                                           value=1.0))

endMacroTransaction()