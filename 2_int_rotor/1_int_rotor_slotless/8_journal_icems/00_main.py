#! Flux3D 18.1
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

## start scripting

executeBatchSpy('1_param_revH.py')               		# Defines different parameters
time_params = time.time() - t

executeBatchSpy('2_app_def.py')               			# Defines different parameters
time_app_def= time.time() - t

executeBatchSpy('3_mesh_info.py')               		# Defines different parameters
time_mesh = time.time() - t

executeBatchSpy('4_geom_revD_circular.py')              # Defines different parameters
time_geometry = time.time() - t

executeBatchSpy('5_mat_def.py')               			# Defines different parameters
time_materials = time.time() - t

executeBatchSpy('6_elec_circuit_toroidal_revG.py')      # Defines different parameters
time_toroidal_coils = time.time() - t

executeBatchSpy('7_assign_circular.py')      			# Defines different parameters
time_assign = time.time() - t

executeBatchSpy('8_sensors.py')           	    		# Defines different parameters
time_sensors = time.time() - t

executeBatchSpy('9_make_scenarios_passive_revC.py')    	# Defines different parameters
time_scenarios_p = time.time() - t

executeBatchSpy('10_make_scenarios_active_revC.py')    	# Defines different parameters
time_scenarios_a = time.time() - t

t = time.time()

meshDomain()

generateSecondOrderElements()

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

total_time = time_params+time_app_def+time_mesh+time_geometry+time_materials+time_toroidal_coils+time_assign+time_sensors+time_scenarios_p+time_scenarios_a

print("\n")
print("Time for initialisation:        "+print_time_hms(time_initialisation))
print("Time for building the geometry: "+print_time_hms(time_geometry))
print("Time for building the mesh:     "+print_time_hms(time_mesh))
print("Time for physics:               "+print_time_hms(time_materials))
print("Time for solving:               "+print_time_hms(time_solving))
print("\n")
print("Total time:                     "+print_time_hms(total_time))