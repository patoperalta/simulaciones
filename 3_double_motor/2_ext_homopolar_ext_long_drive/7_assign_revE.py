#! Flux3D 18.1
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
lastInstance = RegionVolume(name='DRV_ROT_PM_R_1',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='DRV_ROT_PM_R_2',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='DRV_ROT_PM_R_3',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='DRV_ROT_PM_R_4',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='DRV_ROT_IRON_D',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])			 
			 
##drive stator
lastInstance = RegionVolume(name='DRV_ST_IRON_D',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])


##assign motor volumes
##assign volumes		

Volume[1].assignRegion(region=RegionVolume['BNG_ST_IRON'])

Volume[2].assignRegion(region=RegionVolume['BNG_ST_PM_BOTTOM'])

Volume[4].assignRegion(region=RegionVolume['BNG_ST_PM_TOP'])

Volume[5].assignRegion(region=RegionVolume['BNG_ROT_PM_TOP'])

Volume[6].assignRegion(region=RegionVolume['BNG_ROT_IRON'])

Volume[7].assignRegion(region=RegionVolume['BNG_ROT_PM_BOTTOM'])

Volume[8].assignRegion(region=RegionVolume['DRV_ROT_IRON_D'])

Volume[9].assignRegion(region=RegionVolume['DRV_ROT_PM_R_1'])

Volume[10].assignRegion(region=RegionVolume['DRV_ROT_PM_R_2'])

Volume[11].assignRegion(region=RegionVolume['DRV_ROT_PM_R_3'])

Volume[12].assignRegion(region=RegionVolume['DRV_ROT_PM_R_4'])

Volume[13].assignRegion(region=RegionVolume['DRV_ST_IRON_D'])



##for air
assignRegionToVolumes(volume=[Volume[3],
                              Volume[14],
                              Volume[15],
                              Volume[16],
                              Volume[17],
                              Volume[18],
                              Volume[19]],
                      region=RegionVolume['AIR'])

##orient radial magnets
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_1'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_2'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='270')
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_3'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='180')
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_4'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='90')		 

## orient vertical pms of bearing stator
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_TOP'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',center=['0','0','0'],angle='0')
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',angle='180')

## orient vertical pms of bearing rotor
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_TOP'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',center=['0','0','0'],angle='180')
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',angle='0')
#########################################################################################################################################################			  
##appeareance
#########################################################################################################################################################	   
##change colors
RegionVolume['DRV_ROT_IRON_D','BNG_ST_IRON','DRV_ST_IRON_D'].color=Color['Black']

RegionVolume['BNG_ST_PM_BOTTOM','BNG_ROT_PM_TOP','DRV_ROT_PM_R_1','DRV_ROT_PM_R_3'].color=Color['Red']

RegionVolume['BNG_ST_PM_TOP','BNG_ROT_PM_BOTTOM','DRV_ROT_PM_R_2','DRV_ROT_PM_R_4'].color=Color['Green']

RegionVolume['AIR'].setInvisible()