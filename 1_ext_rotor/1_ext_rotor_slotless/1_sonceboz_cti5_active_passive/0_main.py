#! Flux3D 12.0



newProject()
print("FICHIER MAIN.PY\n")

# proj_name = ['C:\Users\jperalta\Desktop\08_flux_ext_rotor\3_ext_rotor_script\20170919_ext_rotor_rev_J\projects']
proj_name = ['C:\flux_solving']


step=[100]


freq=[50000.0]
depth=[10.0]
niter=[100]
alpha=[0.018699956271368]


# scenario
# scenario = 0 reference values
# scenario = 1 tension induite
#for plot
scen1_min=[0.0]
scen1_max=[1.0]
scen1_step=[1.0]

#

scenario=[1]

magnet_angle=[0.0]



measval=[3]


# USING BATCH MODE
matlab=[0]

AC=[0]

# if matlab[0]==0:
	# executeBatchSpy('param.py')			# define different parameters
	# executeBatchSpy('app_def.py')		# define the application definition
	# executeBatchSpy('mesh_info.py')		# contains the information for the mesh
	# executeBatchSpy('geom.py')			# define the geometry
	# # # # executeBatchSpy('elec_circuit.py')	# define the electic circuit
	# executeBatchSpy('mat_def.py')		# the material
	# executeBatchSpy('assign_faces.py')	# assign the material
	# executeBatchSpy('make_scenarios.py')
	# meshDomain()
	# #executeBatchSpy('fauhlaber_winding.py')	
	# executeBatchSpy('solve.py')
	# # executeBatchSpy('curve.py')

