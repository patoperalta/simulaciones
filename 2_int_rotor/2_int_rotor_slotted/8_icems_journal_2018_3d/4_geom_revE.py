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

#########################################################################################################################################################
## geometry points
#########################################################################################################################################################			  

## do slot, radial in
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
                 uvw=['W_SLOT/2',
                      'Y2',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])				 

## slot, radial out
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

##inner slot radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[4],
                        Point[3]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##close slot
##straight sides
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[5]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[6]],
            nature=Nature['STANDARD'])

##outer ring radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[2],
                        Point[1]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##close sides
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[5]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[2]],
            nature=Nature['STANDARD'])
			
##inner stator radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[6],
                        Point[5]],
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
# result = Line[ALL].propagate(transformation=Transf['ROT_ST_60'],
          # repetitionNumber=5)
		  
result = FaceAutomatic[ALL].propagate(transformation=Transf['ROT_ST_60'],
          repetitionNumber=5,
          buildingOption='FacesWithMeshGenerator',
          regionPropagation='None')

##########################################################

##define outer arc now	
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[33],
                        Point[36]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
##separating point of coil
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['r_ST_IN',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])	 
##close the newest arcs
#rstin			  
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[21],
                        Point[37]],
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
#at coil
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[20],
                        Point[38]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
			  
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
              defPoint=[Point[38],
                        Point[23]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])		
#now really separate coil	
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[38],
                      Point[37]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])	  

## generate face again
buildFaces()
# Face[13,14].meshGenerator=MeshGenerator['MAPPED']
## rotate
result = FaceAutomatic[13,14,15].propagate(transformation=Transf['ROT_ST_60'],
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
            defPoint=[Point[97],
                      Point[100]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[100],
                      Point[99]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[99],
                      Point[98]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[98],
                      Point[97]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])
				 
## build faces
buildFaces()
FaceAutomatic[140].delete()
FaceAutomatic[139].delete()

## and make mapped faces				 
Face[141].meshGenerator=MeshGenerator['MAPPED']
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
result = FaceAutomatic[141].extrude(transformation=Transf['ROT_ROTOR'],
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
result = Volume[31,32].propagateVolume(transformation=Transf['AX_SIM_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

##now extend the coils even further up
lastInstance = TransfTranslationVector(name='H_COILS_PLUS',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'TH_COIL'])
								
lastInstance = TransfTranslationVector(name='H_COILS_MINUS',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                '-TH_COIL'])								
##up
result = FaceAutomatic[97,91,64].extrude(transformation=Transf['H_COILS_PLUS'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Volumes')
##down
result = FaceAutomatic[14,7,16].extrude(transformation=Transf['H_COILS_MINUS'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Volumes')
#propagate
result = Volume[35,37,36,38,39,40].propagateVolume(transformation=Transf['ROT_ST_60'],
                repetionNumber=5,
                buildingOption='Volumes',
                regionPropagation='None')		
#######################################################				
##domain
lastInstance = InfiniteBoxCylinderZ(size=['3*r_st_out',
                           '4*r_st_out',
                           '3*Max(H_ROT,H_ST)',
                           '4*Max(H_ROT,H_ST)'])          


buildFaces()  		

InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

FaceAutomatic[299].delete()
FaceAutomatic[298].delete()
FaceAutomatic[297].delete()
FaceAutomatic[300].delete()

buildVolumes()

CoordSys['COORD_SYS_ST'].rotationAngles=RotationAngles(angleX='0',
                                                       angleY='0',
                                                       angleZ='-30')
