#! Flux3D 12.0

#########################################################################################################################################################

## in 9 and 10, mechanical gap is kept constant, and to this end, only the l_slot is changed, simulating then the change in airgap and therefore copper quantity in slotless motor
## now we fix lslot ~ copper quantity and change mechanical / magnetic airgap in this case

ParameterGeom['L_SLOT'].expression='3'

d_min = 2
d_max = 4 
d_dgap= 1

startMacroTransaction()
Scenario['0_FIELD'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['0_FIELD'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['1_DZ'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['2_DALPHA'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['3_DBETA'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['3_DBETA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['4_DX'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['4_DX'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['5_DY'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['5_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['6_JT'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['6_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()

startMacroTransaction()
Scenario['7_JF'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['7_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                               intervals=[IntervalStepValue(minValue=d_min,
                                                                            maxValue=d_max,
                                                                            stepValue=d_dgap)]))
endMacroTransaction()
