# loadProject('D:/pato_peralta/1_flux_simulations/6_journal/20190517_slotted_rev1.FLU')
# loadProject('D:/pato_peralta/1_flux_simulations/6_journal/20190517_slotless_rev1.FLU')
# executeBatchSpy('C:/Users/jperalta/Desktop/20190520_slotless_rev1.FLU')
# for i in range(10, 20+1, 5):
	# Scenario['0_FIELD_R'+str(i)].solve(projectName=filename)
	# Scenario['1_DZ_R'+str(i)].solve(projectName=filename)
	# Scenario['2_DALPHA_R'+str(i)].solve(projectName=filename)
	# Scenario['3_DBETA_R'+str(i)].solve(projectName=filename)
	# Scenario['4_DX_R'+str(i)].solve(projectName=filename)
	# Scenario['5_DY_R'+str(i)].solve(projectName=filename)
	# Scenario['6_JT_R'+str(i)].solve(projectName=filename)	
	# Scenario['7_JF_R'+str(i)].solve(projectName=filename)	
# loadProject('D:/pato_peralta/1_flux_simulations/6_journal/20190521_slotted_rev1.FLU')


# filename='C:/Users/jperalta/Desktop/03_flux_int_rotor_slotless/10_icems_3d/20190521_slotless_rev1'	
# filename='D:/pato_peralta/1_flux_simulations/6_journal/20190521_slotted_rev1'		
# for i in [10,15]:
	# print('R='+str(i))
	# print('0_FIELD_R'+str(i))
	# Scenario['0_FIELD_R'+str(i)].solve(projectName=filename+'.FLU')
	# print('1_DZ_R'+str(i))
	# Scenario['1_DZ_R'+str(i)].solve(projectName=filename+'.FLU')
	# print('2_DALPHA_R'+str(i))
	# Scenario['2_DALPHA_R'+str(i)].solve(projectName=filename+'.FLU')
	# print('3_DBETA_R'+str(i))
	# Scenario['3_DBETA_R'+str(i)].solve(projectName=filename+'.FLU')
	# print('4_DX_R'+str(i))
	# Scenario['4_DX_R'+str(i)].solve(projectName=filename+'.FLU')
	# print('5_DY_R'+str(i))
	# Scenario['5_DY_R'+str(i)].solve(projectName=filename+'.FLU')
	# print('6_JT_R'+str(i))
	# Scenario['6_JT_R'+str(i)].solve(projectName=filename+'.FLU')	
	# print('7_JF_R'+str(i))
	# Scenario['7_JF_R'+str(i)].solve(projectName=filename+'.FLU')		
	# filename=filename+'_R'+str(i)
	# saveProjectAs(filename+'.FLU')
	

#filename='D:/pato_peralta/1_flux_simulations/6_journal/2_less_constraint_mesh/20190531_slotted_rev2'
filename='D:/pato_peralta/1_flux_simulations/6_journal/2_less_constraint_mesh/20190531_slotted_rev2_R20_2'

for i in [20]:
	print('R='+str(i))
	
	# print('0_FIELD_R'+str(i))	
	
	# if i==15:
		# Scenario['0_FIELD_R'+str(i)].solve(projectName=filename+'.FLU')	
	# else:
		# Scenario['0_FIELD_R'+str(i)].continueToSolve(projectName=filename+'.FLU',
												# option='IterateOnNonConvergentSteps')	
	
	# print('2_DALPHA_R'+str(i))											
	# if i==20:
		# Scenario['2_DALPHA_R'+str(i)].continueToSolve(projectName=filename+'.FLU',
												# option='IterateOnNonConvergentSteps')											
	# else:
		# Scenario['2_DALPHA_R'+str(i)].solve(projectName=filename+'.FLU')		
	
	# print('1_DZ_R'+str(i))
	# Scenario['1_DZ_R'+str(i)].solve(projectName=filename+'.FLU')
	
	print('3_DBETA_R'+str(i))
	Scenario['3_DBETA_R'+str(i)].solve(projectName=filename+'.FLU')
	print('4_DX_R'+str(i))
	Scenario['4_DX_R'+str(i)].solve(projectName=filename+'.FLU')
	print('5_DY_R'+str(i))
	Scenario['5_DY_R'+str(i)].solve(projectName=filename+'.FLU')
	print('6_JT_R'+str(i))
	Scenario['6_JT_R'+str(i)].solve(projectName=filename+'.FLU')	
	print('7_JF_R'+str(i))
	Scenario['7_JF_R'+str(i)].solve(projectName=filename+'.FLU')		
	print('8_DALPHA2_R'+str(i))
	Scenario['8_DALPHA2_R'+str(i)].solve(projectName=filename+'.FLU')			
	print('9_DBETA2_R'+str(i))
	Scenario['9_DBETA2_R'+str(i)].solve(projectName=filename+'.FLU')