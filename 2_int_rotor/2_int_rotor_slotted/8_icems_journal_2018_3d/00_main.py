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
## start scripting

executeBatchSpy('1_param_revG.py')               		# Defines different parameters

executeBatchSpy('2_app_def.py')               			# Defines different parameters

executeBatchSpy('3_mesh_info.py')               		# Defines different parameters

executeBatchSpy('4_geom_revE.py')              			# Defines different parameters

executeBatchSpy('5_mat_def.py')               			# Defines different parameters

executeBatchSpy('6_coils_concentric_revF.py')      		# Defines different parameters

executeBatchSpy('7_assign_revB.py')      				# Defines different parameters

executeBatchSpy('8_sensors.py')      					# Defines different parameters

## create scenarios
## common parameters
# alpha_min = 1.0
# alpha_max = 2
# d_alpha= 0.2
 
# beta_min = 0.1
# beta_max = 0.3
# d_beta= 0.1

# j=8
## specific for motor size
# r_rot=10
# wslot=7
# dst=8

# lslot_min = 7
# lslot_max = 10 
# lslot_dgap= 1
# executeBatchSpy('9_scenarios_slotted.py')      			# Defines different parameters

## specific for motor size
# r_rot=15
# wslot=12
# dst=13

# lslot_min = 9
# lslot_max = 12 
# lslot_dgap= 1
# executeBatchSpy('9_scenarios_slotted.py')      			# Defines different parameters

## specific for motor size
# r_rot=20
# wslot=16
# dst=18

# lslot_min = 11
# lslot_max = 14 
# lslot_dgap= 1
# executeBatchSpy('9_scenarios_slotted.py')      			# Defines different parameters
##end

t = time.time()

meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()

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

# total_time = time_params+time_app_def+time_mesh+time_geometry+time_materials+time_electric_circuit_assign+time_scenarios

print("\n")
print("Time for initialisation:        "+print_time_hms(time_initialisation))
print("Time for building the geometry: "+print_time_hms(time_geometry))
print("Time for building the mesh:     "+print_time_hms(time_mesh))
print("Time for physics:               "+print_time_hms(time_materials))
print("Time for solving:               "+print_time_hms(time_solving))
print("\n")
print("Total time:                     "+print_time_hms(total_time))