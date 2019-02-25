#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/6_proto_1/20mm_with_hole/00_main.py')

saveProjectAs('20181010_prot1_drot20mm_metglas_characterization.FLU')

saveProjectAs('../../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_with_hole_v2/sims/20181116_prot_revB.FLU')

saveProject()

meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()

startMacroTransaction()
Scenario['01_DX'].pilots['DX']=MultiValues(parameter=VariationParameter['DX'],
                                           intervals=[IntervalStepValue(minValue=0.2,
                                                                        maxValue=1.0,
                                                                        stepValue=0.1)])
endMacroTransaction()

saveProject()

saveProjectAs('../../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_with_hole_v2/sims/20181116_inductance_pm.FLU')

CoilConductor['I_1'].rmsModulus='I_T_1+I_F_1+10'


closeProject()

exit()
