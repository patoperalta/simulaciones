#! Flux3D 12.0
#########################################################################################################################################################
##assign
#########################################################################################################################################################			 	

lastInstance = RegionVolume(name='IRON_ST',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Black'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Red'],
             visibility=Visibility['VISIBLE'])			 
			 
Volume[1,3,5,6].assignRegion(region=RegionVolume['PM'])

Volume[2,4,7,8].assignRegion(region=RegionVolume['IRON_ST'])

assignRegionToVolumes(volume=[Volume[9],
                              Volume[10],
                              Volume[11],
                              Volume[12],
                              Volume[13],
                              Volume[14],
                              Volume[15]],
                      region=RegionVolume['AIR'])

orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

##mesh things
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=4)

lastInstance = MeshLineArithmetic(name='R_ROT',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ST : assigned for the half of the st height',
                   color=Color['White'],
                   number=3)

lastInstance = MeshLineArithmetic(name='H_ROT : assigned for the half of the rot height',
                   color=Color['White'],
                   number=5)
				   
lastInstance = MeshLineArithmetic(name='THETA',
                   color=Color['White'],
                   number=45)
				   
Line[8,21].assignMeshLine(meshLine=MeshLine['R_ST'])

Line[7,37].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[1,10].assignMeshLine(meshLine=MeshLine['R_ROT'])

Line[2,28].assignMeshLine(meshLine=MeshLine['H_ROT'])

Line[9,22,14,19,27,24].assignMeshLine(meshLine=MeshLine['THETA'])				   