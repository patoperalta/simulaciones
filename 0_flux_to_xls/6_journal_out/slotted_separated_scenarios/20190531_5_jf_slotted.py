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
r_mot=[20]
# r_mot=[20]

# to be able to export values of integral
import sys

#info about the motor and its revision and blahblah
rev='1'
mot='slotted'
dir='mot_'+mot+'/' ##create this folder manually	
								  
## 7 JF_RMS
### insert and adjust headers
category = 'JF_RMS'
exp = 'IF_HAT;A_CU;P_CU_TOT;F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;L_SLOT;R_ROT_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_7_JF_rev'+rev+'_R'+str(r_mot[0])+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')
	
## auxiliary category
## in this case, JF
cat=[8]

##now start cycling scenarios
n=300 ##counter for value extraction
for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(l_slot)):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
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
			
					if (alpha[i]==2 and beta[j]==0.1 and r_mot[l]==20 and l_slot[k]==11) or (alpha[i]==1.6 and beta[j]==0.2 and r_mot[l]==20 and l_slot[k]==13) or (alpha[i]==1.8 and beta[j]==0.2 and r_mot[l]==20 and l_slot[k]==13):
						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(l_slot[k])+';'+str(r_mot[l])+';'+str(cat[m])
						values_f_rot='-1'+';'+'-1'+';'+'-1' #as string
						values_f_st=values_f_rot
						line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
						f.write(line)					
					else:
						##switch scenario
						selectCurrentStep(activeScenario=Scenario['7_JF_R'+str(r_mot[l])],
									parameterValue=['ALPHA_H='+str(alpha[i]),
													'BETA='+str(beta[j]),
													'L_SLOT='+str(l_slot[k]),					
													'D_ST='+str(d_st),
													'W_SLOT='+str(w_slot),
													'R_ROT_OUT='+str(r_mot[l]),
													# 'JF_RMS='+str(cat[m])])	
													'JF_RMS='+str(cat[m])])	

						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(l_slot[k])+';'+str(r_mot[l])+';'+str(cat[m]) ##scenario info
						
						result = VariationParameterFormula['IF_HAT'].createResultCurrentValue(result='IF_HAT_'+str(n)) ##extract copper area
						value_if_hat = str(result[0].value)								

						result = VariationParameterFormula['A_CU'].createResultCurrentValue(result='ACU_JF_'+str(n)) ##extract copper area
						value_acu = str(result[0].value)
						
						##extract copper losses
						result = VariationParameterFormula['P_CU_TOT'].createResultCurrentValue(result='PCUTOT_JF_'+str(n))
						value_pcu = str(result[0].value)
														
						##f_rot
						result = predefine['F_ROT'].createResultCurrentValue(result='FROT_JF_'+str(n)) #extract
						values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
						
						##f_st
						result = predefine['F_ST'].createResultCurrentValue(result='FST_JF_'+str(n)) #extract
						values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string						
						
						##line
						line=values_scn+';'+value_if_hat+';'+value_acu+';'+value_pcu+';'+values_f_rot+';'+values_f_st+'\n'
						
						##write
						f.write(line)
						n=n+1	#counter
f.close()
n		