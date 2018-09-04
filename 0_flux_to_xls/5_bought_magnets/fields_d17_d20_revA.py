####### alpha
x0=1.4
dx=0.2
N=4
alpha=[None]*N
alpha[0]=x0
for i in range(N-1):
	alpha[i+1]=round(alpha[i]+dx,2)
	
####### d_st
x0=4.0
dx=1
N=5
d_st=[None]*N
d_st[0]=x0
for i in range(N-1):
	d_st[i+1]=round(d_st[i]+dx,2)

####### create paths
PathStraightLine2PTS(name='Path_2',
                     pathDiscretization=PointPathDiscretization(pointNumber=50),
                     regionVolume='IRON_ST',
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                          uvw=['0', 'r_st_in', '0']),
                     endPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                        uvw=['0', 'r_st_out', '0']))

##path
lastInstance = CompoundPath(name='CompoundPath',
			 paths=[Path['PATH_2']],
			 color=Color['Turquoise'],
			 visibility=Visibility['VISIBLE'])										
										
####### names
name='d20_m235'	
for i in range (0,len(alpha)):
	for j in range (0,len(d_st)):
		#select scenario
		selectCurrentStep(activeScenario=Scenario['8_STATOR_OPT'],
			parameterValue=['ALPHA_H='+str(alpha[i]),
							'D_ST='+str(d_st[j])])
		
		#name of curve
		aux='_alpha_'+str(alpha[i])+'_dst_'+str(d_st[j])
		aux=aux.replace('.', '')
				
		#create curve					 
		SpatialCurve(name='SpatialCurve'+aux,
					 compoundPath=CompoundPath['COMPOUNDPATH'],
					 formula=['ModV(B)'])					 
					 
		##save			 
		CurveSpatial2D['SpatialCurve'+aux].exportExcel(xlsFile=name,
            mode='replace')							