#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/7_icems_journal_2018_2d/00_main.py')

Scenario['1_DX'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotless_2d.FLU')

Scenario['2_DY'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotless_2d.FLU')

Scenario['3_JTORQUE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotless_2d.FLU')

Scenario['4_JFORCE'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/20190510_slotless_2d.FLU')

EvolutiveCurve2D(name='F_ROT_vs_JF',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JF_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['F_ROT'])

selectCurrentStep(activeScenario=Scenario['1_DX'],
                  parameterValue=['DX=0.1'])

EvolutiveCurve2D(name='F_ROT_vs_DX',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DX'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

selectCurrentStep(activeScenario=Scenario['2_DY'],
                  parameterValue=['DY=0.1'])

selectCurrentStep(activeScenario=Scenario['2_DY'],
                  parameterValue=['DY=1.0'])

EvolutiveCurve2D(name='F_ROT_vs_DY',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['DY'],
                                                                                 limitMin=0.1,
                                                                                 limitMax=1.0)]),
                 formula=['F_ROT'])

selectCurrentStep(activeScenario=Scenario['3_JTORQUE'],
                  parameterValue=['JT_RMS=0.0'])

EvolutiveCurve2D(name='TZ_ROT_vs_JT',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=25.0)]),
                 formula=['TZ_ROT'])

CurveVariation2D['F_ROT_VS_DX'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_frot_dx.xls',
            mode='add')

CurveVariation2D['F_ROT_VS_DY'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_frot_dy.xls',
            mode='add')

CurveVariation2D['F_ROT_VS_JF'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_frot_jf.xls',
            mode='add')

CurveVariation2D['F_ROT_VS_DX'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_frot_dx.xls',
            mode='replace')

CurveVariation2D['F_ROT_VS_DY'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_frot_dy.xls',
            mode='replace')

CurveVariation2D['F_ROT_VS_JF'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_frot_jf.xls',
            mode='replace')

CurveVariation2D['TZ_ROT_VS_JT'].exportExcel(xlsFile='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/slotless_2d_tz_jt.xls',
            mode='replace')

lastInstance = IsovalueSpatialGroup(name='ISOVAL_1',
                     formula='B',
                     forceVisibility='yes',
                     smoothValues='yes',
                     group=[Groupspatial['4_NO_INFINITE']])

PropIsovalues['ISOVAL_1'].group=[Groupspatial['2_NO_VACUUM']]


PropIsovalues['ISOVAL_1'].group=[Groupspatial['S_AIRGAP'],
                                 Groupspatial['S_COIL_PLUS_1'],
                                 Groupspatial['S_COIL_PLUS_2'],
                                 Groupspatial['S_COIL_PLUS_3'],
                                 Groupspatial['S_COIL_PLUS_4'],
                                 Groupspatial['S_COIL_PLUS_5'],
                                 Groupspatial['S_COIL_PLUS_6'],
                                 Groupspatial['S_PM'],
                                 Groupspatial['S_IRON_ST']]


closeProject()

exit()
