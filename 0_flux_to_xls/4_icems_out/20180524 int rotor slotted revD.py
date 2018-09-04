## EXPORT INT ROTOR SLOTLESS
## REV C USES CYLINDRICAL GEOMETRY, THEREFORE COORD_SYS_ST IS IN THE MIDDLE OF THE MOTOR AND NOT BELOW
#######################################################################################################################
#######################################################################################################################
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
N=5
beta=[None]*N
beta[0]=x0
for i in range(N-1):
	beta[i+1]=round(beta[i]+dx,2)

## dgap, but it is actually L_SLOT
x0=2.0	#init
dx=1	#diff
N=3	#length
d_gap=[None]*N 	#initialize size
d_gap[0]=x0		#first value
for i in range(N-1):	
	d_gap[i+1]=round(d_gap[i]+dx,2)	
	
## rmot
x0=15.0	#init
dx=5	#diff
N=3		#length
r_mot=[None]*N 	#initialize size
r_mot[0]=x0		#first value
for i in range(N-1):	
	r_mot[i+1]=round(r_mot[i]+dx,2)	

#######################################################################################################################
#######################################################################################################################
#info about the motor and its revision and blahblah
rev='2'
mot='1'
dir='rev'+rev+'/' ##create this folder manually	

##################################################################
#######################################################################################################################
	
## 0 FIELDS

##path inside stator iron								  
PathArcCenterAngle(name='Path_1',
                   pathDiscretization=PointPathDiscretization(pointNumber=1024),
                   regionVolume='IRON_ST',
                   color=Color['White'],
                   visibility=Visibility['VISIBLE'],
                   coordSys=CoordSys['COORD_SYS_ST'],
                   centerCoord=['0',
                                '0',
                                'h_st/2'],
                   angle=['0',
                          '359'],
                   radius='.5*(R_ST_OUT+R_ST_IN)')

lastInstance = CompoundPath(name='FE_PER',
             paths=[Path['PATH_1']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])	

##path through slot			 
PathStraightLine2PTS(name='PATH_2',
                     pathDiscretization=PointPathDiscretization(pointNumber=1024),
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                          uvw=['(R_ROT_OUT+D_AGAP)*Cosd(30)', '(R_ROT_OUT+D_AGAP)*Sind(30)', 'h_st/2']),
                     endPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                        uvw=['(R_ROT_OUT+D_AGAP+L_SLOT)*Cosd(30)', '(R_ROT_OUT+D_AGAP+L_SLOT)*Sind(30)', 'h_st/2']))			 
								  
lastInstance = CompoundPath(name='FE_SLOT',
             paths=[Path['PATH_2']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

##approximate area between slots			 
lastInstance = Grid2DAnnular(name='Grid2D_1',
              coordSys=CoordSys['COORD_SYS_ST'],
              visibility=Visibility['VISIBLE'],
              color=Color['Turquoise'],
              origin=['0',
                      '0',
                      'H_ST/2'],
              radius=['R_ST_IN-L_SLOT',
                      'R_ST_IN',
                      '20'],
              theta=['-12.5',
                     '12.5',
                     '20'])
					 
##REAL AREA WERE COIL IS
lastInstance = Grid2DRectangularXY(name='COIL_UP',
                    coordSys=CoordSys['COORD_COIL_1'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2',
                            'H_ST/2',
                            'TH_COIL_OFFSET+L_COIL/2'],
                    alongX=['W_SLOT',
                            '0',
                            '10'],
                    alongY=['TH_COIL',
                            '0',
                            '10'])

lastInstance = Grid2DRectangularXY(name='COIL_DOWN',
                    coordSys=CoordSys['COORD_COIL_1'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2',
                            'H_ST/2-H_ST-TH_COIL',
                            'TH_COIL_OFFSET+L_COIL/2'],
                    alongX=['W_SLOT',
                            '0',
                            '10'],
                    alongY=['TH_COIL',
                            '0',
                            '10'])
							
lastInstance = Grid2DRectangularXY(name='COIL_LEFT',
                    coordSys=CoordSys['COORD_COIL_1'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2-TH_COIL',
                            'H_ST/2-H_ST-TH_COIL',
                            'TH_COIL_OFFSET+L_COIL/2'],
                    alongX=['TH_COIL',
                            '0',
                            '10'],
                    alongY=['H_ST+2*TH_COIL',
                            '0',
                            '10'])							

lastInstance = Grid2DRectangularXY(name='COIL_RIGHT',
                    coordSys=CoordSys['COORD_COIL_1'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2-TH_COIL+W_SLOT+TH_COIL',
                            'H_ST/2-H_ST-TH_COIL',
                            'TH_COIL_OFFSET+L_COIL/2'],
                    alongX=['TH_COIL',
                            '0',
                            '10'],
                    alongY=['H_ST+2*TH_COIL',
                            '0',
                            '10'])							

#########################################################################################################################
## FIELDS 0 
## REAL EXPORT 

# to be able to export values of integral
import sys

f = open(dir+mot+'_0_brms_a_around_teeth_rev'+rev+'.csv','w')
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;BRMS/A'
f.write(headers) 
f.write('\n')	 

# CurveSpatial2D[ALL].delete()

blah='12'
for l in range(0,len(r_mot)):
	for k in range(0,len(d_gap)):
		for j in range(0,len(beta)):
			for i in range(0,len(alpha)):
				if (i==2 and j==0 and k == 2 and l==0) or (i==4 and j==2 and k == 2 and l==0) or (i==5 and j==0 and k == 2 and l==1) or (i==4 and j==0 and k == 0 and l==2) or (i==5 and j==0 and k == 0 and l==2) or (i==0 and j==0 and k == 2 and l==2) or (i==0 and j==4 and k == 2 and l==2):
					brms_3D = sqrt(0);
					values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])				
				else:
					##filename
					aux='_alpha'+str(alpha[i])+'_beta_'+str(beta[j])+'_dgap_'+str(d_gap[k])+'_rout_'+str(r_mot[l])
					aux=aux.replace('.', '')
					
					##select the step
					selectCurrentStep(activeScenario=Scenario['0_FIELD'],
									parameterValue=['ALPHA_H='+str(alpha[i]),
													'BETA='+str(beta[j]),
													'DTHETA=30.0',
													'L_SLOT='+str(d_gap[k]),
													'R_ST_OUT='+str(r_mot[l])])
					##circle in rotor
					##do curve
					# SpatialCurve(name='perimeter'+aux,
					# compoundPath=CompoundPath['FE_PER'],
							# formula=['Comp(1,B)',
							# 'Comp(2,B)',
							# 'Comp(3,B)'])
					# export 
					# CurveSpatial2D['perimeter'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/perimeter_int_rotor_slotted'+aux,
							# mode='add')

					#slot
					# SpatialCurve(name='slot'+aux,
						# compoundPath=CompoundPath['FE_SLOT'],
						# formula=['Comp(1,B)',
								 # 'Comp(2,B)',
								 # 'Comp(3,B)'])		

					# CurveSpatial2D['slot'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/slot_int_rotor_slotted'+aux,
						# mode='add')					

					##around teeth
					##up
					a_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP']]),
							spatialFormula='1',
							resultName='IntegralSurf_A'+blah+'_UP_WHOLE'+aux+'_DTHETA_30')
				 
					b_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP']]),
							spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
							resultName='IntegralSurf_B'+blah+'_UP_WHOLE'+aux+'_DTHETA_30')
					##down						
					a_down = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN']]),
							spatialFormula='1',
							resultName='IntegralSurf_A'+blah+'_DOWN_WHOLE'+aux+'_DTHETA_30')
				 
					b_down = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN']]),
							spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
							resultName='IntegralSurf_B'+blah+'_DOWN_WHOLE'+aux+'_DTHETA_30')
					##left												
					a_left = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_LEFT']]),
							spatialFormula='1',
							resultName='IntegralSurf_A'+blah+'_LEFT_WHOLE'+aux+'_DTHETA_30')
				 
					b_left = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_LEFT']]),
							spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
							resultName='IntegralSurf_B'+blah+'_LEFT_WHOLE'+aux+'_DTHETA_30')
					##right part
					a_right = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_RIGHT']]),
							spatialFormula='1',
							resultName='IntegralSurf_A'+blah+'_RIGHT_WHOLE'+aux+'_DTHETA_30')
				 
					b_right = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_RIGHT']]),
							spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
							resultName='IntegralSurf_B'+blah+'_RIGHT_WHOLE'+aux+'_DTHETA_30')

					b_int=b_up.value+b_down.value+b_left.value+b_right.value
					
					a_int=a_up.value+a_down.value+a_left.value+a_right.value
					
					brms_3D = sqrt(b_int/a_int);
						
					values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])
						
				line=values_scn+';'+str(brms_3D)+'\n'
				
				f.write(line)				
f.close()				

# CSVExportTable(parameter=[VariationParameter['L_BAR_PH']],
               # evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['ALPHA_H'],
                                                                               # limitMin=alpha[0],
                                                                               # limitMax=alpha[-1]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['BETA'],
                                                                               # limitMin=beta[0],
                                                                               # limitMax=beta[-1]),
                                                         # SetParameterFixed(paramEvol=VariationParameter['DTHETA'],
                                                                           # currentValue=30),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['L_SLOT'],
                                                                               # limitMin=d_gap[0],
                                                                               # limitMax=d_gap[-1]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               # filename=dir+mot+'_0_LBAR_REV'+rev)

#######################################################################################################################
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
n=1000 ##counter for value extraction
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
                                                                           'L_SLOT='+str(d_gap[k]),
                                                                           'R_ST_OUT='+str(r_mot[l])])

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
n=1000 ##counter for value extraction
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
                                                                           'L_SLOT='+str(d_gap[k]),
                                                                           'R_ST_OUT='+str(r_mot[l])])

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
n=2000 ##counter for value extraction
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
																  'L_SLOT='+str(d_gap[k]),				
																  'R_ST_OUT='+str(r_mot[l])])
								
								# selectCurrentStep(activeScenario=Scenario['5_DY'],
											# parameterValue=['ALPHA_H='+str(alpha[i]),
															# 'BETA='+str(beta[j]),
															# 'D_AGAP='+str(d_gap[k]),								
															# 'R_ST_OUT='+str(r_mot[l])								,
															# 'DTHETA=90.0',
															# 'DX='+str(cat[m])])

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
## 7 JF_RMS
### insert and adjust headers
category = 'JF_RMS'
exp = 'IF_HAT;A_CU;P_CU_TOT;F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_7_JF_rev'+rev+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')

## auxiliary category
## in this case, JF
x0=6	#init
dx=2	#diff
N=1		#length
cat=[None]*N 	#initialize size
cat[0]=x0		#first value
for i in range(N-1):	
	cat[i+1]=round(cat[i]+dx,2)	

##now start cycling scenarios
n=70000 ##counter for value extraction
for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(d_gap)):		#range(0,len(d_gap)):
			for j in range(0,len(beta)):	#range(0,len(beta)):
				for i in range(0,len(alpha)):
					if (i==0 and j ==2 and k ==0 and l ==0)or(i==5 and j ==0 and k ==1 and l ==0)or(i==1 and j ==0 and k ==1 and l ==1)or(i==4 and j ==0 and k ==0 and l ==2)or(i==5 and j ==0 and k ==0 and l ==2)or(i==5 and j ==0 and k ==2 and l ==2):
						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])
						line=values_scn+';'+'0'+';'+'0'+';'+'0'+';'+'0'+';'+'0'+'\n'
					else:
						##switch scenario
						selectCurrentStep(activeScenario=Scenario['7_JF'],
									parameterValue=['ALPHA_H='+str(alpha[i]),
													'BETA='+str(beta[j]),
													'L_SLOT='+str(d_gap[k]),
													'R_ST_OUT='+str(r_mot[l]),
													'JF_RMS='+str(cat[m])])	

						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m]) ##scenario info
						
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
selectCurrentStep(activeScenario=Scenario['2_DALPHA'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DALPHA=5',
                                  'L_SLOT='+str(d_gap[0]),
                                  'R_ST_OUT='+str(r_mot[0])])								  


CSVExportTable(parameter=[VariationParameter['R_ROT_OUT_PH'],
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
                                                                           currentValue=5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['L_SLOT'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1]),
                                                          SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               limitMin=r_mot[0],
                                                                               limitMax=r_mot[-1])]),
               filename=dir+mot+'_2_DALPHA_rev'+rev)

#######################################################################################################################
#######################################################################################################################
## 3 DBETA
selectCurrentStep(activeScenario=Scenario['3_DBETA'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DBETA=5',
                                  'L_SLOT='+str(d_gap[0]),
                                  'R_ST_OUT='+str(r_mot[0])])	

CSVExportTable(parameter=[VariationParameter['R_ROT_OUT_PH'],
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
                                                                           currentValue=5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['L_SLOT'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1]),
                                                         SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               limitMin=r_mot[0],
                                                                               limitMax=r_mot[-1])]),
               filename=dir+mot+'_3_DBETA_rev'+rev)

#######################################################################################################################
#######################################################################################################################
## 6 JT

selectCurrentStep(activeScenario=Scenario['6_JT'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'L_SLOT='+str(d_gap[0]),
								  'R_ST_OUT='+str(r_mot[0]),							  
                                  'JT_RMS=6.0'])#,
                                  #'JT_RMS=2.0'])

CSVExportTable(parameter=[VariationParameter['R_ROT_OUT_PH'],
						  VariationParameter['JT_RMS'],
						  VariationParameter['R_ST_OUT_PH'],
                          VariationParameter['V_FE_ST_RING'],
                          VariationParameter['V_FE_ST_SLOTS'],
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
                                                         SetParameterXVariable(paramEvol=VariationParameter['L_SLOT'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1]),
                                                         SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                           currentValue=6),
                                                         SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               limitMin=r_mot[0],
                                                                               limitMax=r_mot[-1])]),
               filename=dir+mot+'_6_JT_rev'+rev)