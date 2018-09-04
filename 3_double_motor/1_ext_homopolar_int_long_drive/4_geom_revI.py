#! Flux3D 12.0

##COORDINATE SYSTEMS
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['0',
                          '0',
                          '-H_B_ST/2*0'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='0',
                                                angleZ='0'),
                  visibility=Visibility['VISIBLE'])	
##rotor coordinate system			  
lastInstance = CoordSysCartesian(name='COORD_SYS_ROT',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['DX+DR_0*Cosd(DTHETA_0)',
                          'DY+DR_0*Sind(DTHETA_0)',
                          'DZ+Abs(ALPHA_H-1)*H_B_ST/2*X_H_DIFF'],
                  rotationAngles=RotationAngles(angleX='DALPHA',
                                                angleY='DBETA',
                                                angleZ='DTHETA'),
                  visibility=Visibility['VISIBLE'])	

## coordinate systems for vertical pms from stator
lastInstance = CoordSysCartesian(name='COORD_SYS_ST_VERT',
                  parentCoordSys=Local(coordSys=CoordSys['COORD_SYS_ST']),
                  origin=['0',
                          '0',
                          '0'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='-90',
                                                angleZ='0'),
                  visibility=Visibility['VISIBLE'])	

## coordinate systems for vertical pms from rotor
lastInstance = CoordSysCartesian(name='COORD_SYS_ROT_VERT',
                  parentCoordSys=Local(coordSys=CoordSys['COORD_SYS_ROT']),
                  origin=['0',
                          '0',
                          '0'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='-90',
                                                angleZ='0'),
                  visibility=Visibility['VISIBLE']) 				  

##start with stator				  
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_B_ST_OUT',
                      '0',
                      '-H_FE_ST_B/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_B_ST_OUT',
                      '0',
                      '-H_FE_ST_B/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_B_ST_OUT+d_st_b',
                      '0',
                      '-H_FE_ST_B/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_B_ST_OUT-D_ST_B',
                      '0',
                      '-H_FE_ST_B/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT',
              defPoint=[Point[1],
                        Point[2]],
              nature=Nature['STANDARD'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT',
              defPoint=[Point[2],
                        Point[1]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT-d_st_b',
              defPoint=[Point[4],
                        Point[3]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT-D_ST_B',
              defPoint=[Point[3],
                        Point[4]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = TransfTranslationVector(name='H_FE_ST_B',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'H_FE_ST_B'])
			    
## DO STATOR IRON POINTS				
result = LineArcRadius[1,2,3,4].extrude(transformation=Transf['H_FE_ST_B'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')

## DO STATOR PM RING TOP POINTS
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_B_ST_OUT-D_ST_B',
                      '0',
                      'H_B_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_B_ST_OUT-D_ST_B)',
                      '0',
                      'H_B_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_B_ST_OUT-0*D_ST_B',
                      '0',
                      'H_B_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_B_ST_OUT-0*D_ST_B)',
                      '0',
                      'H_B_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
				 
# lastInstance = PointCoordinates(color=Color['White'],
                 # visibility=Visibility['VISIBLE'],
                 # coordSys=CoordSys['COORD_SYS_ST'],
                 # uvw=['-(R_B_ST_OUT-D_ST_B+D_PM_B_ST)',
                      # '0',
                      # 'H_B_ST/2-H_PM_ST_B'],
                 # nature=Nature['STANDARD'],
                 # mesh=MeshPoint['AIDED_MESHPOINT'])

# lastInstance = PointCoordinates(color=Color['White'],
                 # visibility=Visibility['VISIBLE'],
                 # coordSys=CoordSys['COORD_SYS_ST'],
                 # uvw=['(R_B_ST_OUT-D_ST_B+D_PM_B_ST)',
                      # '0',
                      # 'H_B_ST/2-H_PM_ST_B'],
                 # nature=Nature['STANDARD'],
                 # mesh=MeshPoint['AIDED_MESHPOINT'])				 

## CLOSE TOP OF PM				 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_B_ST_OUT-0*D_ST_B)',
              defPoint=[Point[12],
                        Point[11]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_B_ST_OUT-0*D_ST_B)',
              defPoint=[Point[11],
                        Point[12]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_B_ST_OUT-D_ST_B)',
              defPoint=[Point[9],
                        Point[10]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_B_ST_OUT-D_ST_B)',
              defPoint=[Point[10],
                        Point[9]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[10],
                      Point[12]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[12],
                      Point[6]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[8]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[8],
                      Point[10]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[2]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])			  
			
##do lower stator bearing magnet	
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_B_ST_OUT-D_ST_B',
                      '0',
                      '-H_B_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_B_ST_OUT-D_ST_B)',
                      '0',
                      '-H_B_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_B_ST_OUT-0*D_ST_B)',
                      '0',
                      '-H_B_ST/2-H_PM_ST_B*0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['(R_B_ST_OUT-0*D_ST_B)',
                      '0',
                      '-H_B_ST/2-H_PM_ST_B*0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])		
				 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT-0*D_ST_B',
              defPoint=[Point[15],
                        Point[16]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT-0*D_ST_B',
              defPoint=[Point[16],
                        Point[15]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT-D_ST_B',
              defPoint=[Point[13],
                        Point[14]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_B_ST_OUT-D_ST_B',
              defPoint=[Point[14],
                        Point[13]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

##close pm stator under
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[2],
                      Point[15]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[15],
                      Point[14]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[14],
                      Point[3]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

##start with bearing rotor			  
######################################################

## upper pm, bearing rotor
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_B_PM_ROT_OUT',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_B_PM_ROT_OUT',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'])				 

## outer perimeter 			 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_B_PM_ROT_OUT',
              defPoint=[Point[17],
                        Point[18]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_B_PM_ROT_OUT',
              defPoint=[Point[18],
                        Point[17]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])	
				 		  
## inner perimeter points			  
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_B_PM_ROT_OUT-D_PM_B_ROT',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_B_PM_ROT_OUT+D_PM_B_ROT',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])			  

## inner perimeter 				 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_B_PM_ROT_OUT-D_PM_B_ROT',
              defPoint=[Point[19],
                        Point[20]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_B_PM_ROT_OUT-D_PM_B_ROT',
              defPoint=[Point[20],
                        Point[19]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

## bearing pm rotor tranlation definition				 
lastInstance = TransfTranslationVector(name='H_PM_ROT_B',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-H_PM_ROT_B/1'])

result = LineArcRadius[29,30,31,32].extrude(transformation=Transf['H_PM_ROT_B'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')	
		
## now define the translation for the rotor iron		
lastInstance = TransfTranslationVector(name='H_FE_ROT_B',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-H_FE_ROT_B/1'])
								
result = LineArcRadius[35,36,39,40].extrude(transformation=Transf['H_FE_ROT_B'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')									

## now extrude lower magnet !!!
result = LineArcRadius[43,44,47,48].extrude(transformation=Transf['H_PM_ROT_B'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')	
		
#########################################################################
## start doing drive rotor
## outer stator points
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_DRV_ST_OUT',
                      '0',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_DRV_ST_OUT',
                      '0',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
#close with radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_DRV_ST_OUT',
              defPoint=[Point[33],
                        Point[34]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_DRV_ST_OUT',
              defPoint=[Point[34],
                        Point[33]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

#inner radius of drive stator
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_DRV_ST_OUT-D_DRV_ST',
                      '0',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_DRV_ST_OUT+D_DRV_ST',
                      '0',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])			  
##close inner radius
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_DRV_ST_OUT-D_DRV_ST',
              defPoint=[Point[35],
                        Point[36]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_DRV_ST_OUT-D_DRV_ST',
              defPoint=[Point[36],
                        Point[35]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

#extrude drv stator			  
lastInstance = TransfTranslationVector(name='H_FE_ST_DRV',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'H_DRV'])

result = LineArcRadius[59,57,60,58].extrude(transformation=Transf['H_FE_ST_DRV'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')

#########################################################################		
#now draw drive rotor

#border points
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_DRV_ROT_OUT',
                      '0',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

				 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_DRV_ROT_OUT',
                      '0',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
								
#close radii
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_DRV_ROT_OUT',
              defPoint=[Point[41],
                        Point[42]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_DRV_ROT_OUT',
              defPoint=[Point[42],
                        Point[41]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

#extrude drv rotor		
lastInstance = TransfTranslationVector(name='H_PM_ROT_DRV',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                'H_DRV'])

result = LineArcRadius[69,70].extrude(transformation=Transf['H_PM_ROT_DRV'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')	  
		
##close bearing stator		
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[11],
                      Point[5]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[16]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[13]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[9],
                      Point[7]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])	

##close bearing rotor
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[18],
                      Point[20]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[22],
                      Point[24]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[26],
                      Point[28]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[30],
                      Point[32]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

##	close drive stator
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[40],
                      Point[38]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[36],
                      Point[34]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])
			
## build infinte box
lastInstance = InfiniteBoxCylinderZ(size=['3*R_B_ST_OUT',
                           '4*R_B_ST_OUT',
                           '3*Max(H_ROT,H_B_ST)',
                           '4*Max(H_ROT,H_B_ST)'])			
						   
## build faces
buildFaces()
			   
## invisible cylinder
InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()	

## erase strange airgap faces
FaceAutomatic[19].delete()
FaceAutomatic[15].delete()
FaceAutomatic[6].delete()
FaceAutomatic[23].delete()
FaceAutomatic[27].delete()
FaceAutomatic[34].delete()
FaceAutomatic[41].delete()
FaceAutomatic[46].delete()
FaceAutomatic[55].delete()
FaceAutomatic[50].delete()
		
## build the volumes		
buildVolumes()