# EXPORT SENSORS

# color='VIOLET' 
# ALPHA_H=2
# BETA=0.3
# D_AGAP=3

sep=.5 #look at A1366 hall sensor datasheet... 

# define paths were hall sensor path will be read
for i in range(1,7):
	# radial path
	PathStraightLine2PTS(name='PRAD'+str(i),
						 pathDiscretization=DistancePathDiscretization(distance=0.5),
						 regionVolume='AIR',
						 color=Color['White'],
						 visibility=Visibility['VISIBLE'],
						 startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											  uvw=['(R_ROT_OUT+3*'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ROT_OUT+3*'+str(sep)+')*Sind(60*'+str(i-1)+')', '0']),
						 endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											uvw=['(R_ST_IN-'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ST_IN-'+str(sep)+')*Sind(60*'+str(i-1)+')', '0']))

	lastInstance = CompoundPath(name='HS_R_'+str(i),
			 paths=[Path['PRAD'+str(i)]],
			 color=Color['Turquoise'],
			 visibility=Visibility['VISIBLE'])

	cleanInvalidPaths()										

	PathStraightLine2PTS(name='PAX_TOP'+str(i),
						 pathDiscretization=DistancePathDiscretization(distance=.5),
						 regionVolume='AIR',
						 color=Color['White'],
						 visibility=Visibility['VISIBLE'],
						 startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											  uvw=['(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Sind(60*'+str(i-1)+')', 'H_ST/2+'+str(sep)+'']),
						 endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											uvw=['R_ST_OUT*Cosd(60*'+str(i-1)+')', 'R_ST_OUT*Sind(60*'+str(i-1)+')', 'H_ST/2+'+str(sep)+'']))


	lastInstance = CompoundPath(name='HS_AX_TOP_'+str(i),
				 paths=[Path['PAX_TOP'+str(i)]],
				 color=Color['Turquoise'],
				 visibility=Visibility['VISIBLE'])

	cleanInvalidPaths()					 
				 
	PathStraightLine2PTS(name='PAX_BOTTOM'+str(i),
						 pathDiscretization=DistancePathDiscretization(distance=.5),
						 regionVolume='AIR',
						 color=Color['White'],
						 visibility=Visibility['VISIBLE'],
						 startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											  uvw=['(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Sind(60*'+str(i-1)+')', '-H_ST/2-'+str(sep)+'']),
						 endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
											uvw=['R_ST_OUT*Cosd(60*'+str(i-1)+')', 'R_ST_OUT*Sind(60*'+str(i-1)+')', '-H_ST/2-'+str(sep)+'']))


	lastInstance = CompoundPath(name='HS_AX_BOTTOM_'+str(i),
				 paths=[Path['PAX_BOTTOM'+str(i)]],
				 color=Color['Turquoise'],
				 visibility=Visibility['VISIBLE'])				 

	cleanInvalidPaths()

## for DISP
scenario='11_DISP_ANGLE'
folder='fields_2/'
for i in range(0,36): 				#for each DTHETA
	for j in range(0,6): 			#for each DTHETA_0, so as to follow structure for afterwards
		# select scenario... one should actually adjust this manually each time, depending on what one wants
		selectCurrentStep(activeScenario=Scenario[scenario],
						  parameterValue=['DTHETA='+str(i*10),										  
										  'DR_0=0.5',
										  'DTHETA_0='+str(j*60)])	
		# we now extract each hall sensor info
		for hs in range(1,7):
			#define name
			hr=scenario+'_HS_R_'+str(hs)+'_ANG_DTHETA_'+str(i*10)+'_ANG_DTHETA_0_'+str(j*60)
			#make curve
			SpatialCurve(name=hr,
					compoundPath=CompoundPath['HS_R_'+str(hs)],
					formula=['Comp(1,B)',
							 'Comp(2,B)',
							 'Comp(3,B)'])
			#save
			CurveSpatial2D[hr].exportExcel(xlsFile=folder+hr,
					mode='add')
					
			#define name
			hax_top=scenario+'_HS_AX_TOP_'+str(hs)+'_ANG_DTHETA_'+str(i*10)+'_ANG_DTHETA_0_'+str(j*60)
			#make curve		
			SpatialCurve(name=hax_top,
					compoundPath=CompoundPath['HS_AX_TOP_'+str(hs)],
					formula=['Comp(1,B)',
							 'Comp(2,B)',
							 'Comp(3,B)'])
			#save						 
			CurveSpatial2D[hax_top].exportExcel(xlsFile=folder+hax_top,
					mode='add')
			
			#define name
			hax_bottom=scenario+'_HS_AX_BOTTOM_'+str(hs)+'_ANG_DTHETA_'+str(i*10)+'_ANG_DTHETA_0_'+str(j*60)
			#make curve		
			SpatialCurve(name=hax_bottom,
					compoundPath=CompoundPath['HS_AX_BOTTOM_'+str(hs)],
					formula=['Comp(1,B)',
							 'Comp(2,B)',
							 'Comp(3,B)'])
			#save						 
			CurveSpatial2D[hax_bottom].exportExcel(xlsFile=folder+hax_bottom,
					mode='add')

scenario='01_DX'
folder='fields_displacements/'					
for i in range(1,6):	
	#beware of dots when using str function !!!
	if i*2<10:	
		selectCurrentStep(activeScenario=Scenario[scenario],
						  parameterValue=['DX=.'+str(i*2)])	
		print 'DX=.'+str(i*2)				  
	else:
		selectCurrentStep(activeScenario=Scenario[scenario],
						  parameterValue=['DX='+str(i/5)])			
		print 'DX=.'+str(i/5)
	for hs in range(1,7):
		#define name
		hr=scenario+'_HS_R_'+str(hs)+'_DX_'+str(200*i)+'um'
		#make curve
		SpatialCurve(name=hr,
				compoundPath=CompoundPath['HS_R_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save
		CurveSpatial2D[hr].exportExcel(xlsFile=folder+hr,
				mode='add')
				
		#define name
		hax_top=scenario+'_HS_AX_TOP_'+str(hs)+'_DX_'+str(200*i)+'um'
		#make curve		
		SpatialCurve(name=hax_top,
				compoundPath=CompoundPath['HS_AX_TOP_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save						 
		CurveSpatial2D[hax_top].exportExcel(xlsFile=folder+hax_top,
				mode='add')
		
		#define name
		hax_bottom=scenario+'_HS_AX_BOTTOM_'+str(hs)+'_DX_'+str(200*i)+'um'
		#make curve		
		SpatialCurve(name=hax_bottom,
				compoundPath=CompoundPath['HS_AX_BOTTOM_'+str(hs)],
				formula=['Comp(1,B)',
						 'Comp(2,B)',
						 'Comp(3,B)'])
		#save						 
		CurveSpatial2D[hax_bottom].exportExcel(xlsFile=folder+hax_bottom,
				mode='add')

scenario='08_DISP0_ANGLE'
folder='fields/'
for i in range(0,36): 				#for each DTHETA
	for j in range(0,1): 			#for each DTHETA_0, so as to follow structure for afterwards
		# select scenario... one should actually adjust this manually each time, depending on what one wants
		selectCurrentStep(activeScenario=Scenario[scenario],
						  parameterValue=['DTHETA='+str(i*10),										  
										  'DR_0=0.0',
										  'DTHETA_0='+str(j*60)])	
		# we now extract each hall sensor info
		for hs in range(1,7):
			#define name
			hr=scenario+'_HS_R_'+str(hs)+'_ANG_DTHETA_'+str(i*10)+'_ANG_DTHETA_0_'+str(j*60)
			#make curve
			SpatialCurve(name=hr,
					compoundPath=CompoundPath['HS_R_'+str(hs)],
					formula=['Comp(1,B)',
							 'Comp(2,B)',
							 'Comp(3,B)'])
			#save
			CurveSpatial2D[hr].exportExcel(xlsFile=folder+hr,
					mode='add')
					
			#define name
			hax_top=scenario+'_HS_AX_TOP_'+str(hs)+'_ANG_DTHETA_'+str(i*10)+'_ANG_DTHETA_0_'+str(j*60)
			#make curve		
			SpatialCurve(name=hax_top,
					compoundPath=CompoundPath['HS_AX_TOP_'+str(hs)],
					formula=['Comp(1,B)',
							 'Comp(2,B)',
							 'Comp(3,B)'])
			#save						 
			CurveSpatial2D[hax_top].exportExcel(xlsFile=folder+hax_top,
					mode='add')
			
			#define name
			hax_bottom=scenario+'_HS_AX_BOTTOM_'+str(hs)+'_ANG_DTHETA_'+str(i*10)+'_ANG_DTHETA_0_'+str(j*60)
			#make curve		
			SpatialCurve(name=hax_bottom,
					compoundPath=CompoundPath['HS_AX_BOTTOM_'+str(hs)],
					formula=['Comp(1,B)',
							 'Comp(2,B)',
							 'Comp(3,B)'])
			#save						 
			CurveSpatial2D[hax_bottom].exportExcel(xlsFile=folder+hax_bottom,
					mode='add')
				
				
CurveSpatial2D[ALL].HideCurve()					

