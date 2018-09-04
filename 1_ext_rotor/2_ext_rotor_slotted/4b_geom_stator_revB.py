#! Flux3D 12.0
## do stator geometry!

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['L_SLOT_OUT',
                      '-W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['L_SLOT_OUT',
                      'W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])


lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_sT_OUT',
              defPoint=[Point[1],
                        Point[2]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##points were stator teeth meet
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['(W_SLOT/2)/Tand(30)',
                      '-W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['(W_SLOT/2)/Tand(30)',
                      'W_SLOT/2',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

##transformation for tooth tip
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_TEETH',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='60'))

result = LineArcRadius[1].propagate(transformation=Transf['ROT_TEETH'],
          repetitionNumber=6)

result = PointCoordinates[4].propagate(transformation=Transf['ROT_TEETH'],
          repetitionNumber=4)

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[1]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[2]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

result = LineSegment[7,8].propagate(transformation=Transf['ROT_TEETH'],
          repetitionNumber=5)

##extrude upwards
lastInstance = TransfTranslationVector(name='ROT_H_ST',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'h_st'])

result = Line[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18].extrude(transformation=Transf['ROT_H_ST'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')

##turn stator so that it is similar to slotted motor           
CoordSys['COORD_SYS_ST'].rotationAngles=RotationAngles(angleX='0',
                                                       angleY='0',
                                                       angleZ='30')     


