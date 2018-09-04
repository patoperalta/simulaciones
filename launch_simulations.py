########################
								 
meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()							 

filename='D:/pato_peralta/1_flux_simulations/3_hall_sensors/20180810_int_rotor_slotless_green_variant_hall_sensors.FLU'

# Scenario['0_FIELD'].solve(projectName=filename)

# Scenario['1_DZ'].solve(projectName=filename)

# Scenario['2_DALPHA'].continueToSolve(projectName=filename,
                                 # option='IterateOnNonConvergentSteps')

# Scenario['2_DALPHA'].solve(projectName=filename)

# Scenario['3_DBETA'].solve(projectName=filename)

# Scenario['4_DX'].solve(projectName=filename)

# Scenario['5_DY'].solve(projectName=filename)

# Scenario['6_JT'].solve(projectName=filename)

# Scenario['7_JF'].solve(projectName=filename)

# Scenario['2_DALPHA_3'].solve(projectName=filename)

# Scenario['3_DBETA_3'].solve(projectName=filename)

#############

# Scenario['DISP_0_ANGLE_JF'].solve(projectName=filename)

# Scenario['DISP_0_ANGLE_JT'].solve(projectName=filename)

# Scenario['DISP_ANGLE_JF'].solve(projectName=filename)

# Scenario['DISP_ANGLE_JT'].solve(projectName=filename)

# Scenario['ANG_GREEN'].solve(projectName=filename)

# Scenario['ANG_VIOLET'].solve(projectName=filename)

#############

# Scenario['DISP_ANGLE'].solve(projectName=filename)

# Scenario['DISP_ANGLE_JT'].solve(projectName=filename)

# Scenario['DISP_ANGLE_JF'].solve(projectName=filename)

# Scenario['DISP_0_ANGLE'].solve(projectName=filename)

Scenario['DISP_0_ANGLE_JT'].solve(projectName=filename)

Scenario['DISP_0_ANGLE_JF'].solve(projectName=filename)