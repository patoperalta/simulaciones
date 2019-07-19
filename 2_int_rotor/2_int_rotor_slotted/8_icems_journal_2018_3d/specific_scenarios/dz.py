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

# alpha=2
# beta=0.2
# l_slot=9
# rrot=15
# n=85

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

Scenario(name='DZ_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DZ_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DZ_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DZ_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DZ_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DZ_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ_MULT'],
                                           value=1.0))

endMacroTransaction()