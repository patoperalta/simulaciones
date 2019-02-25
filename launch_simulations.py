########################
								 
meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()		

filename='C:/Users/jperalta/Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_with_hole_v2/sims/20181116_prot_revB.FLU'

# Scenario['00_FIELDS'].solve(projectName=filename)

Scenario['01_DX'].solve(projectName=filename)

Scenario['02_DY'].solve(projectName=filename)

Scenario['03_DZ'].solve(projectName=filename)

Scenario['04_DALPHA'].solve(projectName=filename)

Scenario['05_DBETA'].solve(projectName=filename)

Scenario['06_JTORQUE'].solve(projectName=filename)

Scenario['07_JFORCE'].solve(projectName=filename)

Scenario['08_DISP0_ANGLE'].solve(projectName=filename)

Scenario['09_DISP0_ANGLE_JT'].solve(projectName=filename)

# Scenario['10_DISP0_ANGLE_JF'].solve(projectName=filename)

Scenario['11_DISP_ANGLE'].solve(projectName=filename)

# Scenario['12_DISP_ANGLE_JT'].solve(projectName=filename)

# Scenario['13_DISP_ANGLE_JF'].solve(projectName=filename)


# Scenario['2_DALPHA'].solve(projectName=filename)

# Scenario['3_DBETA'].solve(projectName=filename)

# Scenario['4_DX'].solve(projectName=filename)

# Scenario['5_DY'].solve(projectName=filename)

# Scenario['6_JT'].solve(projectName=filename)

# Scenario['7_JF'].solve(projectName=filename)

# Scenario['2_DALPHA'].continueToSolve(projectName=filename,
                                 # option='IterateOnNonConvergentSteps')

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