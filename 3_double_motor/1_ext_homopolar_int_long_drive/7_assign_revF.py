#! Flux3D 12.0
############################			  
##assign
#########################################################################################################################################################	   
##definitions


##bearing stator
lastInstance = RegionVolume(name='BNG_ST_PM_TOP',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='BNG_ST_PM_BOTTOM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='BNG_ST_IRON',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])			 

##bearing rotor			 
lastInstance = RegionVolume(name='BNG_ROT_IRON',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])			 
			 
lastInstance = RegionVolume(name='BNG_ROT_PM_TOP',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='BNG_ROT_PM_BOTTOM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])			 

##drive rotor
lastInstance = RegionVolume(name='DRV_ROT_PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])	 
			 
##drive stator
lastInstance = RegionVolume(name='DRV_ST_IRON',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
##air
lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])


##assign motor volumes	
Volume[1].assignRegion(region=RegionVolume['BNG_ST_IRON'])

Volume[2].assignRegion(region=RegionVolume['BNG_ST_PM_BOTTOM'])

Volume[4].assignRegion(region=RegionVolume['BNG_ST_PM_TOP'])

Volume[5].assignRegion(region=RegionVolume['BNG_ROT_PM_TOP'])

Volume[6].assignRegion(region=RegionVolume['BNG_ROT_IRON'])

Volume[7].assignRegion(region=RegionVolume['BNG_ROT_PM_BOTTOM'])

Volume[8].assignRegion(region=RegionVolume['DRV_ST_IRON'])

Volume[9].assignRegion(region=RegionVolume['DRV_ROT_PM'])

##assign air volumes
assignRegionToVolumes(volume=[Volume[3],
                              Volume[10],
                              Volume[11],
                              Volume[12],
                              Volume[13],
                              Volume[14],
                              Volume[15]],
                      region=RegionVolume['AIR'])

## orient vertical pms of bearing stator
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_TOP'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',center=['0','0','0'],angle='0')
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',angle='180')

## orient vertical pms of bearing rotor
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_TOP'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',center=['0','0','0'],angle='180')
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',angle='0')

## diametral magnetization drive
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

#########################################################################################################################################################			  
##appeareance
#########################################################################################################################################################	   
##change colors
RegionVolume['BNG_ROT_PM_BOTTOM','BNG_ST_PM_TOP'].color=Color['Red']

RegionVolume['BNG_ROT_PM_TOP','BNG_ST_PM_BOTTOM'].color=Color['Green']

RegionVolume['BNG_ROT_IRON','BNG_ST_IRON','DRV_ST_IRON'].color=Color['Black']

RegionVolume['DRV_ROT_PM'].color=Color['Cyan']

RegionVolume['AIR'].setInvisible()