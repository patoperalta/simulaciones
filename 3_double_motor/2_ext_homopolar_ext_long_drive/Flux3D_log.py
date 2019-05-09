#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/3_double_motor/2_ext_homopolar_ext_long_drive/00_main.py')

Scenario(name='01_DZ_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['01_DZ_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DZ'],
                                               intervals=[IntervalStepValue(minValue=1.0,
                                                                            maxValue=5.0,
                                                                            stepValue=1.0)]))

endMacroTransaction()

saveProjectAs('../../../../../Desktop/double_mot_test.FLU')

Scenario['01_DZ_2'].delete()
Scenario(name='1_DZ_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['1_DZ_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DZ'],
                                              intervals=[IntervalStepValue(minValue=1.0,
                                                                           maxValue=5.0,
                                                                           stepValue=1.0)]))

endMacroTransaction()

Scenario(name='2_DALPHA_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['2_DALPHA_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DALPHA'],
                                                  intervals=[IntervalStepValue(minValue=2.0,
                                                                               maxValue=8.0,
                                                                               stepValue=2.0)]))

endMacroTransaction()

ParameterGeom['DALPHA'].expression='8'


ParameterGeom['DALPHA'].expression='6'


startMacroTransaction()
Scenario['2_DALPHA_2'].pilots['DALPHA']=MultiValues(parameter=VariationParameter['DALPHA'],
                                                    intervals=[IntervalStepValue(minValue=2.0,
                                                                                 maxValue=4.0,
                                                                                 stepValue=2.0)])
endMacroTransaction()

ParameterGeom['DALPHA'].expression='0'


Scenario(name='3_DBETA_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['3_DBETA_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DALPHA'],
                                                 intervals=[IntervalStepValue(minValue=2.0,
                                                                              maxValue=4.0,
                                                                              stepValue=2.0)]))

Scenario['3_DBETA_2'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                               value=45.0))

endMacroTransaction()

Scenario(name='4_DX_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['4_DX_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DX'],
                                              intervals=[IntervalStepValue(minValue=0.5,
                                                                           maxValue=1.0,
                                                                           stepValue=0.5)]))

endMacroTransaction()

Scenario['3_DBETA_2'].delete()
Scenario(name='6_JT_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['6_JT_2'].addPilot(pilot=MonoValue(parameter=VariationParameter['DRV_JT_RMS'],
                                            value=6.0))

Scenario['6_JT_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['DRV_THETA_T'],
                                              intervals=[IntervalStepValue(minValue=0.0,
                                                                           maxValue=150.0,
                                                                           stepValue=30.0)]))

endMacroTransaction()

saveProject()

saveProject()

meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()

Scenario['1_DZ_2'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

Scenario['2_DALPHA_2'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

Scenario['4_DX_2'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

Scenario['6_JT_2'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

selectCurrentStep(activeScenario=Scenario['6_JT_2'],
                  parameterValue=['DRV_JT_RMS=6.0',
                                  'DRV_THETA_T=150.0'])

EvolutiveCurve2D(name='TZ_DRV_BNG_ST_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['DRV_JT_RMS'],
                                                                             currentValue=6.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['DRV_THETA_T'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=150.0)]),
                 formula=['TZ_DRV_BNG_ST'])

Scenario(name='6_JT_1',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['6_JT_1'].addPilot(pilot=MonoValue(parameter=VariationParameter['BNG_JF_RMS'],
                                            value=6.0))

Scenario['6_JT_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['BNG_THETA_F0'],
                                              intervals=[IntervalStepValue(minValue=0.0,
                                                                           maxValue=170.0,
                                                                           stepValue=5.0)]))

endMacroTransaction()

startMacroTransaction()
Scenario['6_JT_1'].name='7_JF_2'
endMacroTransaction()

Scenario['7_JF_2'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

EvolutiveCurve2D(name='F_DRV_BNG_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['BNG_JF_RMS'],
                                                                             currentValue=6.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['BNG_THETA_F0'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=170.0)]),
                 formula=['F_DRV_BNG_ROT'])

saveProject()

closeProject()

exit()
