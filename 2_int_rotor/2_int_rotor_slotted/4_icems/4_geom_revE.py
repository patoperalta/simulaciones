#! Flux3D 12.0

#########################################################################################################################################################
## coordinate systems
#########################################################################################################################################################	

##revD was for candidacy exam
##revE is actually the same but with full rotor		  

##stator coordinate system
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['0',
                          '0',
                          '-h_st/2'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='0',
                                                angleZ='0'),
                  visibility=Visibility['VISIBLE'])

##rotor coordinate system			  
lastInstance = CoordSysCartesian(name='COORD_SYS_ROT',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['DX+DR_0*Cosd(DTHETA_0)',
                          'DY+DR_0*Sind(DTHETA_0)',
                          'DZ+Abs(ALPHA_H-1)*H_ST/2*X_H_DIFF'],
                  rotationAngles=RotationAngles(angleX='DALPHA',
                                                angleY='DBETA',
                                                angleZ='DTHETA'),
                  visibility=Visibility['VISIBLE'])	

#########################################################################################################################################################
## geometry points
#########################################################################################################################################################			  

## do slot
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-W_SLOT/2',
                      'Y2',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-W_SLOT/2',
                      'Y-L_SLOT',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['W_SLOT/2',
                      'Y-L_SLOT',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['W_SLOT/2',
                      'Y2',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

##middle points, where the stator ring comes				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-W_SLOT/2',
                      'Y',
                      '0'],
                 nature=Nature['STANDARD'])		

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['W_SLOT/2',
                      'Y',
                      '0'],
                 nature=Nature['STANDARD'])					 

##close slot
##straight sides
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[6]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[3]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[5]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[2]],
            nature=Nature['STANDARD'])

##inner slot radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[3],
                        Point[2]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##outer ring radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[4],
                        Point[1]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
			  
##build faces and define type of mesh
buildFaces()
# Face[1].meshGenerator=MeshGenerator['MAPPED']

##define type of transformation
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ST_60',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='60'))		

##and apply		
result = FaceAutomatic[1].propagate(transformation=Transf['ROT_ST_60'],
          repetitionNumber=5,
          buildingOption='FacesWithMeshGenerator',
          regionPropagation='Same')

##define arcs now	

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[36],
                        Point[4]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])



lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[35],
                        Point[6]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

## generate face again
buildFaces()
Face[7].meshGenerator=MeshGenerator['MAPPED']
## rotate
result = FaceAutomatic[7].propagate(transformation=Transf['ROT_ST_60'],
          repetitionNumber=5,
          buildingOption='FacesWithMeshGenerator',
          regionPropagation='Same')

##define vertical translation and extrude upwards

lastInstance = TransfTranslationVector(name='ST_H_ST',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'h_ST'])
								
result = FaceAutomatic[ALL].extrude(transformation=Transf['ST_H_ST'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

								
##rotor now
##rotor points
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

##rotor lines
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[76],
                      Point[75]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[75],
                      Point[74]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[74],
                      Point[73]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[73],
                      Point[76]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])
				 
## build faces
buildFaces()
## and make mapped faces				 
Face[75].meshGenerator=MeshGenerator['MAPPED']
##define transformation of rotational symmetry
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ROTOR',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))
##apply transformation
result = FaceAutomatic[75].extrude(transformation=Transf['ROT_ROTOR'],
        repetitionNumber=2,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')				 
##define axial transformation
lastInstance = TransfTranslationVector(name='AX_SIM_ROT',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-H_ROT/2'])
##now apply axial symmetry
result = Volume[13,14].propagateVolume(transformation=Transf['AX_SIM_ROT'],
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

FaceAutomatic[74].delete()
FaceAutomatic[73].delete()

buildVolumes()

