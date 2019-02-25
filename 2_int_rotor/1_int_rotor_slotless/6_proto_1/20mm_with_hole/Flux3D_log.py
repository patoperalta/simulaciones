#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/6_proto_1/20mm_with_hole/00_main.py')

RegionVolume['IRON_ST'].magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['METGLAS'])


saveProjectAs('../../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_dst_vs_bhcurves/20181120_metglas_1_excel.FLU')

ParameterGeom['D_ST'].expression='5'


ParameterGeom['D_ST'].expression='7'


Scenario(name='14_DST_JT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['14_DST_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_ST'],
                                                 intervals=[IntervalStepValue(minValue=2.0,
                                                                              maxValue=10.0,
                                                                              stepValue=1.0)]))

Scenario['14_DST_JT'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                 intervals=[IntervalStepValue(minValue=2.0,
                                                                              maxValue=6.0,
                                                                              stepValue=1.0)]))

endMacroTransaction()

saveProject()

saveProjectAs('../../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_dst_vs_bhcurves/20181120_metglas_2_pdf.FLU')

RegionVolume['IRON_ST'].magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['METGLAS_2605SA1'])


saveProject()

saveProjectAs('../../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_dst_vs_bhcurves/20181120_metglas_3_netl.FLU')

RegionVolume['IRON_ST'].magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['METGLAS_NETL'])


saveProject()

meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()          

Scenario['14_DST_JT'].solve(projectName='../../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_dst_vs_bhcurves/20181120_metglas_3_netl.FLU')

closeProject()

exit()
