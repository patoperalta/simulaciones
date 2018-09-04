#! Flux3D 12.0
############################			  
##assign
##########################################################################################################################

##create possible regions
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
			 
## colors to volumes
##iron stator
Volume[41].color=Color['Black']
#iron rotor
Volume[4,5,6,7,8,9,10,11,12,1,2,3,23,22,32,21,30,31,28,29,26,27,24,25].color=Color['Black']
##pm1
Volume[13,33,14,34].color=Color['Red']
##pm2
Volume[18,15,38,35].color=Color['Green']
##pm3
Volume[39,19,36,16].color=Color['Red']
##pm4
Volume[17,20,40,37].color=Color['Green']

			 
##assign regions to volumes
Volume[41].assignRegion(region=RegionVolume['IRON_ST'])

Volume[4,5,6,7,8,9,10,11,12,1,2,3,23,22,32,21,30,31,28,29,26,27,24,25].assignRegion(region=RegionVolume['IRON_ROT'])

Volume[13,33,14,34].assignRegion(region=RegionVolume['PM1'])

Volume[18,15,38,35].assignRegion(region=RegionVolume['PM2'])

Volume[39,19,36,16].assignRegion(region=RegionVolume['PM3'])

Volume[17,20,40,37].assignRegion(region=RegionVolume['PM4'])

##the rest, air
assignRegionToVolumes(volume=[Volume[42],
                              Volume[43],
                              Volume[44],
                              Volume[45],
                              Volume[46],
                              Volume[47],
                              Volume[48]],
                      region=RegionVolume['AIR'])

##orient magnets
orientRegVolMaterial(region=RegionVolume['PM1'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')
orientRegVolMaterial(region=RegionVolume['PM2'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='270')
orientRegVolMaterial(region=RegionVolume['PM3'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='180')
orientRegVolMaterial(region=RegionVolume['PM4'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='90')		

## mesh things
##mesh things
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=8)

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
LinePropagated[132,250].assignMeshLine(meshLine=MeshLine['H_ROT'])

LineExtruded[34].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[55,59,85,164,109,174,133,182].assignMeshLine(meshLine=MeshLine['R_ROT'])

LinePropagated[53].assignMeshLine(meshLine=MeshLine['R_ST'])

LineExtruded[75,99,123,147].assignMeshLine(meshLine=MeshLine['THETA_FE'])

Line[83,188,91,167,193,175,198,183,159,154,67,153,139,131,115,107].assignMeshLine(meshLine=MeshLine['THETA_MAG'])				   