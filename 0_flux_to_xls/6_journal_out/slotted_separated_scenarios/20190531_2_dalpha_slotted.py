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
r_mot=[10,15,20]
# r_mot=[20]

#info about the motor and its revision and blahblah
rev='1'
mot='slotted'
dir='mot_'+mot+'/' ##create this folder manually	
		
j=8	
## 6 JT
for l in range(0,len(r_mot)):
	##size of the airgap... we  have to transform it afterwards
	if r_mot[l]==10:
		d_st=8
		w_slot=7
		l_0=7
	elif r_mot[l]==15:
		d_st=13
		w_slot=12
		l_0=9
	elif r_mot[l]==20:
		d_st=18
		w_slot=16
		l_0=11

	dx=1	#diff
	N=4		#length
	l_slot=[None]*N 	#initialize size
	l_slot[0]=l_0		#first value
	for z in range(N-1):
		l_slot[z+1]=round(l_slot[z]+dx,1)		

	selectCurrentStep(activeScenario=Scenario['2_DALPHA_R'+str(r_mot[l])],
				parameterValue=['ALPHA_H='+str(alpha[0]),
								'BETA='+str(beta[0]),
								'DALPHA_MULT=1',
								# 'DTHETA=90',
								'L_SLOT='+str(l_0),
								'R_ROT_OUT='+str(r_mot[0]),
								'D_ST='+str(d_st),
								'W_SLOT='+str(w_slot)])
								# 'JF_RMS='+str(cat[m])])	
								# 'JT_RMS='+str(j)])	
							  
	CSVExportTable(parameter=[VariationParameter['R_ROT_OUT'],
							  VariationParameter['TX_ROT'],
							  VariationParameter['TX_ST'],
							  VariationParameter['TY_ROT'],
							  VariationParameter['TY_ST'],
							  VariationParameter['TZ_ROT'],
							  VariationParameter['TZ_ST']],
					evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['ALPHA_H'],
																				   limitMin=alpha[0],
																				   limitMax=alpha[-1]),
					SetParameterXVariable(paramEvol=VariationParameter['BETA'],
																				   limitMin=beta[0],
																				   limitMax=beta[-1]),
					SetParameterXVariable(paramEvol=VariationParameter['L_SLOT'],
																				   limitMin=l_slot[0],
																				   limitMax=l_slot[-1]),
					SetParameterFixed(paramEvol=VariationParameter['R_ROT_OUT'],
																			   currentValue=r_mot[l]),	
					SetParameterFixed(paramEvol=VariationParameter['DALPHA_MULT'],
																			   currentValue=1),
					# SetParameterFixed(paramEvol=VariationParameter['DTHETA'],
																			   # currentValue=90),
					SetParameterFixed(paramEvol=VariationParameter['W_SLOT'],
																			   currentValue=w_slot),
					SetParameterFixed(paramEvol=VariationParameter['D_ST'],
																			   currentValue=d_st)]),
					filename=dir+mot+'_2_DALPHA_rev'+rev+'_R_'+str(r_mot[l]))		   