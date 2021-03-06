#! Flux2D 18.1
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

## things of 2D initialization
SketcherOption[1].magnetizationGrid=MagnetizationGrid(gridActivation='OUI',lengthGridCell=10.0,cellSubdivision=10,subdivisionPoint=10)

openSketcher2dContext()

closeSketcher2dContext()

## start scripting

executeBatchSpy('1_param_2d_revF.py')               		# Defines different parameters
time_params = time.time() - t

executeBatchSpy('2_app_def.py')               			# Defines different parameters
time_app_def= time.time() - t

executeBatchSpy('3_mesh_info.py')               		# Defines different parameters
time_mesh = time.time() - t

executeBatchSpy('4_geom_2d_revF.py')              		# Defines different parameters
time_geometry = time.time() - t

executeBatchSpy('5_mat_def.py')               			# Defines different parameters
time_materials = time.time() - t

executeBatchSpy('6_assign_mats_and_coils_revA.py')      # Defines different parameters
time_electric_circuit_assign = time.time() - t

executeBatchSpy('7_sensors.py')           	    		# Defines different parameters
time_sensors = time.time() - t

executeBatchSpy('8_scenarios_test.py')               	# Defines different parameters
time_scenarios = time.time() - t

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

total_time = time_params+time_app_def+time_mesh+time_geometry+time_materials+time_electric_circuit_assign+time_scenarios

print("\n")
print("Time for initialisation:        "+print_time_hms(time_initialisation))
print("Time for building the geometry: "+print_time_hms(time_geometry))
print("Time for building the mesh:     "+print_time_hms(time_mesh))
print("Time for physics:               "+print_time_hms(time_materials))
print("Time for solving:               "+print_time_hms(time_solving))
print("\n")
print("Total time:                     "+print_time_hms(total_time))