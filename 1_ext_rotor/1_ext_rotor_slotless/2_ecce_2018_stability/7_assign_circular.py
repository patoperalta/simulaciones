#! Flux3D 12.0
############################			  
##assign
#########################################################################################################################################################	   
##definitions
lastInstance = RegionVolume(name='IRON_ROT',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='IRON_ST',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])			 

lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM1',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM2',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM3',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM4',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

## change volume colors
## iron stator
Volume[21,43,22,44].color=Color['Black']

## iron rotor
Volume[1,3,4,5,6,7,8,9,10,11,12,2,28,27,25,26,23,24,33,34,31,32,29,30].color=Color['Black']

## pm1
Volume[36,14,35,13].color=Color['Red']

## pm3
Volume[38,16,41,19].color=Color['Red']

## pm2
Volume[39,42,20,17].color=Color['Green']

## pm4
Volume[37,15,18,40].color=Color['Green']			 
			 
##assign motor volumes
Volume[21,43,22,44].assignRegion(region=RegionVolume['IRON_ST'])

Volume[1,3,4,5,6,7,8,9,10,11,12,2,28,27,25,26,23,24,33,34,31,32,29,30].assignRegion(region=RegionVolume['IRON_ROT'])

Volume[36,14,35,13].assignRegion(region=RegionVolume['PM1'])

Volume[37,15,18,40].assignRegion(region=RegionVolume['PM2'])

Volume[38,16,41,19].assignRegion(region=RegionVolume['PM3'])

Volume[39,42,20,17].assignRegion(region=RegionVolume['PM4'])

##for air
assignRegionToVolumes(volume=[Volume[45],
                              Volume[46],
                              Volume[47],
                              Volume[48],
                              Volume[49],
                              Volume[50],
                              Volume[51]],
                      region=RegionVolume['AIR'])


##orient material/magnets
orientRegVolMaterial(region=RegionVolume['PM1'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')
orientRegVolMaterial(region=RegionVolume['PM2'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='270')
orientRegVolMaterial(region=RegionVolume['PM3'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='180')
orientRegVolMaterial(region=RegionVolume['PM4'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='90')			 

##mesh things, same values as the int_rotor_slotless from 06.04
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=4)

lastInstance = MeshLineArithmetic(name='R_ROT',
                   color=Color['White'],
                   number=4)

lastInstance = MeshLineArithmetic(name='H_ST',
                   color=Color['White'],
                   number=5)

lastInstance = MeshLineArithmetic(name='H_ROT',
                   color=Color['White'],
                   number=8)
				   
theta_mag=80	##check this with params
			   
lastInstance = MeshLineArithmetic(name='THETA_MAG',
                   color=Color['White'],
                   number=int(45*theta_mag/90*1/2))				   
				   
lastInstance = MeshLineArithmetic(name='THETA_FE',
                   color=Color['White'],
                   number=int(45*(90-theta_mag)/90))
				   
## apply mesh things
Line[6,165].assignMeshLine(meshLine=MeshLine['H_ROT'])

LinePropagated[264,160].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[9,5,30,114,122,54,130,78].assignMeshLine(meshLine=MeshLine['R_ROT'])

LineSegment[1].assignMeshLine(meshLine=MeshLine['R_ST'])

LineExtruded[21,45,69,93].assignMeshLine(meshLine=MeshLine['THETA_FE'])

Line[53,61,77,85,101,13,29,37,138,117,143,125,148,133,109,104].assignMeshLine(meshLine=MeshLine['THETA_MAG'])