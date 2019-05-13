#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['F_ROT'])

CurveVariation2D['F_ROT_1'].delete()
EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

CurveVariation2D['TZ_ROT_1'].delete()
EvolutiveCurve2D(name='TZ_VS_JT',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

Scenario['4_JFORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_VS_JF',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['DTHETA'],
                                                                             currentValue=30.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['JF_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['F_ROT'])

Curve2d['F_ROT_VS_JF'].visible=0

Scenario['4_JFORCE'].deleteAllResults()

startMacroTransaction()
Scenario['4_JFORCE'].removePilot(parameter=VariationParameter['DTHETA'])
endMacroTransaction()

saveProject()

Scenario['4_JFORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_VS_JF_2',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JF_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['F_ROT'])

startMacroTransaction()
Scenario['6_THETA_FORCE'].removePilot(parameter=VariationParameter['DTHETA'])
endMacroTransaction()

Scenario['6_THETA_FORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['JF_RMS'],
                                                                             currentValue=6.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['THETA_F0'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=175.0)]),
                 formula=['F_ROT'])

closeProject()

exit()
