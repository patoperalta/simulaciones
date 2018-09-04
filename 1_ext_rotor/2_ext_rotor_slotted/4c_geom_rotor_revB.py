#! Flux3D 12.0
# do rotor and its corresponding magnets
#inspired in the construction of the ext rotor slotless stator revC_circ
##rotor iron				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_OUT',
                      '0',
                      '0'],
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
                 uvw=['R_ROT_IN',
                      '0',
                      'H_ROT/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_IN',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

##rotor magnet				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_IN-D_MAG',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_IN-D_MAG',
                      '0',
                      'H_ROT/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

##close magnet from the side
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[42],
                      Point[39]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[39],
                      Point[40]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[40],
                      Point[41]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[41],
                      Point[42]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

##close rotor iron from the side			
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[39],
                      Point[38]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[38],
                      Point[37]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[37],
                      Point[40]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

## build faces to start defining their mesh
buildFaces()

FaceAutomatic[21,22].meshGenerator=MeshGenerator['MAPPED']

## now start with the extrusions
## define their transformations
## define the easy transformations
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_BTWN_MAGS_IRON : rotor iron pieces between magnets',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='90-THETA_MAG'))


lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ROT_MAG : extrude positively',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='THETA_MAG/2'))
															  
## extrude rotor iron each time... in order to avoid strange errors at the meshing process
result = FaceAutomatic[22].extrude(transformation=Transf['ROT_ROT_MAG'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[27].extrude(transformation=Transf['ROT_BTWN_MAGS_IRON'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[32].extrude(transformation=Transf['ROT_ROT_MAG'],
        repetitionNumber=2,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[42].extrude(transformation=Transf['ROT_BTWN_MAGS_IRON'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[47].extrude(transformation=Transf['ROT_ROT_MAG'],
        repetitionNumber=2,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[57].extrude(transformation=Transf['ROT_BTWN_MAGS_IRON'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[62].extrude(transformation=Transf['ROT_ROT_MAG'],
        repetitionNumber=2,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[72].extrude(transformation=Transf['ROT_BTWN_MAGS_IRON'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[77].extrude(transformation=Transf['ROT_ROT_MAG'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

## now, extrude and repeat 3 times the magnets		
## magnets	
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ROT_MAG_MIN : extrude positively',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='-THETA_MAG/2'))	

## same face, to both sides
result = FaceAutomatic[21].extrude(transformation=Transf['ROT_ROT_MAG'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[21].extrude(transformation=Transf['ROT_ROT_MAG_MIN'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')														  
															  
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_MAG_90',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='90'))			
															  
result = Volume[13,14].propagateVolume(transformation=Transf['ROT_MAG_90'],
                repetionNumber=3,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')														  
				
## now extrude downwards
## axial extrusion transformations
lastInstance = TransfTranslationVector(name='AX_ROT',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-h_ROT/2'])	

## extrude downwards
result = Volume[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20].propagateVolume(transformation=Transf['AX_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

								