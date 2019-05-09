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
				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_ROT_OUT',
                      '0'],
                 nature=Nature['STANDARD'])				 
				  				  
##stator inner and outer point	
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
                 uvw=['-R_ST_IN',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])				 

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_OUT',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])							  

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_ST_OUT',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])							  				 
				 
##close rotor
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_ROT_OUT',
              defPoint=[Point[1],
                        Point[2]],
              nature=Nature['STANDARD'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_ROT_OUT',
              defPoint=[Point[2],
                        Point[1]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##close stator
##outside
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[5],
                        Point[6]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[6],
                        Point[5]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
##inside	
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[3],
                        Point[4]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[4],
                        Point[3]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])			  			  

##infinitebox
lastInstance = InfiniteBoxDisc(DISCOID=['3*r_st_out',
                         '4*r_st_out'])			 
						 
##faces
# buildFaces()

# FaceAutomatic[2].delete()

##do coil
##outer point
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['r_ST_in-D_SPACE_STATOR_COIL',
                      '0'],
                 nature=Nature['STANDARD'])
##inner point
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN-D_SPACE_STATOR_COIL-(D_AGAP-D_MECHGAP)',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
##transformation to turn
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_COIL',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0'],
                                rotationAngles=RotationAngles(angleZ='59'))	

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[16],
                      Point[15]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])						

##extrude								
result = LineSegment[11].extrude(transformation=Transf['ROT_COIL'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')

##faces								

buildFaces()

FaceAutomatic[2].delete()	

##now repeate coil
lastInstance = TransfRotation3AnglesPivotCoord(name='PROP_COIL',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0'],
                                rotationAngles=RotationAngles(angleZ='60'))
								
result = FaceAutomatic[6].propagate(transformation=Transf['PROP_COIL'],
          repetitionNumber=5,
          buildingOption='Faces',
          regionPropagation='None')		
		  
buildFaces() 
							
InfiniteBoxDisc['InfiniteBoxDisc'].setInvisible()							