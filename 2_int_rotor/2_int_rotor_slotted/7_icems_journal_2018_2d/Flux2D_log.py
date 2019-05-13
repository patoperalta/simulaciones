#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='TZ_ROT_VS_JT',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

Scenario['4_JFORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JF_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['F_ROT'])

Curve2d['F_ROT_1'].name='F_ROT_VS_JF'


startMacroTransaction()
Scenario['1_DX'].pilots['DX']=MultiValues(parameter=VariationParameter['DX'],
                                          intervals=[IntervalStepValue(minValue=0.1,
                                                                       maxValue=1.0,
                                                                       stepValue=0.1)])
endMacroTransaction()

Scenario['1_DX'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_VS_DX',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DX'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

saveProject()

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

Scenario['2_DY'].deleteAllResults()

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

Scenario['2_DY'].deleteAllResults()

startMacroTransaction()
Scenario['2_DY'].pilots['DY']=MultiValues(parameter=VariationParameter['DY'],
                                          intervals=[IntervalStepValue(minValue=0.1,
                                                                       maxValue=1.0,
                                                                       stepValue=0.1)])
endMacroTransaction()

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

EvolutiveCurve2D(name='F_ROT_VS_DY',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DY'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

saveProject()

Scenario['2_DY'].deleteAllResults()

Curve2d['F_ROT_VS_DY'].visible=0

CurveVariation2D['F_ROT_VS_DY'].delete()
startMacroTransaction()
Scenario['2_DY'].removePilot(parameter=VariationParameter['DY'])
Scenario['2_DY'].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90.0))
Scenario['2_DY'].addPilot(pilot=MultiValues(parameter=VariationParameter['DX'],
                                            intervals=[IntervalStepValue(minValue=0.1,
                                                                         maxValue=1.0,
                                                                         stepValue=0.1)]))
endMacroTransaction()

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d.FLU')

selectCurrentStep(activeScenario=Scenario['2_DY'],
                  parameterValue=['DTHETA=90.0',
                                  'DX=0.4'])

EvolutiveCurve2D(name='F_ROT_VS_DY',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['DTHETA'],
                                                                             currentValue=90.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['DX'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

saveProject()

saveProject()

saveProject()

CurveVariation2D['F_ROT_VS_DX'].exportTXT(txtFile='slotted_frot_dx',
          mode='add')

CurveVariation2D['F_ROT_VS_DX'].exportTXT(txtFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotted_frot_dx',
          mode='add')

CurveVariation2D['F_ROT_VS_DX'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotted_frot_dx',
            mode='add')

CurveVariation2D['F_ROT_VS_DY'].exportExcel(xlsFile='asdasda',
            mode='add')

saveProject()

closeProject()

exit()
