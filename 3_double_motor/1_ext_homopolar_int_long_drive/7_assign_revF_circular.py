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
Volume[1,9].assignRegion(region=RegionVolume['BNG_ST_PM_BOTTOM'])

Volume[2,10].assignRegion(region=RegionVolume['BNG_ST_IRON'])

Volume[3,11].assignRegion(region=RegionVolume['BNG_ST_PM_TOP'])

Volume[4,12].assignRegion(region=RegionVolume['DRV_ST_IRON'])

Volume[5,13].assignRegion(region=RegionVolume['BNG_ROT_PM_BOTTOM'])

Volume[6,14].assignRegion(region=RegionVolume['BNG_ROT_IRON'])

Volume[7,15].assignRegion(region=RegionVolume['BNG_ROT_PM_TOP'])

Volume[8,16].assignRegion(region=RegionVolume['DRV_ROT_PM'])

##assign air volumes
assignRegionToVolumes(volume=[Volume[17],
                              Volume[18],
                              Volume[19],
                              Volume[20],
                              Volume[21],
                              Volume[22],
                              Volume[23]],
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

#mesh details
#mesh things

# lastInstance = MeshLineArithmetic(name='BNG_R_ST',
                   # color=Color['White'],
                   # number=3)

# lastInstance = MeshLineArithmetic(name='BNG_R_ROT',
                   # color=Color['White'],
                   # number=3)

# lastInstance = MeshLineArithmetic(name='BNG_H_ST',
                   # color=Color['White'],
                   # number=4)

# lastInstance = MeshLineArithmetic(name='BNG_H_ROT',
                   # color=Color['White'],
                   # number=6)
				   
# lastInstance = MeshLineArithmetic(name='DRV_R_ROT',
                   # color=Color['White'],
                   # number=3)			
				   
# lastInstance = MeshLineArithmetic(name='DRV_R_ST',
                   # color=Color['White'],
                   # number=3)					   

# lastInstance = MeshLineArithmetic(name='DRV_H_ST',
                   # color=Color['White'],
                   # number=10)				   
				   
# lastInstance = MeshLineArithmetic(name='THETA',
                   # color=Color['White'],
                   # number=90)
				   
# lastInstance = MeshLineArithmetic(name='THETA_ROT',
                   # color=Color['White'],
                   # number=10)				   
				   

# LineSegment[13,12,11].assignMeshLine(meshLine=MeshLine['BNG_H_ROT'])

# LineSegment[3,2,1].assignMeshLine(meshLine=MeshLine['BNG_H_ST'])

# LineSegment[14].assignMeshLine(meshLine=MeshLine['BNG_R_ROT'])

# LineSegment[4].assignMeshLine(meshLine=MeshLine['BNG_R_ST'])

# LineSegment[21,25].assignMeshLine(meshLine=MeshLine['DRV_H_ST'])

# LineSegment[26].assignMeshLine(meshLine=MeshLine['DRV_R_ROT'])        

# LineSegment[22].assignMeshLine(meshLine=MeshLine['DRV_R_ST'])			   

# Line[74,99].assignMeshLine(meshLine=MeshLine['THETA_ROT'])
