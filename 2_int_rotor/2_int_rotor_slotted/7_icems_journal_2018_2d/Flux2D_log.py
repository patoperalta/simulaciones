#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

# C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotted_2d_r10.FLU

Scenario['3_JTORQUE'].solve(projectName='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190513_slotted_2d_r20.FLU')

EvolutiveCurve2D(name='TZ_ROT_vs_JT',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])


Scenario['1_DX'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190513_slotted_2d_r20.FLU')

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190513_slotted_2d_r20.FLU')

Scenario['4_JFORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190513_slotted_2d_r20.FLU')

CurveVariation2D['TZ_ROT_VS_JT'].delete()
saveProjectAs('../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190513_slotted_2d_r20.FLU')

selectCurrentStep(activeScenario=Scenario['1_DX'],
                  parameterValue=['DX=0.1'])

EvolutiveCurve2D(name='F_ROT_VS_DX',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DX'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

CurveVariation2D['F_ROT_VS_DX'].exportExcel(xlsFile='slotted_2d_frot_dx',
            mode='replace')

selectCurrentStep(activeScenario=Scenario['2_DY'],
                  parameterValue=['DY=0.1'])

saveProject()

closeProject()

exit()
