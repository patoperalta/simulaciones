# EXPORT SENSORS

# color='VIOLET' 
# ALPHA_H=2
# BETA=0.3
# D_AGAP=3

color='RED' 
ALPHA_H=1.8
BETA=0.5
D_AGAP=2

# color='RED' 
# ALPHA_H=1.8
# BETA=0.3
# D_AGAP=2.5

# define paths were hall sensor path will be read
for i in range(1,7):
	PathStraightLine2PTS(name='P1'+str(i),
						 pathDiscretization=IntervalPathDiscretization(intervalNumber=10),
						 regionVolume='AIR',
						 color=Color['White'],
						 visibility=Visibility['VISIBLE'],
						 startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											  uvw=['(R_ST_IN-1)*Cosd(60*'+str(i-1)+')', '(R_ST_IN-1)*Sind(60*'+str(i-1)+')', '0']),
						 endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											uvw=['(R_ST_IN-1)*Cosd(60*'+str(i-1)+')', '(R_ST_IN-1)*Sind(60*'+str(i-1)+')', 'H_ST/2+1']))
	
	lastInstance = CompoundPath(name='HS_R_'+str(i),
			 paths=[Path['P1'+str(i)]],
			 color=Color['Turquoise'],
			 visibility=Visibility['VISIBLE'])

	cleanInvalidPaths()										

	PathStraightLine2PTS(name='P2'+str(i),
						 pathDiscretization=IntervalPathDiscretization(intervalNumber=10),
						 regionVolume='AIR',
						 color=Color['White'],
						 visibility=Visibility['VISIBLE'],
						 startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											  uvw=['(R_ST_IN-1)*Cosd(60*'+str(i-1)+')', '(R_ST_IN-1)*Sind(60*'+str(i-1)+')', 'H_ST/2+1']),
						 endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											uvw=['(R_ST_IN-1+D_ST+1)*Cosd(60*'+str(i-1)+')', '(R_ST_IN-1+D_ST+1)*Sind(60*'+str(i-1)+')', 'H_ST/2+1']))


	lastInstance = CompoundPath(name='HS_AX_'+str(i),
				 paths=[Path['P2'+str(i)]],
				 color=Color['Turquoise'],
				 visibility=Visibility['VISIBLE'])

	cleanInvalidPaths()

## for ANGLE	
for i in range(0,36):
	selectCurrentStep(activeScenario=Scenario['ANG_'+color],
					  parameterValue=['ALPHA_H='+str(ALPHA_H),
									  'DTHETA='+str(i*10),
									  'DX=0.5',
									  'D_AGAP='+str(D_AGAP),
									  'BETA='+str(BETA)])	

	for hs in range(1,7):
		#define name
		hr='H_R_'+str(hs)+'_'+str(color)+'_ANG_DTHETA_'+str(i*10)
		#make curve
		SpatialCurve(name=hr,
				compoundPath=CompoundPath['HS_R_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save
		CurveSpatial2D[hr].exportExcel(xlsFile='excels/'+hr,
				mode='add')
				
		#define name
		hax='H_AX_'+str(hs)+'_'+str(color)+'_ANG_DTHETA_'+str(i*10)
		#make curve		
		SpatialCurve(name=hax,
				compoundPath=CompoundPath['HS_R_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save						 
		CurveSpatial2D[hax].exportExcel(xlsFile='excels/'+hax,
				mode='add')
				
## for POS	
for i in range(0,36):
	selectCurrentStep(activeScenario=Scenario['POS_'+color],
					  parameterValue=['ALPHA_H='+str(ALPHA_H),
									  'DTHETA_0='+str(i*10),
									  'DR_0=0.5',
									  'D_AGAP='+str(D_AGAP),
									  'BETA='+str(BETA)])	

	for hs in range(1,7):
		#define name
		hr='H_R_'+str(hs)+'_'+str(color)+'_POS_DTHETA_'+str(i*10)
		#make curve
		SpatialCurve(name=hr,
				compoundPath=CompoundPath['HS_R_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save
		CurveSpatial2D[hr].exportExcel(xlsFile='excels/'+hr,
				mode='add')
				
		#define name
		hax='H_AX_'+str(hs)+'_'+str(color)+'_POS_DTHETA_'+str(i*10)
		#make curve		
		SpatialCurve(name=hax,
				compoundPath=CompoundPath['HS_R_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save						 
		CurveSpatial2D[hax].exportExcel(xlsFile='excels/'+hax,
				mode='add')				