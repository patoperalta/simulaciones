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

# to be able to export values of integral
import sys

#info about the motor and its revision and blahblah
rev='1'
mot='slotless'
dir='mot_'+mot+'/' ##create this folder manually	

## 4 DX
	
## auxiliary category
cat=[1]
	
### insert and adjust headers
category = 'DX'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ROT_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_4_DX_rev'+rev+'_R_'+str(r_mot[0])+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')	
n=0 ##counter for value extraction

for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(d_gap)):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
					##size of the airgap... we  have to transform it afterwards
					if r_mot[l]==10:
						d_st=6
					elif r_mot[l]==15:
						d_st=11
					elif r_mot[l]==20:
						d_st=17
						
					##switch scenario
					selectCurrentStep(activeScenario=Scenario['4_DX_R'+str(r_mot[l])],
								parameterValue=['ALPHA_H='+str(alpha[i]),
												'BETA='+str(beta[j]),
												'DX_MULT='+str(cat[m]),
												'D_AGAP='+str(d_gap[k]),
												'D_ST='+str(d_st),
												'R_ROT_OUT='+str(r_mot[l])])

					##scenario info
					values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])
					
					##f_rot
					result = predefine['F_ROT'].createResultCurrentValue(result='F_ROT_DX_'+str(n)) #extract
					n=n+1	#counter
					values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
					
					##f_st
					result = predefine['F_ST'].createResultCurrentValue(result='F_ST_DX_'+str(n)) #extract
					n=n+1	#counter
					values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string						
					
					##line
					line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
					
					##write
					f.write(line)

f.close()
n			