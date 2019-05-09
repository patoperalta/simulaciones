#! Flux3D 12.0
#########################################################################################################################################################
##assign
#########################################################################################################################################################			 	

##made for geometry revE!!!
## changed a little for disc rotor

lastInstance = RegionVolume(name='IRON_ST',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])			 
			 
Volume[1,8,2,9,3,10,4,11,5,12,6,7].assignRegion(region=RegionVolume['IRON_ST'])

Volume[13,15,16,14].assignRegion(region=RegionVolume['PM'])

assignRegionToVolumes(volume=[Volume[17],
                              Volume[18],
                              Volume[19],
                              Volume[20],
                              Volume[21],
                              Volume[22],
                              Volume[23]],
                      region=RegionVolume['AIR'])


orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

RegionVolume['IRON_ST'].color=Color['Black']

RegionVolume['PM'].color=Color['Red']

##mesh things
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=4)

lastInstance = MeshLineArithmetic(name='R_ROT',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ST',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ROT',
                   color=Color['White'],
                   number=6)
				   
lastInstance = MeshLineArithmetic(name='THETA_ROT',
                   color=Color['White'],
                   number=90)
				   
lastInstance = MeshLineArithmetic(name='THETA_ST',
                   color=Color['White'],
                   number=15)				   
				   
LinePropagated[139,148].assignMeshLine(meshLine=MeshLine['H_ROT'])

LineExtruded[109].assignMeshLine(meshLine=MeshLine['H_ST'])

LineSegment[134].assignMeshLine(meshLine=MeshLine['R_ROT'])

LinePropagated[63,65,69,71,75,77,81,83,89,87,95,93,101,99,107,105,111,113,117,119,53,57,59,51].assignMeshLine(meshLine=MeshLine['R_ST']) ##up

# LinePropagated[63,71,75,83,87,95,99,107,111,119,59,51].assignMeshLine(meshLine=MeshLine['R_ST']) ##up

Line[32,35,34,31,28,29,25,26,22,23,20,19,16,14,13,17,10,11,7,8,1,2,3,4].assignMeshLine(meshLine=MeshLine['R_ST']) ##down

# Line[35,31,29,25,23,19,13,17,11,7,1,3].assignMeshLine(meshLine=MeshLine['R_ST']) ##down

LineExtruded[138,143].assignMeshLine(meshLine=MeshLine['THETA_ROT'])

LinePropagated[124,126,128,130,132,122,121,123,125,127,129,131].assignMeshLine(meshLine=MeshLine['THETA_ST'])	##up

Line[37,48,46,44,42,40,39,38,47,45,43,41].assignMeshLine(meshLine=MeshLine['THETA_ST']) ##down

			   