#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/8_icems_journal_2018_3d/00_main.py')

saveProjectAs('../../../../../../Desktop/03_flux_int_rotor_slotless/10_icems_3d/20190521_slotless_rev1_r20.FLU')

filename='C:/Users/jperalta/Desktop/03_flux_int_rotor_slotless/10_icems_3d/20190521_slotless_rev1_r20'     
for i in [20]:
     print('R='+str(i))
     # print('0_FIELD_R'+str(i))
     # Scenario['0_FIELD_R'+str(i)].solve(projectName=filename+'.FLU')
     # print('1_DZ_R'+str(i))
     # Scenario['1_DZ_R'+str(i)].solve(projectName=filename+'.FLU')
     # print('2_DALPHA_R'+str(i))
     # Scenario['2_DALPHA_R'+str(i)].solve(projectName=filename+'.FLU')
     # print('3_DBETA_R'+str(i))
     # Scenario['3_DBETA_R'+str(i)].solve(projectName=filename+'.FLU')
     print('4_DX_R'+str(i))
     Scenario['4_DX_R'+str(i)].solve(projectName=filename+'.FLU')
     print('5_DY_R'+str(i))
     Scenario['5_DY_R'+str(i)].solve(projectName=filename+'.FLU')
     print('6_JT_R'+str(i))
     Scenario['6_JT_R'+str(i)].solve(projectName=filename+'.FLU')     
     print('7_JF_R'+str(i))
     Scenario['7_JF_R'+str(i)].solve(projectName=filename+'.FLU')     

saveProject()

closeProject()

exit()
