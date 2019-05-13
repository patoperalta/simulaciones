#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

deleteMesh()

ParameterGeom['DY'].expression='1'


ParameterGeom['DY'].expression='0'


ParameterGeom['DX'].expression='1'


ParameterGeom['DTHETA'].expression='90'


closeProject()

exit()
