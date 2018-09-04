## EXPORT INT ROTOR SLOTLESS
## REV C USES CYLINDRICAL GEOMETRY, THEREFORE COORD_SYS_ST IS IN THE MIDDLE OF THE MOTOR AND NOT BELOW
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
mot='3'
dir='rev'+rev+'/' ##create this folder manually	

#######################################################################################################################
#######################################################################################################################
	
## 0 FIELDS

## for higher coord_sys_st using cilidrical geometry			 
lastInstance = CoordSysCartesian(name='Coord_SYS_ST_LOW',
                  parentCoordSys=Local(coordSys=CoordSys['Coord_SYS_ST']),
                  origin=['0',
                          '0',
                          '-h_st/2'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='0',
                                                angleZ='0'),
                  visibility=Visibility['VISIBLE']) 	

## DO PATH AND GRIDS
## circle inside iron 
PathArcCenterAngle(name='Path_01',
                   pathDiscretization=PointPathDiscretization(pointNumber=1024),
                   regionVolume='IRON_ST',
                   color=Color['White'],
                   visibility=Visibility['VISIBLE'],
                   coordSys=CoordSys['Coord_SYS_ST_LOW'],
                   centerCoord=['0',
                                '0',
                                'h_st/2'], # x 0 if cilyndric construction is chosen, because Coord_SYS_ST_LOW is displaced
                   angle=['0',
                          '359'],
                   radius='.5*(R_ST_OUT+R_ST_IN)')

lastInstance = CompoundPath(name='FE_PER',
             paths=[Path['Path_01']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])	

## circle inside airgap			 
PathArcCenterAngle(name='PATH_02',
                   pathDiscretization=PointPathDiscretization(pointNumber=1024),
                   color=Color['White'],
                   visibility=Visibility['VISIBLE'],
                   coordSys=CoordSys['COORD_SYS_ROT'],
                   centerCoord=['0',
                                '0',
                                '0'],
                   angle=['0',
                          '359'],
                   radius='R_ROT_OUT+.5*D_AGAP')

lastInstance = CompoundPath(name='AIRGAP_PERIMETER',
             paths=[Path['PATH_02']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])	

## grid where coil is			 
lastInstance = Grid2DRectangularXZ(name='COIL_GRID',
                    coordSys=CoordSys['Coord_SYS_ST_LOW'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['R_ST_IN-COIL_R',
                            '0',
                            '0'],
                    alongX=['COIL_R',
                            '0',
                            '10'],							
                    alongZ=['h_st',		#for Coord_SYS_ST_LOW at the bottom
                            '0',
                            '10'])	

## vertical path were strongest flux is located
PathStraightLine2PTS(name='Path_03',
                     pathDiscretization=PointPathDiscretization(pointNumber=1024),
                     regionVolume='IRON_ST',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['Coord_SYS_ST_LOW'],
                                          uvw=['0', '0.5*(R_ST_OUT+R_ST_IN)', '0']),
                     endPoint=PathPoint(coordSys=CoordSys['Coord_SYS_ST_LOW'],
                                        uvw=['0', '0.5*(R_ST_OUT+R_ST_IN)', 'H_ST']))


lastInstance = CompoundPath(name='FE_HEIGHT',
             paths=[Path['PATH_03']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])		

##upper part of coil
lastInstance = Grid2DRectangularXZ(name='COIL_UP',
                    coordSys=CoordSys['Coord_SYS_ST_LOW'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['r_st_in-coil_R',
                            '0',
                            'h_st'],
                    alongX=['coil_r+R_ST_OUT-R_ST_IN+COIL_R',
                            '0',
                            '10'],
                    alongZ=['coil_r',
                            '0',
                            '10'])

##outer part of coil
lastInstance = Grid2DRectangularXZ(name='COIL_OUT',
                    coordSys=CoordSys['Coord_SYS_ST_LOW'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['R_ST_OUT',
                            '0',
                            '0'],
                    alongX=['COIL_R',
                            '0',
                            '10'],
                    alongZ=['H_st',
                            '0',
                            '10'])

##lower part of coil
lastInstance = Grid2DRectangularXZ(name='COIL_DOWN',
                    coordSys=CoordSys['Coord_SYS_ST_LOW'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['r_st_in-coil_R',
                            '0',
                            '-coil_r'],
                    alongX=['coil_r+R_ST_OUT-R_ST_IN+COIL_R',
                            '0',
                            '10'],
                    alongZ=['coil_r',
                            '0',
                            '10'])

#########################################################################################################################
##change scenario

# to be able to export values of integral
import sys

f = open(dir+mot+'_0_brms_a_wholecoil_rev'+rev+'.csv','w')
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
			
				#select scenario
				selectCurrentStep(activeScenario=Scenario['0_FIELD'],
					parameterValue=['ALPHA_H='+str(alpha[i]),
									'BETA='+str(beta[j]),
									'D_AGAP='+str(d_gap[k]),
									'R_ST_OUT='+str(r_mot[l])])
	
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
				# or do the export for the for parts
				
				# inside airgap
				a_in = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_GRID']]),
						spatialFormula='1',
						resultName='IntegralSurf_A_IN_WHOLE'+aux)
			 
				b_in = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_GRID']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B_IN_WHOLE'+aux)				
				#upper part
				a_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP']]),
						spatialFormula='1',
						resultName='IntegralSurf_A_UP_WHOLE'+aux)
			 
				b_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B_UP_WHOLE'+aux)										
				#lower part
				a_low = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN']]),
						spatialFormula='1',
						resultName='IntegralSurf_A_LOW_WHOLE'+aux)
			 
				b_low = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B_LOW_WHOLE'+aux)
				#outer part
				a_out = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_OUT']]),
						spatialFormula='1',
						resultName='IntegralSurf_A_OUT_WHOLE'+aux)
			 
				b_out = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_OUT']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf_B_OUT_WHOLE'+aux)						
			
				b_int=b_in.value+b_up.value+b_low.value+b_out.value
				
				a_int=a_in.value+a_up.value+a_low.value+a_out.value
				
				brms_3D = sqrt(b_int/a_int);
					
				values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])
						
				line=values_scn+';'+str(brms_3D)+'\n'
			
				f.write(line)			
f.close()

##BEING STILL IN FIELD SCENARIO, RUN THIS

CSVExportTable(parameter=[VariationParameter['R_ROT_OUT'],
						  VariationParameter['L_BAR_PH']],
               evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['ALPHA_H'],
                                                                               limitMin=alpha[0],
                                                                               limitMax=alpha[-1]),
                                                         SetParameterXVariable(paramEvol=VariationParameter['BETA'],
                                                                               limitMin=beta[0],
                                                                               limitMax=beta[-1]),
                                                         SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_0_LBAR_REV'+rev)

#######################################################################################################################
#######################################################################################################################
## 1 DZ

### insert and adjust headers
category = 'DZ'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## auxiliary category
## in this case, JF
x0=.5	#init
dx=1	#diff
N=1		#length
cat=[None]*N 	#initialize size
cat[0]=x0		#first value
for i in range(N-1):	
	cat[i+1]=round(cat[i]+dx,2)	

## open the file and
f = open(dir+mot+'_1_DZ_rev'+rev+'.csv','w')
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
								selectCurrentStep(activeScenario=Scenario['1_DZ'],
											parameterValue=['ALPHA_H='+str(alpha[i]),
															'BETA='+str(beta[j]),
															'DZ='+str(cat[m]),
															'D_AGAP='+str(d_gap[k])])#,
															# 'R_ST_OUT='+str(r_mot[l])])

								##scenario info
								values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])+';'+str(cat[m])
								
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

#######################################################################################################################
#######################################################################################################################

## 2 DALPHA
selectCurrentStep(activeScenario=Scenario['2_DALPHA'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DALPHA=5',
                                  'D_AGAP='+str(d_gap[0])])#,
                                  # 'R_ST_OUT=10.0'])


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
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_2_DALPHA_rev'+rev)

#######################################################################################################################
#######################################################################################################################

## 3 DBETA
selectCurrentStep(activeScenario=Scenario['3_DBETA'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'DBETA=5',
                                  'D_AGAP='+str(d_gap[0]),
                                  'R_ST_OUT='+str(r_mot[0])])

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
                                                         SetParameterFixed(paramEvol=VariationParameter['DBETA'],
                                                                           currentValue=5),
                                                         SetParameterXVariable(paramEvol=VariationParameter['D_AGAP'],
                                                                               limitMin=d_gap[0],
                                                                               limitMax=d_gap[-1])]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1])]),
               filename=dir+mot+'_3_DBETA_rev'+rev)


#######################################################################################################################
#######################################################################################################################

## 4 DX
	
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
category = 'DX'
exp = 'F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;'+category+';'+exp

## open the file and
f = open(dir+mot+'_4_DX_rev'+rev+'.csv','w')
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
								##switch scenario
								selectCurrentStep(activeScenario=Scenario['4_DX'],
											parameterValue=['ALPHA_H='+str(alpha[i]),
															'BETA='+str(beta[j]),
															'DX='+str(cat[m]),
															'D_AGAP='+str(d_gap[k])])#,
															# 'R_ST_OUT='+str(r_mot[l])])

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
n=0 ##counter for value extraction
for m in range(0,len(cat)):
	for l in range(0,len(r_mot)):
		for k in range(0,len(d_gap)):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
								##switch scenario
								selectCurrentStep(activeScenario=Scenario['5_DY'],
											parameterValue=['ALPHA_H='+str(alpha[i]),
															'BETA='+str(beta[j]),
															'D_AGAP='+str(d_gap[k]),								
															# 'R_ST_OUT='+str(r_mot[l]),
															'DTHETA=90.0',
															'DX='+str(cat[m])])

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
## 6 JT
selectCurrentStep(activeScenario=Scenario['6_JT'],
                  parameterValue=['ALPHA_H='+str(alpha[0]),
                                  'BETA='+str(beta[0]),
                                  'D_AGAP='+str(d_gap[0]),
                                  # 'R_ST_OUT='+str(r_mot[0]),
                                  'JT_RMS=6.0'])

# lastInstance = VariationParameterFormula(name='R_ROT_PH',
                          # formula='R_ROT_OUT')						  
								  
CSVExportTable(parameter=[VariationParameter['R_ROT_OUT'],
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
                                                         # SetParameterXVariable(paramEvol=VariationParameter['R_ST_OUT'],
                                                                               # limitMin=r_mot[0],
                                                                               # limitMax=r_mot[-1]),
                                                         # SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                               # limitMin=2.0,
                                                                               # limitMax=4.0)]),
                                                         SetParameterFixed(paramEvol=VariationParameter['JT_RMS'],
                                                                           currentValue=6)]),																			   
               filename=dir+mot+'_6_JT_rev'+rev)

#######################################################################################################################
#######################################################################################################################								  
## 7 JF_RMS
### insert and adjust headers
category = 'JF_RMS'
exp = 'IF_HAT;A_CU;P_CU_TOT;F_ROT_X;F_ROT_Y;F_ROT_Z;F_ST_X;F_ST_Y;F_ST_Z'
headers = 'ALPHA_H;BETA;D_AGAP;R_ROT_OUT;'+category+';'+exp

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
n=1 ##counter for value extraction
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
															# 'R_ST_OUT='+str(r_mot[l]),
															# 'JF_RMS='+str(cat[m])])	
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