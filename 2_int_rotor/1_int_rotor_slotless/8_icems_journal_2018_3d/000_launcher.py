# loadProject('D:/pato_peralta/1_flux_simulations/6_journal/20190517_slotted_rev1.FLU')



filename='D:/pato_peralta/1_flux_simulations/6_journal/20190517_slotted_rev1.FLU'
for i in range(10, 20+1, 5):
	Scenario['0_FIELD_R'+str(i)].solve(projectName=filename)
	Scenario['1_DZ_R'+str(i)].solve(projectName=filename)
	Scenario['2_DALPHA_R'+str(i)].solve(projectName=filename)
	Scenario['3_DBETA_R'+str(i)].solve(projectName=filename)
	Scenario['4_DX_R'+str(i)].solve(projectName=filename)
	Scenario['5_DY_R'+str(i)].solve(projectName=filename)
	Scenario['6_JT_R'+str(i)].solve(projectName=filename)	
	Scenario['7_JF_R'+str(i)].solve(projectName=filename)		

