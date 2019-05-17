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

Volume[33,34,31,32].assignRegion(region=RegionVolume['PM'])

##iron teeth
Volume[3,4,5,6,7,1].assignRegion(region=RegionVolume['IRON_ST'])

##steel backiron
Volume[26,2,27,8,28,9,29,10,30,11,15,12].assignRegion(region=RegionVolume['IRON_ST'])

##domain
assignRegionToVolumes(volume=[Volume[75],
                              Volume[76],
                              Volume[77],
                              Volume[74],
                              Volume[73],
                              Volume[71],							  
                              Volume[72]],
                      region=RegionVolume['AIR_DOMAIN'])
##coils

assignRegionToVolumes(volume=[Volume[35],
                              Volume[37],
                              Volume[36],
                              Volume[16],
                              Volume[14],
                              Volume[40],
                              Volume[39],
                              Volume[38]],
                      region=RegionVolume['COIL_1'])

assignRegionToVolumes(volume=[Volume[51],
                              Volume[46],
                              Volume[41],
                              Volume[21],
                              Volume[17],
                              Volume[66],
                              Volume[61],
                              Volume[56]],
                      region=RegionVolume['COIL_2'])

assignRegionToVolumes(volume=[Volume[42],
                              Volume[18],
                              Volume[67],
                              Volume[62],
                              Volume[57],
                              Volume[22],
                              Volume[52],
                              Volume[47]],
                      region=RegionVolume['COIL_3'])

assignRegionToVolumes(volume=[Volume[43],
                              Volume[48],
                              Volume[53],
                              Volume[23],
                              Volume[58],
                              Volume[63],
                              Volume[68],
                              Volume[19]],
                      region=RegionVolume['COIL_4'])

assignRegionToVolumes(volume=[Volume[44],
                              Volume[49],
                              Volume[54],
                              Volume[24],
                              Volume[59],
                              Volume[64],
                              Volume[69],
                              Volume[20]],
                      region=RegionVolume['COIL_5'])

assignRegionToVolumes(volume=[Volume[45],
                              Volume[50],
                              Volume[55],
                              Volume[25],
                              Volume[60],
                              Volume[65],
                              Volume[70],
                              Volume[13]],
                      region=RegionVolume['COIL_6'])

orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

## mapped slots and their backiron
#backiron
Volume[12,2,8,9,10,11].meshGenerator=MeshGenerator['MAPPED']
#slots	
Volume[3,1,7,6,5,4].meshGenerator=MeshGenerator['MAPPED']
#coil volume on top and under slots	
Volume[47,48,49,50,37,46,64,65,39,61,62,63].meshGenerator=MeshGenerator['MAPPED']
#coil sides, up and down
Volume[41,52,42,53,43,54,44,55,45,36,35,51,59,68,58,67,57,66,56,40,38,70,60,69].meshGenerator=MeshGenerator['MAPPED']
#coil sides at airgap height
Volume[21,16,17,22,18,23,19,24,20,25,13,14].meshGenerator=MeshGenerator['MAPPED']

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
LinePropagated[128,153,83,90,96,133,104,138,146,115,120,148].assignMeshLine(meshLine=MeshLine['R_ST'])

Line[207,213].assignMeshLine(meshLine=MeshLine['R_ROT'])

LineExtruded[152,127,88,82,95,132,103,137,111,142,119,147].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[212,208,206].assignMeshLine(meshLine=MeshLine['H_ROT'])

LineExtruded[211,215].assignMeshLine(meshLine=MeshLine['THETA_ROT'])

LinePropagated[201,202,203,204,164,200].assignMeshLine(meshLine=MeshLine['THETA_ST_ROUND_BI'])

LinePropagated[155,89,135,140,145,150,114,122,130,85,98,106].assignMeshLine(meshLine=MeshLine['THETA_ST_SLOT'])

   				   