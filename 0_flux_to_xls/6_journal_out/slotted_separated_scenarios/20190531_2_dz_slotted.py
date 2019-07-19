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

##without points or commas...
## rmot
r_mot=[15]
# r_mot=[20]

# to be able to export values of integral
import sys

#info about the motor and its revision and blahblah
rev='1'
mot='slotted'
dir='mot_'+mot+'/' ##create this folder manually	

## 1 DZ

### insert and adjust headers
category = 'DZ'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;L_SLOT;R_ROT_OUT;'+category+';'+exp

## auxiliary category	
cat=[1]

## open the file and
f = open(dir+mot+'_1_DZ_rev'+rev+'_R_'+str(r_mot[0])+'.csv','w')
# f = open(mot+'_1_DZ_rev'+rev+'_R_'+str(r_mot[0])+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')	
n=2600 ##counter for value extraction

for m in range(0,len(cat)):
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

		for k in range(0,4):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
					n=n+1
					if (alpha[i]==1.6 and beta[j]==0.2 and r_mot[l]==10 and l_slot[k]==8) or (alpha[i]==2 and beta[j]==0.1 and r_mot[l]==10  and l_slot[k]==8) or (alpha[i]==1.6 and beta[j]==0.2 and r_mot[l]==20 and l_slot[k]==13) or (alpha[i]==1.8 and beta[j]==0.2 and r_mot[l]==20 and l_slot[k]==13) or (alpha[i]==2 and beta[j]==0.2 and r_mot[l]==15 and l_slot[k]==9):
					# if (alpha[i]==1.6 and beta[j]==0.2 and l_slot[k]==7 and r_mot[l]==10):					
						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(l_slot[k])+';'+str(r_mot[l])+';'+str(cat[m])
						values_f_rot='-1'+';'+'-1'+';'+'-1' #as string
						values_f_st=values_f_rot
						line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
						f.write(line)
					else:
						##switch scenario
						selectCurrentStep(activeScenario=Scenario['1_DZ_R'+str(r_mot[l])],
									parameterValue=['ALPHA_H='+str(alpha[i]),
													'BETA='+str(beta[j]),
													'D_ST='+str(d_st),
													'W_SLOT='+str(w_slot),
													'DZ_MULT='+str(cat[m]),
													'L_SLOT='+str(l_slot[k]),
													'R_ROT_OUT='+str(r_mot[l])])

						##scenario info
						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(l_slot[k])+';'+str(r_mot[l])+';'+str(cat[m])
						
						##f_rot
						result = predefine['F_ROT'].createResultCurrentValue(result='F_ROT_DZ_'+str(n)) #extract
						n=n+1	#counter
						values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
						
						##f_st
						result = predefine['F_ST'].createResultCurrentValue(result='F_ST_DZ_'+str(n)) #extract
						n=n+1	#counter
						values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string						
						
						##line
						line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
						
						##write
						f.write(line)				
f.close()
n	