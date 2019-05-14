#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario['0_FIELDS'].solve(projectName='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190514_slotless_2d_r10')

Scenario['1_DX'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190514_slotless_2d_r10.FLU')

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190514_slotless_2d_r10.FLU')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190514_slotless_2d_r10.FLU')

Scenario['4_JFORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190514_slotless_2d_r10.FLU')

selectCurrentStep(activeScenario=Scenario['1_DX'],
                  parameterValue=['DX=0.1'])

EvolutiveCurve2D(name='F_ROT_vs_DX',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DX'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

selectCurrentStep(activeScenario=Scenario['2_DY'],
                  parameterValue=['DY=0.1'])

EvolutiveCurve2D(name='F_ROT_vs_Dy',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DY'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

selectCurrentStep(activeScenario=Scenario['3_JTORQUE'],
                  parameterValue=['JT_RMS=0.0'])

displayIsovalues()

displayIsovalues()

EvolutiveCurve2D(name='TZ_ROT_vs_JT',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

selectCurrentStep(activeScenario=Scenario['4_JFORCE'],
                  parameterValue=['JF_RMS=0.0'])

EvolutiveCurve2D(name='F_ROT_vs_JF',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JF_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['F_ROT'])

CurveVariation2D['F_ROT_VS_DX'].exportExcel(xlsFile='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/r10_results/slotless_2d_frot_dx',
            mode='replace')

CurveVariation2D['F_ROT_VS_DY'].exportExcel(xlsFile='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/r10_results/slotless_2d_frot_dy',
            mode='replace')

CurveVariation2D['F_ROT_VS_JF'].exportExcel(xlsFile='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/r10_results/slotless_2d_frot_jf',
            mode='replace')

CurveVariation2D['TZ_ROT_VS_JT'].exportExcel(xlsFile='C:/Users/jperalta/Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/r10_results/slotless_2d_tz_jt',
            mode='replace')



displayIsovalues()

saveProject()

closeProject()

exit()
