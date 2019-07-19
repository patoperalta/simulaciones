j=8

# alpha=1.6
# beta=0.3
# l_slot=7
# rrot=10
# n=17

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

alpha=2
beta=0.1
l_slot=11
rrot=20
n=151

Scenario(name='JT_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['JT_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['JT_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['JT_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['JT_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['JT_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                           value=1.0))

endMacroTransaction()