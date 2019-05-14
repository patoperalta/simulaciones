#! Flux3D 12.0

#########################################################################################################################################################
## coordinate systems
#########################################################################################################################################################	

# rev C still has a hole in the middle

# rev D has no hole and corresponds to ICEMS optimization		  

##stator coordinate system
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['0',
                          '0',
                          '-h_st/2*0'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='0',
                                                angleZ='0'),
                  visibility=Visibility['VISIBLE']) 
				  
#rotor coordinate system for relative displacements		  
lastInstance = CoordSysCartesian(name='COORD_SYS_ROT',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['DX+DR_0*Cosd(DTHETA_0)',
                          'DY+DR_0*Sind(DTHETA_0)',
                          'DZ'],
                  rotationAngles=RotationAngles(angleX='DALPHA',
                                                angleY='DBETA',
                                                angleZ='DTHETA'),
                  visibility=Visibility['VISIBLE'])						  
#######################################################

##do all the points
##rotor
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['0',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['0',
                      '0',
                      'H_ROT/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_OUT',
                      '0',
                      'H_ROT/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_OUT',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

##stator				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN',
                      '0',
                      'H_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_OUT',
                      '0',
                      'H_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_OUT',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

#######################################################				 
## close points with lines
##rotor
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[2],
                      Point[3]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[4]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[1]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[2]],
            nature=Nature['STANDARD'])
##stator
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[5]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[8]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[8],
                      Point[7]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[7],
                      Point[6]],
            nature=Nature['STANDARD'])

#######################################################
## generate transformation
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ROTOR',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))

lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ST',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))

buildFaces()

FaceAutomatic[ALL].meshGenerator=MeshGenerator['MAPPED']

#######################################################
## apply transformation
result = FaceAutomatic[1].extrude(transformation=Transf['ROT_ROTOR'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[2].extrude(transformation=Transf['ROT_ST'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')
#######################################################
## define transformation

lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_SYM_ROT',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))
															  
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_SYM_ST',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))															  

lastInstance = TransfTranslationVector(name='AX_SIM_ROT',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-H_ROT/2'])

lastInstance = TransfTranslationVector(name='AX_SIM_ST',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                '-H_ST/2'])
															  
#######################################################
## apply transformation
result = Volume[1].propagateVolume(transformation=Transf['ROT_SYM_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')
				
result = Volume[2].propagateVolume(transformation=Transf['ROT_SYM_ST'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

result = Volume[1,3].propagateVolume(transformation=Transf['AX_SIM_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

result = Volume[2,4].propagateVolume(transformation=Transf['AX_SIM_ST'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

#######################################################				
##domain
lastInstance = InfiniteBoxCylinderZ(size=['3*r_st_out',
                           '4*r_st_out',
                           '5*Max(H_ROT,H_ST)',
                           '6*Max(H_ROT,H_ST)'])          


buildFaces()     

InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

FaceAutomatic[34].delete()
FaceAutomatic[33].delete()
FaceAutomatic[35].delete()

buildVolumes()

