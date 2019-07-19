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
# x0=10.0	#init
# dx=5	#diff
# N=2	#length
# r_mot=[None]*N 	#initialize size
# r_mot[0]=x0		#first value
# for i in range(N-1):	
	# r_mot[i+1]=round(r_mot[i]+dx,2)	
##without points or commas...
r_mot=[10,15]
r_mot=[20]

# to be able to export values of integral
import sys

#info about the motor and its revision and blahblah
rev='1'
mot='slotless'
dir='mot_'+mot+'/' ##create this folder manually	

##example	
for l in range(0,len(r_mot)):
	for k in range(0,len(d_gap)):
		for j in range(0,len(beta)):
			for i in range(0,len(alpha)):
				print('now...')
				print('r_mot='+str(r_mot[l]))				
				print('alpha='+str(alpha[i]))
				print('beta='+str(beta[j]))
				print('d_gap='+str(d_gap[k]))

				##size of the airgap... we  have to transform it afterwards
				if r_mot[l]==10:
					d_st=6
				elif r_mot[l]==15:
					d_st=11
				elif r_mot[l]==20:
					d_st=17
					
				aux='_alpha'+str(alpha[i])+'_beta_'+str(beta[j])+'_dgap_'+str(d_gap[k]*10)+'_rmot_'+str(r_mot[l])
				aux=aux.replace('.', '')
			
				#select scenario
				selectCurrentStep(activeScenario=Scenario['0_FIELD_R'+str(r_mot[l])],
					parameterValue=['ALPHA_H='+str(alpha[i]),
									'BETA='+str(beta[j]),
									'D_AGAP='+str(d_gap[k]),
									'D_ST='+str(d_st),									
									'R_ROT_OUT='+str(r_mot[l])])
	
				SpatialCurve(name='perimeter'+aux,
						compoundPath=CompoundPath['FE_PER'],
						formula=['Comp(1,B)',
								 'Comp(2,B)',
								 'Comp(3,B)'])

				CurveSpatial2D['perimeter'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/perimeter'+aux,
						mode='add')
			
				SpatialCurve(name='h'+aux,
						compoundPath=CompoundPath['FE_HEIGHT'],
						formula=['ModV(B)'])

				CurveSpatial2D['h'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/h'+aux,
						mode='add')
				
			#not really needed anymore
				SpatialCurve(name='b_airgap'+aux,
						compoundPath=CompoundPath['AIRGAP_PERIMETER'],
						formula=['Comp(1,B)',
								'Comp(2,B)',
								'Comp(3,B)'])

				CurveSpatial2D['b_airgap'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/b_airgap'+aux,
						mode='add')						