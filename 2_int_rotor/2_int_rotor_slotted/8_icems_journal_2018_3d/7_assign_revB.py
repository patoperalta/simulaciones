#! Flux3D 12.0
#########################################################################################################################################################
##assign
#########################################################################################################################################################			 	

##made for geometry revE!!!
## changed a little for disc rotor

lastInstance = RegionVolume(name='IRON_ST',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Black'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='AIR_DOMAIN',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Magenta'],
             visibility=Visibility['VISIBLE'])		 

lastInstance = RegionVolume(name='PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Red'],
             visibility=Visibility['VISIBLE'])		
			 
for i in range(1,7):			 
	lastInstance = RegionVolume(name='COIL_'+str(i),
				 magneticDC3D=MagneticDC3DVolumeVacuum(),
				 color=Color['Magenta'],
				 visibility=Visibility['VISIBLE'])	
				 
# ##solid coils, which are not really needed...
# for i in range(1,7):
	# lastInstance = RegionVolume(name='COIL_'+str(i),
				 # magneticDC3D=MagneticDC3DVolumeCoilConductor(coilConductor=CoilConductor3D(turnNumber='1',
																							# seriesParallel=AllInSeries(),
																							# electricComponent=CoilConductor['I_'+str(i)],
																							# fillFactor='1'),
															  # material=Material['AIR']),
				 # color=Color['Red'],
				 # visibility=Visibility['INVISIBLE'])
			 
InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

Volume[38,37,40,39].assignRegion(region=RegionVolume['PM'])

##iron teeth
Volume[5,6,7,1,3,4].assignRegion(region=RegionVolume['IRON_ST'])
##steel backiron
Volume[12,27,32,2,28,33,8,29,34,9,30,35,10,31,11,15,16,36].assignRegion(region=RegionVolume['IRON_ST'])
##coils
Volume[57,52,47,22,18,62,67,72].assignRegion(region=RegionVolume['COIL_1'])

Volume[48,53,58,19,23,63,68,73].assignRegion(region=RegionVolume['COIL_2'])

Volume[49,54,59,20,24,74,69,64].assignRegion(region=RegionVolume['COIL_3'])

Volume[50,55,60,21,25,65,70,75].assignRegion(region=RegionVolume['COIL_4'])

Volume[51,56,61,13,26,66,71,76].assignRegion(region=RegionVolume['COIL_5'])

Volume[41,42,43,17,14,44,45,46].assignRegion(region=RegionVolume['COIL_6'])
##domain
assignRegionToVolumes(volume=[Volume[78],
                              Volume[80],
                              Volume[79],
                              Volume[82],
                              Volume[81],
                              Volume[83]],
                      region=RegionVolume['AIR_DOMAIN'])

assignRegionToVolumes(volume=[Volume[77]],
                      region=RegionVolume['AIR_DOMAIN'])

orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

##mesh things, meshed equivalently to slotless version
## see 
## C:\Users\jperalta\Documents\github_pato\flux\2_int_rotor\1_int_rotor_slotless\8_icems_journal_2018_3d\7_assign_circular.py
## from line 37
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=3)

lastInstance = MeshLineArithmetic(name='R_ROT',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ST : whole height',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ROT : whole height',
                   color=Color['White'],
                   number=10)
				   
lastInstance = MeshLineArithmetic(name='THETA_ROT',
                   color=Color['White'],
                   number=45)
				   
lastInstance = MeshLineArithmetic(name='THETA_ST_ROUND_BI : which is divided into almost 3 pieces',
                   color=Color['White'],
                   number=(45-9)/3)		   
				   
lastInstance = MeshLineArithmetic(name='THETA_ST_SLOT : coming out of slot',
                   color=Color['White'],
                   number=(9)/3)		

## assign lines
LinePropagated[165,216,103,102,219,148,145,222,153,150,225,158,155,228,163,160,177,168,264,269,291,329,296,299,334,304,307,339,312,315,344,320,323,349,259,255].assignMeshLine(meshLine=MeshLine['R_ST'])

Line[237,243].assignMeshLine(meshLine=MeshLine['R_ROT'])

LineExtruded[151,149,224,156,154,227,161,159,176,166,164,215,99,100,218,146,144,221,180,96,94,185,109,107,190,117,115,195,125,123,200,133,131,169,141,139,105,192,112,113,197,120,121,202,129,171,136,137,182,91,92,187,104].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[236,242].assignMeshLine(meshLine=MeshLine['H_ROT'])

LineExtruded[241,245].assignMeshLine(meshLine=MeshLine['THETA_ROT'])

LinePropagated[231,223,226,233,229,234,232,220,230,217,179,178].assignMeshLine(meshLine=MeshLine['THETA_ST_ROUND_BI'])

LinePropagated[101,147,152,157,162,167].assignMeshLine(meshLine=MeshLine['THETA_ST_SLOT'])