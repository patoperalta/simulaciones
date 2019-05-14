#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/8_icems_journal_2018_3d/00_main.py')

closeModelerContext()

deleteMesh()

ParameterGeom['DX_MULT'].expression='1'


ParameterGeom['R_ROT_OUT'].expression='15'


ParameterGeom['R_ROT_OUT'].expression='10'


ParameterGeom['DX'].expression='DX_MULT*R_ROT_OUT/15'


ParameterGeom['R_ROT_OUT'].expression='15'


ParameterGeom['R_ROT_OUT'].expression='20'


ParameterGeom['DX_MULT'].expression='0'


ParameterGeom['DX'].expression='DX_MULT*R_ROT_OUT/12'


ParameterGeom['DX_MULT'].expression='1'


ParameterGeom['R_ROT_OUT'].expression='15'


ParameterGeom['R_ROT_OUT'].expression='10'


closeProject()

exit()
