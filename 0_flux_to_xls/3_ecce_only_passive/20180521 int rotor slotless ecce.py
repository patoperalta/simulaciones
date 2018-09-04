## EXPORT INT ROTOR SLOTTED STATOR

#######################################################################################################################
#######################################################################################################################
#design space definition
## alpha export
x0=1
dx=0.2
N=6
alpha=[None]*N
alpha[0]=x0
for i in range(N-1):
	alpha[i+1]=round(alpha[i]+dx,2)

## beta export
x0=0.1
dx=0.1
N=10
beta=[None]*N
beta[0]=x0
for i in range(N-1):
	beta[i+1]=round(beta[i]+dx,2)

## dgap
x0=1.5	#init
dx=.5	#diff
N=1		#length
d_gap=[None]*N 	#initialize size
d_gap[0]=x0		#first value
for i in range(N-1):	
	d_gap[i+1]=round(d_gap[i]+dx,2)	
	
## rmot
x0=10	#init
dx=10	#diff
N=5	#length
r_mot=[None]*N 	#initialize size
r_mot[0]=x0		#first value
for i in range(N-1):	
	r_mot[i+1]=round(r_mot[i]+dx,2)	
#######################################################################################################################
#info about the motor and its revision and blahblah
rev='2' # 1 for constant airgap, 2 for proportional airgap
mot='2'
dir='mot'+mot+'/' ##create this folder manually	
#####################################################################################################################
# 0 DIMENSIONS
CSVExportTable(parameter=[VariationParameter['R_ROT_OUT_PH'],
                          VariationParameter['R_ROT_IN_PH'],
                          VariationParameter['R_ST_OUT'],
                          VariationParameter['R_ST_IN_PH'],
                          VariationParameter['H_ROT_PH'],
                          VariationParameter['H_ST_PH']],
               evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['ALPHA_H'],
                                                                               limitMin=alpha[0],
                                                                               limitMax=alpha[-1]),
                                                         SetParameterXVariable(paramEvol=VariationParameter['BETA'],
                                                                               limitMin=beta[0],
                                                                               limitMax=beta[-1]),
                                                         SetParameterFixed(paramEvol=VariationParameter['DZ'],
                                                                           currentValue=0.5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               limitMin=r_mot[0],
                                                                               limitMax=r_mot[-1])]),
               filename=dir+mot+'_0_DIMENSIONS_rev'+rev)
			   
#######################################################################################################################
## 1 DZ
     
## auxiliary category
## in this case, DZ
x0=.5     #init
dx=1     #diff
N=1          #length
cat=[None]*N      #initialize size
cat[0]=x0          #first value
for i in range(N-1):     
     cat[i+1]=round(cat[i]+dx,2)     

### insert and adjust headers
category = 'DZ'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_1_DZ_rev'+rev+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')     
n=100000 ##counter for value extraction
for m in range(0,len(cat)):
     for l in range(0,len(r_mot)):
          for k in range(0,len(d_gap)):
               for j in range(0,len(beta)):
                    for i in range(0,len(alpha)):
                                        ##switch scenario
                                        selectCurrentStep(activeScenario=Scenario['1_DZ'],
                                                       parameterValue=['ALPHA_H='+str(alpha[i]),
                                                                           'BETA='+str(beta[j]),
                                                                           'DZ='+str(cat[m]),
                                                                           'R_ST_OUT='+str(r_mot[l])])#,
                                                                           #'R_ST_OUT='+str(r_mot[l])])

                                        ##scenario info
                                        values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])
                                        
                                        ##f_rot
                                        result = predefine['F_ROT'].createResultCurrentValue(result='F_ROT_DZ_'+str(n)) #extract
                                        n=n+1     #counter
                                        values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
                                        
                                        ##f_st
                                        result = predefine['F_ST'].createResultCurrentValue(result='F_ST_DZ_'+str(n)) #extract
                                        n=n+1     #counter
                                        values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string                              
                                        
                                        ##line
                                        line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
                                        
                                        ##write
                                        f.write(line)
          
f.close()
n                                          


#######################################################################################################################    
## 4 DX  
     
## auxiliary category
## in this case, JF
x0=.5     #init
dx=1     #diff
N=1          #length
cat=[None]*N      #initialize size
cat[0]=x0          #first value
for i in range(N-1):     
     cat[i+1]=round(cat[i]+dx,2)     

### insert and adjust headers
category = 'DX'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_4_DX_rev'+rev+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')     
n=200000 ##counter for value extraction
for m in range(0,len(cat)):
     for l in range(0,len(r_mot)):
          for k in range(0,len(d_gap)):
               for j in range(0,len(beta)):
                    for i in range(0,len(alpha)):
                                        ##switch scenario
                                        selectCurrentStep(activeScenario=Scenario['4_DX'],
                                                       parameterValue=['ALPHA_H='+str(alpha[i]),
                                                                           'BETA='+str(beta[j]),
                                                                           'DX='+str(cat[m]),
                                                                           'R_ST_OUT='+str(r_mot[l])])#,
                                                                           #'R_ST_OUT='+str(r_mot[l])])

                                        ##scenario info
                                        values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])
                                        
                                        ##f_rot
                                        result = predefine['F_ROT'].createResultCurrentValue(result='F_ROT_DY_'+str(n)) #extract
                                        n=n+1     #counter
                                        values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
                                        
                                        ##f_st
                                        result = predefine['F_ST'].createResultCurrentValue(result='F_ST_DY_'+str(n)) #extract
                                        n=n+1     #counter
                                        values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string                              
                                        
                                        ##line
                                        line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
                                        
                                        ##write
                                        f.write(line)
          
f.close()
n     

#######################################################################################################################  
## 5 DY
	
## auxiliary category
## in this case, JF
x0=.5	#init
dx=1	#diff
N=1		#length
cat=[None]*N 	#initialize size
cat[0]=x0		#first value
for i in range(N-1):	
	cat[i+1]=round(cat[i]+dx,2)	

### insert and adjust headers
category = 'DX;DTHETA'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_5_DY_rev'+rev+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')	
n=300000 ##counter for value extraction
for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(d_gap)):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
								##switch scenario

								selectCurrentStep(activeScenario=Scenario['5_DY'],
												  parameterValue=['ALPHA_H='+str(alpha[i]),
																  'BETA='+str(beta[j]),
																  'DX=1.0',
																  'DTHETA=90.0',
																  'R_ST_OUT='+str(r_mot[l])])#,								
																  #'R_ST_OUT='+str(r_mot[l])])

								##scenario info
								values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])+';90'
								
								##f_rot
								result = predefine['F_ROT'].createResultCurrentValue(result='F_ROT_DY_'+str(n)) #extract
								n=n+1	#counter
								values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
								
								##f_st
								result = predefine['F_ST'].createResultCurrentValue(result='F_ST_DY_'+str(n)) #extract
								n=n+1	#counter
								values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string						
								
								##line
								line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
								
								##write
								f.write(line)
		
f.close()
n				

#######################################################################################################################
#######################################################################################################################
## 2 DALPHA
# selectCurrentStep(activeScenario=Scenario['2_DALPHA'],
                  # parameterValue=['ALPHA_H=1.0',
                                  # 'BETA=0.1',
                                  # 'DALPHA=2.5',
                                  # 'D_AGAP=2.0',
                                  # 'R_ST_OUT=10.0'])
								  
## 2 DALPHA
selectCurrentStep(activeScenario=Scenario['2_DALPHA_2'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DALPHA=1.5',
                                  'R_ST_OUT='+str(r_mot[0])])#,
                                  #'R_ST_OUT='+str(r_mot[0])])								  


CSVExportTable(parameter=[VariationParameter['DALPHA'],
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
                                                         SetParameterFixed(paramEvol=VariationParameter['DALPHA'],
                                                                           currentValue=1.5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               limitMin=r_mot[0],
                                                                               limitMax=r_mot[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_2_DALPHA_rev'+rev)

#######################################################################################################################
## 3 DBETA
selectCurrentStep(activeScenario=Scenario['3_DBETA_2'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DBETA=1.5',
                                  'R_ST_OUT='+str(r_mot[0])])#,
                                  #'R_ST_OUT='+str(r_mot[0])])	

CSVExportTable(parameter=[VariationParameter['DBETA'],
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
                                                         SetParameterFixed(paramEvol=VariationParameter['DBETA'],
                                                                           currentValue=1.5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               limitMin=r_mot[0],
                                                                               limitMax=r_mot[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_3_DBETA_rev'+rev)
