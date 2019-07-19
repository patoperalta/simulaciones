# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

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

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

alpha=1
beta=0.3
l_slot=14
rrot=20
n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()