##EXPORT EXT ROTOR SLOTTED
## REV C USES CYLINDRICAL GEOMETRY for geometry... that does not change much for the export... i also made the design space wider
#######################################################################################################################
#######################################################################################################################
#design space definition
## alpha export
x0=1.4
dx=0.2
N=4
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

## dgap
x0=1.5	#init
dx=.5	#diff
N=4		#length
d_gap=[None]*N 	#initialize size
d_gap[0]=x0		#first value
for i in range(N-1):	
	d_gap[i+1]=round(d_gap[i]+dx,2)	
	
## rmot
x0=7.5	#init
dx=1	#diff
N=1		#length
r_mot=[None]*N 	#initialize size
r_mot[0]=x0		#first value
for i in range(N-1):	
	r_mot[i+1]=round(r_mot[i]+dx,2)	
#######################################################################################################################
#######################################################################################################################
#info about the motor and its revision and blahblah
rev='8'
mot='2'
dir='rev'+rev+'/' ##create this folder manually
#######################################################################################################################
#######################################################################################################################
	
##0 FIELDS

## GRIDS AND LINES

#######################################################################################################################
##LINES WHERE FIELD WILL BE EXTRACTED
PathStraightLine2PTS(name='Path_1',
                     pathDiscretization=PointPathDiscretization(pointNumber=1024),
                     regionVolume='IRON_ST',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                          uvw=['(K_W_SLOT*R_ROT_OUT)/2*1/Sin(pi()/6)*Cos(pi()/3)', '(K_W_SLOT*R_ROT_OUT)/2*1/Sin(pi()/6)*Sin(pi()/3)', 'H_ST/2']),
                     endPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                        uvw=['R_ST_OUT*Cos(pi()/3)', 'R_ST_OUT*Sin(pi()/3)', 'H_ST/2']))


lastInstance = CompoundPath(name='SLOT : through B-charged slot',
             paths=[Path['PATH_1']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

cleanInvalidPaths()

cleanInvalidPaths()

PathStraightLine2PTS(name='PATH_2',
                     pathDiscretization=PointPathDiscretization(pointNumber=1024),
                     regionVolume='IRON_ST',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                          uvw=['0', '0', 'H_ST/2']),
                     endPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                        uvw=['(K_W_SLOT*R_ROT_OUT)/2*1/Sin(pi()/6)*Cos(pi()/3)', '(K_W_SLOT*R_ROT_OUT)/2*1/Sin(pi()/6)*Sin(pi()/3)', 'H_ST/2']))


lastInstance = CompoundPath(name='CENTER_R_SC : center of slot facing magnet',
             paths=[Path['PATH_2']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

cleanInvalidPaths()
							
##2D GRID FROM COILS, MIDDLE PART
lastInstance = Grid2DRectangularXY(name='COIL_UP_MID',
                    coordSys=CoordSys['COORD_COIL_2'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2',
                            'H_ST/2',
                            '-1/2*(L_SLOT_OUT-W_SLOT/2*1/Sin(Pi()/6))'],
                    alongX=['W_SLOT',
                            '0',
                            '10'],
                    alongY=['K_COIL*R_ROT_OUT',
                            '0',
                            '10'])

lastInstance = Grid2DRectangularXY(name='COIL_DOWN_MID',
                    coordSys=CoordSys['COORD_COIL_2'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2',
                            'H_ST/2-H_ST-K_COIL*R_ROT_OUT',
                            '-1/2*(L_SLOT_OUT-W_SLOT/2*1/Sin(Pi()/6))'],
                    alongX=['W_SLOT',
                            '0',
                            '10'],
                    alongY=['K_COIL*R_ROT_OUT',
                            '0',
                            '10'])

lastInstance = Grid2DRectangularXY(name='COIL_LEFT_MID',
                    coordSys=CoordSys['COORD_COIL_2'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['W_SLOT/2+K_COIL*R_ROT_OUT',
                            '-H_ST/2-K_COIL*R_ROT_OUT',
                            '-1/2*(L_SLOT_OUT-W_SLOT/2*1/Sin(Pi()/6))'],
                    alongX=['0',
                            'K_COIL*R_ROT_OUT',
                            '10'],
                    alongY=['K_COIL*R_ROT_OUT+H_ST+K_COIL*R_ROT_OUT',
                            '0',
                            '10'])

lastInstance = Grid2DRectangularXY(name='COIL_RIGHT_MID',
                    coordSys=CoordSys['COORD_COIL_2'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['-W_SLOT/2',
                            '-H_ST/2-K_COIL*R_ROT_OUT',
                            '-1/2*(L_SLOT_OUT-W_SLOT/2*1/Sin(Pi()/6))'],
                    alongX=['0',
                            'K_COIL*R_ROT_OUT',
                            '10'],
                    alongY=['K_COIL*R_ROT_OUT+H_ST+K_COIL*R_ROT_OUT',
                            '0',
                            '10'])							

#########################################################################################################################
## FIELDS 0 
## REAL EXPORT 
	
import sys

f = open(dir+mot+'0_brms_a_wholecoil_mid_rev'+rev+'.csv','w')
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;BRMS/A'
f.write(headers) 
f.write('\n')

##example	
for l in range(0,len(r_mot)):
	for k in range(0,len(d_gap)):
		for j in range(0,len(beta)):
			for i in range(0,len(alpha)):

				##name
				aux='_alpha'+str(alpha[i])+'_beta_'+str(beta[j])+'_dgap_'+str(d_gap[k]*10)+'_rout_'+str(r_mot[l])
				aux=aux.replace('.', '')
			
				# select scenario
				selectCurrentStep(activeScenario=Scenario['0_FIELD'],
					parameterValue=['ALPHA_H='+str(alpha[i]),
									'BETA='+str(beta[j]),
									'D_AGAP='+str(d_gap[k])])#,
									# 'R_ROT_OUT='+str(r_mot[l])])
				
				##GRIDS
				# inside airgap
				a_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP_MID']]),
						spatialFormula='1',
						resultName='IntegralSurf_A2_IN_UP_m_3'+aux)
			 
				b_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP_MID']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B2_IN_UP_m_3'+aux)				
				# upper part
				a_down = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN_MID']]),
						spatialFormula='1',
						resultName='IntegralSurf_A2_UP_DOWN_m_3'+aux)
			 
				b_down = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN_MID']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B2_UP_DOWN_m_3'+aux)										
				# lower part
				a_left = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_LEFT_MID']]),
						spatialFormula='1',
						resultName='IntegralSurf_A2_LOW_LEFT_m_3'+aux)
			 
				b_left = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_LEFT_MID']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B2_LOW_LEFT_m_3'+aux)
				# outer part
				a_right = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_RIGHT_MID']]),
						spatialFormula='1',
						resultName='IntegralSurf_A2_OUT_RIGHT_m_3'+aux)
			 
				b_right = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_RIGHT_MID']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B2_OUT_RIGHT_m_3'+aux)						
			
				b_int=b_up.value+b_down.value+b_left.value+b_right.value
				
				a_int=a_up.value+a_down.value+a_left.value+a_right.value
				
				brms_3D = sqrt(b_int/a_int);
					
				values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])
						
				line=values_scn+';'+str(brms_3D)+'\n'
			
				f.write(line)
				
				##PATHS
				SpatialCurve(name='center_rsc_2'+aux,
							 compoundPath=CompoundPath['CENTER_R_SC'],
							 formula=['ModV(B)'])
							 
				CurveSpatial2D['center_rsc_2'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/center_rsc'+aux,
						mode='add')							 
						
				SpatialCurve(name='slot_2'+aux,
							 compoundPath=CompoundPath['SLOT'],
							 formula=['ModV(B)'])
							 
				CurveSpatial2D['slot_2'+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/slot'+aux,
						mode='add')											
f.close()	

CSVExportTable(parameter=[VariationParameter['R_ROT_OUT'],
						  VariationParameter['L_BAR_PH'],
						  VariationParameter['R_ST_OUT_PH'],
                          VariationParameter['R_SC'],
                          VariationParameter['K_W_SLOT'],
                          VariationParameter['H_ST_PH']],
               evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['ALPHA_H'],
                                                                               limitMin=alpha[0],
                                                                               limitMax=alpha[-1]),
                                                         SetParameterXVariable(paramEvol=VariationParameter['BETA'],
                                                                               limitMin=beta[0],
                                                                               limitMax=beta[-1]),
                                                         SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ROT_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_0_dimensions_rev'+rev)		   
#######################################################################################################################
## 1 DZ
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

	
## auxiliary category
## in this case, dz does not really roll
x0=.5	#init
dx=1	#diff
N=1		#length
cat=[None]*N 	#initialize size
cat[0]=x0		#first value
for i in range(N-1):	
	cat[i+1]=round(cat[i]+dx,2)	
	
n=1 ##counter for value extraction
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
															'D_AGAP='+str(d_gap[k])])#,
															# 'R_ROT_OUT='+str(r_mot[l])])

								##scenario info
								values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])
								
								##f_rot
								result = predefine['F_ROT'].createResultCurrentValue(result='F_ROT_DZ_'+str(n)) #extract
								values_f_rot=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string
								
								##f_st
								result = predefine['F_ST'].createResultCurrentValue(result='F_ST_DZ_'+str(n)) #extract
								values_f_st=str(result.value[0].value)+';'+str(result.value[1].value)+';'+str(result.value[2].value) #as string						
								
								##line
								line=values_scn+';'+values_f_rot+';'+values_f_st+'\n'
								n=n+1	#counter								
								##write
								f.write(line)
		
f.close()
n								  			   
#######################################################################################################################
##DALPHA
## 2 DALPHA
selectCurrentStep(activeScenario=Scenario['2_DALPHA'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DALPHA=5',
                                  'D_AGAP='+str(d_gap[0])])#,
                                  # 'R_ROT_OUT='+str(r_mot[0])])


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
                                                         SetParameterFixed(paramEvol=VariationParameter['DALPHA'],
                                                                           currentValue=5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ROT_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_2_DALPHA_rev'+rev)
######################################################################################################################			   
## 3 DBETA

selectCurrentStep(activeScenario=Scenario['3_DBETA'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DALPHA=5',
                                  'DTHETA=45.0',
                                  'D_AGAP='+str(d_gap[0])])#,
                                  # 'R_ROT_OUT='+str(r_mot[0])])


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
                                                         SetParameterFixed(paramEvol=VariationParameter['DALPHA'],
                                                                           currentValue=5),
                                                         SetParameterFixed(paramEvol=VariationParameter['DTHETA'],
                                                                           currentValue=45.0),
                                                         SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ROT_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_3_DBETA_rev'+rev)

######################################################################################################################
			   
## 4 DX
### insert and adjust headers
	
## auxiliary category
## in this case, JF
x0=.5	#init
dx=1	#diff
N=1		#length
cat=[None]*N 	#initialize size
cat[0]=x0		#first value
for i in range(N-1):	
	cat[i+1]=round(cat[i]+dx,2)

category = 'DX'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_4_DX_rev'+rev+'.csv','w')
## writer the header
f.write(headers) #Give your csv text here.
## Python will convert \n to os.linesep
f.write('\n')	
	
n=1 ##counter for value extraction
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
															'D_AGAP='+str(d_gap[k])])#,
															# 'R_ROT_OUT='+str(r_mot[l])])

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
			   
####################################################################################################################### 5 DY

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
	
n=1 ##counter for value extraction
for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(d_gap)):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
								##switch scenario
								selectCurrentStep(activeScenario=Scenario['5_DY'],
											parameterValue=['ALPHA_H='+str(alpha[i]),
															'BETA='+str(beta[j]),
															'DX='+str(cat[m]),
															'DTHETA=45.0',
															'D_AGAP='+str(d_gap[k])]),
															# 'R_ROT_OUT='+str(r_mot[l])])

								##scenario info
								values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])+';45'
								
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
######################################################################################################################				   
## 6 JT
selectCurrentStep(activeScenario=Scenario['6_JT'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'D_AGAP='+str(d_gap[0]),
                                  # 'R_ROT_OUT='+str(r_mot[0]),
                                  'JT_RMS=6.0'])

CSVExportTable(parameter=[VariationParameter['R_ROT_OUT'],
                          VariationParameter['JT_RMS'],
                          VariationParameter['R_ROT_OUT'],						  
                          VariationParameter['V_FE_ST'],
                          VariationParameter['V_FE_ROT'],
                          VariationParameter['V_PM'],
                          VariationParameter['V_COIL'],
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
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ROT_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                               # limitMin=2.0,
                                                                               # limitMax=4.0)]),
                                                         SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                           currentValue=10)]),																			   
               filename=dir+mot+'_6_JT_rev'+rev)

#####################################################################################################################			   
			   
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
x0=10	#init
dx=2	#diff
N=1		#length
cat=[None]*N 	#initialize size
cat[0]=x0		#first value
for i in range(N-1):	
	cat[i+1]=round(cat[i]+dx,2)	

##now start cycling scenarios
n=10000 ##counter for value extraction
for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(d_gap)):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
								##switch scenario
								selectCurrentStep(activeScenario=Scenario['7_JF'],
											parameterValue=['ALPHA_H='+str(alpha[i]),
															'BETA='+str(beta[j]),
															'D_AGAP='+str(d_gap[k]),
															# 'R_ROT_OUT='+str(r_mot[l]),
															'JF_RMS='+str(cat[m])])	

								values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m]) ##scenario info

								result = VariationParameterFormula['IF_HAT'].createResultCurrentValue(result='IF_HAT_'+str(n)) ##extract copper area
								value_ifhat = str(result[0].value)								
								
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
								line=values_scn+';'+value_ifhat+';'+value_acu+';'+value_pcu+';'+values_f_rot+';'+values_f_st+'\n'
								
								##write
								f.write(line)
								n=n+1	#counter
f.close()
n				   