#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/8_icems_journal_2018_3d/00_main.py')

saveProjectAs('../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190517_slotted_rev1.FLU')

Scenario['0_FIELD_R10'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190517_slotted_rev1.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

closeProject()

exit()
