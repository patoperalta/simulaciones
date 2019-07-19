#design space definition
## alpha export
x0=1.0
dx=0.2
N=6
alpha=[None]*N
alpha[0]=x0
for i in range(N-1):
	alpha[i+1]=round(alpha[i]+dx,2)

## beta export
x0=0.1
dx=0.1
N=3
beta=[None]*N
beta[0]=x0
for i in range(N-1):
	beta[i+1]=round(beta[i]+dx,2)

## dgap
x0=3.0	#init
dx=1	#diff
N=4		#length
d_gap=[None]*N 	#initialize size
d_gap[0]=x0		#first value
for i in range(N-1):	
	d_gap[i+1]=round(d_gap[i]+dx,2)	
	
## rmot
r_mot=[10,15]
r_mot=[20]

#info about the motor and its revision and blahblah
rev='1'
mot='slotless'
dir='mot_'+mot+'/' ##create this folder manually	
		
j=8	
## 6 JT
for l in range(0,len(r_mot)):
	##size of the airgap... we  have to transform it afterwards
	if r_mot[l]==10:
		d_st=6
	elif r_mot[l]==15:
		d_st=11
	elif r_mot[l]==20:
		d_st=17
	selectCurrentStep(activeScenario=Scenario['6_JT_R'+str(r_mot[l])],
					  parameterValue=['ALPHA_H='+str(alpha[0]),
									  'BETA='+str(beta[0]),
									  'D_ST='+str(d_st),
									  'D_AGAP='+str(d_gap[0]),
									  'R_ROT_OUT='+str(r_mot[l]),
									  'JT_RMS='+str(j)])
									  
	CSVExportTable(parameter=[VariationParameter['R_ROT_PH'],
							  VariationParameter['JT_RMS'],
							  VariationParameter['R_ST_OUT_PH'],
							  VariationParameter['V_FE_ST'],
							  VariationParameter['V_PM'],
							  VariationParameter['V_CU'],
							  VariationParameter['IT_HAT'],
							  VariationParameter['P_CU_TOT'],
							  VariationParameter['A_CU'],
							  VariationParameter['TZ_ROT'],
							  VariationParameter['TZ_ST']],
				   evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['ALPHA_H'],
																				   limitMin=alpha[0],
																				   limitMax=alpha[-1]),
					SetParameterXVariable(paramEvol=VariationParameter['BETA'],
																				   limitMin=beta[0],
																				   limitMax=beta[-1]),
					SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
																				   limitMin=d_gap[0],
																				   limitMax=d_gap[-1]),
					SetParameterFixed(paramEvol=VariationParameter['R_ROT_OUT'],
																			   currentValue=r_mot[l]),	
					SetParameterFixed(paramEvol=VariationParameter['D_ST'],
																			   currentValue=d_st),		   
					SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
																			   currentValue=j)]),
				   filename=dir+mot+'_6_JT_rev'+rev+'_R_'+str(r_mot[l]))			   