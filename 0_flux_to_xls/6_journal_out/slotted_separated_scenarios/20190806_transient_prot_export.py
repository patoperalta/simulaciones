#06.08.2019 used to export transient losses in rotor
#design space definition
## alpha export
x0=1.6
dx=0.2
N=2
alpha=[None]*N
alpha[0]=x0
for i in range(N-1):
	alpha[i+1]=round(alpha[i]+dx,2)

## beta export
x0=0.3
dx=0.1
N=1
beta=[None]*N
beta[0]=x0
for i in range(N-1):
	beta[i+1]=round(beta[i]+dx,2)
	
## rrot
r_rot=20
##percentage of full speed in string,  10  --> 100%, so 02 is 20 %
speed='02'
speed_n=0.2 	#well ok, just make both the same, 

#not sure anymore what is the point of cat
cat=[1]

for m in range(0,len(cat)):						#not really needed anymore
	for l in range(0,1):#the exportation is made for each radius (which is determined above), so this shouldn't scroll
		for k in range(0,1):	#only simulated one l_slot for each alpha,beta,rrot configuration, assuming the rest stays the same
			for j in range(0,len(beta)):		#this does scroll
				for i in range(0,len(alpha)):	#this scrolls also
					##original size of lslot and d_st
					if r_rot==10:
						d_st=8
						w_slot=7
						l_0=7
					elif r_rot==15:
						d_st=13
						w_slot=12
						l_0=9
					elif r_rot==20:
						d_st=18
						w_slot=16
						l_0=11
						
					#choose scenario
					selectCurrentStep(activeScenario=Scenario['PJ_ROT_'+str(r_rot)+'_N'+speed],
									  parameterValue=['ALPHA_H='+str(alpha[i]),
													  'BETA='+str(beta[j]),
													  'D_ST='+str(d_st),
													  'L_SLOT='+str(l_0),
													  'R_ROT_OUT='+str(r_rot),
													  'W_SLOT='+str(w_slot),
													  'N_PROP='+str(speed_n),
													  'ANGPOS_ROTOR=0.0']) #always start at angle 0
					
					#define name, remove dots, 
					aux = '_ALPHA_'+str(alpha[i])+'_BETA_'+str(beta[j])+'_RROT_'+str(r_rot)
					aux=aux.replace('.', '')
					
					#add names beginning 
					EvolutiveCurve2D(name='P_JOULE_ROT'+aux,
									 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['ALPHA_H'],
																								 currentValue=alpha[i]),
																			   SetParameterFixed(paramEvol=VariationParameter['BETA'],
																								 currentValue=beta[j]),
																			   SetParameterFixed(paramEvol=VariationParameter['D_ST'],
																								 currentValue=d_st),
																			   SetParameterFixed(paramEvol=VariationParameter['L_SLOT'],
																								 currentValue=l_0),
																			   SetParameterFixed(paramEvol=VariationParameter['R_ROT_OUT'],
																								 currentValue=r_rot),
																			   SetParameterFixed(paramEvol=VariationParameter['W_SLOT'],
																								 currentValue=w_slot),
																			   SetParameterFixed(paramEvol=VariationParameter['N_PROP'],
																								 currentValue=speed_n),
																			   SetParameterXVariable(paramEvol=VariationParameter['ANGPOS_ROTOR'],
																									 limitMin=0.0,
																									 limitMax=90.0)]),
									 formula=['P_JOULE_ROT'])
					
					#export excel
					CurveVariation2D['P_JOULE_ROT'+aux].exportExcel(xlsFile='results/p_harm_rot'+aux,
								mode='replace')