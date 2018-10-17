saveProjectAs('20181010_prot1_drot20mm_metglas.FLU')

#! Thu Oct 11 10:04:33 CEST 2018 loadProject('C:/Users/jperalta/Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_with_hole/sims/20181010_prot1_drot20mm_metglas.FLU')

Scenario(name='08_DISP0_ANGLE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['08_DISP0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.0))

Scenario['08_DISP0_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))

Scenario['08_DISP0_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                    value=0.0))

endMacroTransaction()

startMacroTransaction()
Scenario['08_DISP0_ANGLE'].pilots['DR_0']=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.0)
Scenario['08_DISP0_ANGLE'].pilots['DTHETA_0']=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                        value=0.0)
endMacroTransaction()

Scenario(name='09_DISP0_ANGLE_JT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                       value=0.0))

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                         intervals=[IntervalStepValue(minValue=0.0,
                                                                                      maxValue=350.0,
                                                                                      stepValue=10.0)]))

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                       value=0.0))

Scenario['09_DISP0_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))

endMacroTransaction()

Scenario(name='10_DISP0_ANGLE_JF',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                       value=0.0))

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                         intervals=[IntervalStepValue(minValue=0.0,
                                                                                      maxValue=350.0,
                                                                                      stepValue=10.0)]))

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA_0'],
                                                       value=0.0))

Scenario['10_DISP0_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))

endMacroTransaction()

saveProject()

#! Thu Oct 11 10:42:55 CEST 2018 loadProject('C:/Users/jperalta/Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_with_hole/sims/20181010_prot1_drot20mm_metglas.FLU')

Scenario(name='11_DISP_ANGLE',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['11_DISP_ANGLE'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.5))

Scenario['11_DISP_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))
                                                                                                       
Scenario['11_DISP_ANGLE'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
                                                                   intervals=[IntervalStepValue(minValue=0.0,
                                                                                                           maxValue=300.0,
                                                                                                           stepValue=60.0)]))

endMacroTransaction()

saveProject()

saveProject()

Scenario(name='12_DISP_ANGLE_JT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.5))

Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))
                                                                                                       
Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
                                                                   intervals=[IntervalStepValue(minValue=0.0,
                                                                                                           maxValue=300.0,
                                                                                                           stepValue=60.0)]))
                                                                                                           
Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))                                                                                                           

endMacroTransaction()

startMacroTransaction()
Scenario['12_DISP_ANGLE_JT'].removePilot(parameter=VariationParameter['JF_RMS'])
Scenario['12_DISP_ANGLE_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                        intervals=[IntervalStepValue(minValue=2.0,
                                                                                     maxValue=4.0,
                                                                                     stepValue=2.0)]))
endMacroTransaction()

Scenario(name='13_DISP_ANGLE_JF',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MonoValue(parameter=VariationParameter['DR_0'],
                                                    value=0.5))

Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA'],
                                                      intervals=[IntervalStepValue(minValue=0.0,
                                                                                   maxValue=350.0,
                                                                                   stepValue=10.0)]))
                                                                                                       
Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['DTHETA_0'],
                                                                   intervals=[IntervalStepValue(minValue=0.0,
                                                                                                           maxValue=300.0,
                                                                                                           stepValue=60.0)]))
                                                                                                           
Scenario['13_DISP_ANGLE_JF'].addPilot(pilot=MultiValues(parameter=VariationParameter['JF_RMS'],
                                                         intervals=[IntervalStepValue(minValue=2.0,
                                                                                      maxValue=4.0,
                                                                                      stepValue=2.0)]))                                                                                                           

endMacroTransaction()

saveProject()

