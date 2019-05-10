#! Flux2D 18.1
##stator coordinate system
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['0',
                          '0'],
                  rotationAngles=RotationAngles(angleZ='0'),
                  visibility=Visibility['VISIBLE'])

##rotor coordinate system			  
lastInstance = CoordSysCartesian(name='COORD_SYS_ROT',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['DX+DR_0*Cosd(DTHETA_0)',
                          'DY+DR_0*Sind(DTHETA_0)'],
                  rotationAngles=RotationAngles(angleZ='DTHETA'),
                  visibility=Visibility['VISIBLE'])
				  
##rotor outer points
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_OUT',
                      '0'],
                 nature=Nature['STANDARD'])
				 
##coil inner point
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ROT_OUT+D_MECHGAP',
                      '0'],
                 nature=Nature['STANDARD'])				 
				 			 				 
##stator inner 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])				 
				 
##stator outer
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_OUT',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])		

##transformations to extrude 
##now repeate coil
lastInstance = TransfRotation3AnglesPivotCoord(name='PROP_ST',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0'],
                                rotationAngles=RotationAngles(angleZ='60'))
								
lastInstance = TransfRotation3AnglesPivotCoord(name='PROP_ROT',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0'],
                                rotationAngles=RotationAngles(angleZ='60'))		

## close the circles, that now has six segments
result = PointCoordinates[1].extrude(transformation=Transf['PROP_ROT'],
        repetitionNumber=6,
        extrusionType='standard')

result = PointCoordinates[2,3,4].extrude(transformation=Transf['PROP_ST'],
        repetitionNumber=6,
        extrusionType='standard')
								
##separate the coils
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[2],
                      Point[3]],
            nature=Nature['STANDARD'])

result = LineSegment[25].propagate(transformation=Transf['PROP_ST'],
          repetitionNumber=6)

##infinitebox
lastInstance = InfiniteBoxDisc(DISCOID=['3*r_st_out',
                         '4*r_st_out'])			 
						 
##faces							  
buildFaces() 
							
InfiniteBoxDisc['InfiniteBoxDisc'].setInvisible()							