##coordinate systems
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['0',
                          '0'],
                  rotationAngles=RotationAngles(angleZ='0'),
                  visibility=Visibility['VISIBLE'])

lastInstance = CoordSysCartesian(name='COORD_SYS_ROT',
                  parentCoordSys=Local(coordSys=CoordSys['XY1']),
                  origin=['DX+DR_0*Cosd(DTHETA_0)',
                          'DY+DR_0*Sind(DTHETA_0)'],
                  rotationAngles=RotationAngles(angleZ='DTHETA'),
                  visibility=Visibility['VISIBLE'])

##do slot
##x projection at outer stator radius
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-W_SLOT/2',
                      'Y2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['W_SLOT/2',
                      'Y2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])				 
##at airgap
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-W_SLOT/2',
                      'Y-L_SLOT'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['W_SLOT/2',
                      'Y-L_SLOT'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
				 
##at inner radius
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-W_SLOT/2',
                      'Y'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['W_SLOT/2',
                      'Y'],
                 nature=Nature['STANDARD'])     

##close the slot at the inner surface
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[4],
                        Point[3]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
			  
##close the slot at the lateral surface	
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[3]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[4]],
            nature=Nature['STANDARD'])  
			  
##close the outer stator	
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[2],
                        Point[1]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##propagate these surfaces 6 times
lastInstance = TransfRotation3AnglesPivotCoord(name='TRANSF_ST_60',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0'],
                                rotationAngles=RotationAngles(angleZ='60'))

result = Line[ALL].propagate(transformation=Transf['TRANSF_ST_60'],
          repetitionNumber=6)

##close outer stator
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[1],
                        Point[27]],
              nature=Nature['STANDARD'])
			  
result = LineArcRadius[25].propagate(transformation=Transf['TRANSF_ST_60'],
          repetitionNumber=6)			  

##close inner stator
##two points
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])				 
##radii upwards
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[38],
                        Point[15]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[37],
                        Point[26]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
##radii downwards
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[20],
                        Point[37]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[14],
                        Point[38]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
##separate coil
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[38],
                      Point[37]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])
##propagate	coils
result = Line[31,35,32,33,34].propagate(transformation=Transf['TRANSF_ST_60'],
          repetitionNumber=6)

##do rotor
##outer point
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_ROT_OUT',
                      '0'],
                 nature=Nature['STANDARD'])

##extrude point two times by 180°
lastInstance = TransfRotation3AnglesPivotCoord(name='TRANSF_ROT_180',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0'],
                                rotationAngles=RotationAngles(angleZ='180'))

result = PointCoordinates[49].extrude(transformation=Transf['TRANSF_ROT_180'],
        repetitionNumber=2,
        extrusionType='standard')

##generate infinite box		
lastInstance = InfiniteBoxDisc(DISCOID=['3*r_st_out',
                         '4*r_st_out'])			 
						 
buildFaces()

InfiniteBoxDisc['InfiniteBoxDisc'].setInvisible()						 