#! Flux3D 12.0
import math
import time

#from Definitions_and_functions import *
def print_time_hms( time_sec ):
     "This prints time_sec in hour-min-sec format"
     if(time_sec >= 60.0 and time_sec < 3600.0):
          total_time_minutes = int(math.floor(time_sec/60.0))
          total_time_secondes = int(round(60*(time_sec/60.0-total_time_minutes)))
          return str(total_time_minutes)+" min "+str(total_time_secondes)+" sec \n"
     elif(time_sec >= 3600.0):
          total_time_hours = time_sec/3600.0
          total_time_minutes = 60*(total_time_hours-math.floor(total_time_hours))
          total_time_secondes = 60*(total_time_minutes-math.floor(total_time_minutes))
          return str(int(total_time_hours))+" h "+str(int(total_time_minutes))+" min "+str(int(total_time_secondes))+" sec \n"
     else:
          return "%0.1f s \n" % time_sec



t = time.time()

newProject()

executeBatchSpy('1_param_revJ.py')               		# Defines different parameters
time_params = time.time() - t

executeBatchSpy('2_app_def.py')               			# Defines different parameters
time_app_def= time.time() - t

executeBatchSpy('3_mesh_info.py')               		# Defines different parameters
time_mesh = time.time() - t

executeBatchSpy('4_geom_revI.py')              			# Defines different parameters
# executeBatchSpy('4_geom_revI_circular.py')				# Defines different parameters
time_geometry = time.time() - t

executeBatchSpy('5_mat_def.py')               			# Defines different parameters
time_materials = time.time() - t

executeBatchSpy('6a_elec_circuit_saddle_wdg_drive_revB.py')      # Defines different parameters
time_electric_circuit = time.time() - t

executeBatchSpy('6b_bearing_coil_toroidal_revE.py')      # Defines different parameters
time_electric_circuit = time.time() - t

executeBatchSpy('6c_other_outputs_revB.py')      		# Defines different parameters
time_electric_circuit = time.time() - t

executeBatchSpy('7_assign_revF.py')           	    	# Defines different parameters
time_assign = time.time() - t

# executeBatchSpy('7b_radial_homopolar_bng.py')			# Defines different parameters
# time_assign = time.time() - t

executeBatchSpy('8_sensors_revE.py')               			# Defines different parameters
time_sensors = time.time() - t

executeBatchSpy('9_make_scenarios_passive_revD.py')      # Defines different parameters
time_scenarios = time.time() - t

executeBatchSpy('10_make_scenarios_active_revD.py')         # Defines different parameters
time_scenarios_sensors = time.time() - t

executeBatchSpy('11_mag_circ_mesh.py')         # Defines different parameters
time_scenarios_sensors = time.time() - t

t = time.time()
#saveProjectAs(project_path+project_name)
if(solving):
	saveProjectAs(project_path+project_name)
     # SCENARII
	#executeBatchSpy('Reference_values.py')          # Execute a reference values scenario
	#executeBatchSpy('Rotor_rotation.py')          # Execute a rotor rotation scenario
     #executeBatchSpy('PM_magnetisation_rotation.py')          # Execute a PM magnetisation rotation scenario
     # POSTPROCESSING
     #executeBatchSpy('Coil_fluxes.py')             # Computation of the coil fluxes
     #executeBatchSpy('EM_torque.py')               # Computation of the electromagetic
	#executeBatchSpy('Cut_plans_induction.py')          # Display of induction cut plans

time_solving = time.time() - t



total_time = time_params+time_app_def+time_mesh+time_geometry+time_materials+time_electric_circuit+time_assign+time_sensors+time_scenarios_sensors

print("\n")
print("Time for initialisation:        "+print_time_hms(time_initialisation))
print("Time for building the geometry: "+print_time_hms(time_geometry))
print("Time for building the mesh:     "+print_time_hms(time_mesh))
print("Time for physics:               "+print_time_hms(time_materials))
print("Time for solving:               "+print_time_hms(time_solving))
print("\n")
print("Total time:                     "+print_time_hms(total_time))

# newProject()
# print("FICHIER MAIN.PY\n")

# # proj_name = ['C:\Users\jperalta\Desktop\08_flux_ext_rotor\3_ext_rotor_script\20170919_ext_rotor_rev_J\projects']
# proj_name = ['C:\flux_solving']


# step=[100]


# freq=[50000.0]
# depth=[10.0]
# niter=[100]
# alpha=[0.018699956271368]


# # scenario
# # scenario = 0 reference values
# # scenario = 1 tension induite
# #for plot
# scen1_min=[0.0]
# scen1_max=[1.0]
# scen1_step=[1.0]

# #

# scenario=[1]

# magnet_angle=[0.0]



# measval=[3]


# # USING BATCH MODE
# matlab=[0]

# AC=[0]

# # if matlab[0]==0:
	# # executeBatchSpy('param.py')			# define different parameters
	# # executeBatchSpy('app_def.py')		# define the application definition
	# # executeBatchSpy('mesh_info.py')		# contains the information for the mesh
	# # executeBatchSpy('geom.py')			# define the geometry
	# # # # # executeBatchSpy('elec_circuit.py')	# define the electic circuit
	# # executeBatchSpy('mat_def.py')		# the material
	# # executeBatchSpy('assign_faces.py')	# assign the material
	# # executeBatchSpy('make_scenarios.py')
	# # meshDomain()
	# # #executeBatchSpy('fauhlaber_winding.py')	
	# # executeBatchSpy('solve.py')
	# # # executeBatchSpy('curve.py')

