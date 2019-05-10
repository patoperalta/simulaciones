#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

## excite, and make the stator thinner...
## thinner stator seems to increase the torque
Scenario(name='7_JTORQUE_DST',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['7_JTORQUE_DST'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_ST'],
                                                     intervals=[IntervalStepValue(minValue=1.0,
                                                                                  maxValue=8.0,
                                                                                  stepValue=0.5)]))

Scenario['7_JTORQUE_DST'].addPilot(pilot=MonoValue(parameter=VariationParameter['JT_RMS'],
                                                   value=10.0))

endMacroTransaction()

##orient PM
orientRegSurfMaterial(region=RegionFace['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')     

Scenario['5_THETA_TORQUE'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/5_icems_journal_2d/20190509_slotted_2d_1')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=6.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['THETA_T'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=175.0)]),
                 formula=['TZ_ROT'])

Scenario['7_JTORQUE_DST'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/5_icems_journal_2d/20190509_slotted_2d_1.FLU')

EvolutiveCurve2D(name='TZ_ROT_2',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['D_ST'],
                                                                                 limitMin=1.0,
                                                                                 limitMax=8.0),
                                                           SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                             currentValue=10.0)]),
                 formula=['TZ_ROT'])

saveProject()

closeProject()

exit()
