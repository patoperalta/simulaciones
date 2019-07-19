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
	
##without points or commas...
r_mot=[10,15]
r_mot=[20]

#######################################################################################################################
	
## 0 FIELDS, prepare support

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

# to be able to export values of integral
import sys

#info about the motor and its revision and blahblah
rev='1'
mot='slotless'
dir='mot_'+mot+'/' ##create this folder manually	

##here we open the file of brms/a, and write its first line
f = open(dir+mot+'_brms_a_wholecoil_rev'+rev+'_R_'+str(r_mot[0])+'.csv','w')
headers = 'ALPHA_H;BETA;D_AGAP;R_MOT_OUT;BRMS/A'
f.write(headers) 
f.write('\n')

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

				# inside airgap
				a_in = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_GRID']]),
						spatialFormula='1',
						resultName='IntegralSurf2_A_IN_WHOLE'+aux)
			 
				b_in = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_GRID']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf2_B_IN_WHOLE'+aux)				
				#upper part
				a_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP']]),
						spatialFormula='1',
						resultName='IntegralSurf2_A_UP_WHOLE'+aux)
			 
				b_up = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_UP']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf2_B_UP_WHOLE'+aux)										
				#lower part
				a_low = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN']]),
						spatialFormula='1',
						resultName='IntegralSurf2_A_LOW_WHOLE'+aux)
			 
				b_low = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_DOWN']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf2_B_LOW_WHOLE'+aux)
				#outer part
				a_out = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_OUT']]),
						spatialFormula='1',
						resultName='IntegralSurf2_A_OUT_WHOLE'+aux)
			 
				b_out = IntegralFace(support=SupportIntegral2dGrid(grid2d=[Grid2D['COIL_OUT']]),
						spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
						resultName='IntegralSurf2_B_OUT_WHOLE'+aux)						
			
				b_int=b_in.value+b_up.value+b_low.value+b_out.value
				
				a_int=a_in.value+a_up.value+a_low.value+a_out.value
				
				brms_3D = sqrt(b_int/a_int);
					
				values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(d_gap[k])+';'+str(r_mot[l])
						
				line=values_scn+';'+str(brms_3D)+'\n'
			
				f.write(line)			
f.close()