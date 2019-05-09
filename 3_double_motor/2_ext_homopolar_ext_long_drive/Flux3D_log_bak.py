#! Flux3D 18.1
newProject()

GeomMeshOptions[1].methodAutomaticMeshVolume=OptimizeMeshGemsActivated(level=OptimizationStandard())

openModelerContext()

#! Flux3D 18.1


print("FICHIER PARAM.PY\n")
##################################################################################################################################################################
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## define the motor by the radius of bearing pm
# lastInstance = ParameterGeom(name='R_OUT_PM_ROT_BNG : outer radius of rotor bearing pm',
              # expression='10')
lastInstance = ParameterGeom(name='R_OUT_PM_ROT_BNG : outer radius of rotor bearing pm',
              expression='10')                 

##now, define the airgap and the stator thickness, then we know the total radius of the motor
lastInstance = ParameterGeom(name='D_AGAP_B : bearing air gap',
              expression='1.5')
                 
lastInstance = ParameterGeom(name='D_ST_BNG : radial thickness of bearing stator and its PMs',
              expression='1')                      
                 
##PARAMETERS FOR BEARING STATOR
lastInstance = ParameterGeom(name='R_OUT_ST_BNG : outer radius of bearing stator',
              expression='R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG')

lastInstance = ParameterGeom(name='D_MOT : diameter of whole motor magnetics',
              expression='2*R_OUT_ST_BNG')

##rotor height and diameter parameters                 
lastInstance = ParameterGeom(name='ALPHA_H : ratio H_ROT_B/H_ST_BNG',
              expression='1.8')

lastInstance = ParameterGeom(name='ALPHA_CASE : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = ParameterGeom(name='beta_b : times total diameter gives away motor height if alpha_h <= 1',
              expression='.2')
                 
lastInstance = ParameterGeom(name='beta_d : times total diameter gives away motor height if alpha_h <= 1',
              expression='.5')                 

lastInstance = ParameterGeom(name='H_DRV : total drive height',
              expression='d_mot*beta_d')                 
                 
## height of the bearing stator                 
lastInstance = ParameterGeom(name='H_ST_BNG : bearing stator height, f(dmot,alpha,beta_b) ',
              expression='D_MOT*(ALPHA_CASE*beta_b+(1-ALPHA_CASE)*beta_b/ALPHA_H)')

##total height of pms in bearing stator, that it, each pm has the half of this percentage                 
lastInstance = ParameterGeom(name='H_PERCENT_PM_TO_FE_BNG_ST : %(h of pm  / total height) of stator bearing',
              expression='.6')                   

##each pm with half the height
lastInstance = ParameterGeom(name='H_PM_BNG_ST : actual height of each pm of bearing stator',
              expression='H_PERCENT_PM_TO_FE_BNG_ST*H_ST_BNG/2')
                 
##total iron                 
lastInstance = ParameterGeom(name='H_FE_BNG_ST : iron height of bearing stator ',
              expression='H_ST_BNG-2*H_PM_BNG_ST')                 

##start with rotor                 
lastInstance = ParameterGeom(name='H_ROT_B : rotor height',
              expression='d_mot*(alpha_case*alpha_h*beta_b+(1-alpha_case)*beta_b)')
                             
lastInstance = ParameterGeom(name='D_PM_B_ROT : thickness of rotor bearing pm',
              expression='1')     

##amount of pm and fe in bearing rotor
lastInstance = ParameterGeom(name='H_PERCENT_PM_TO_FE_BNG_ROT : %(h of pm  / total height) of rotor of bearing',
              expression='0.8')

lastInstance = ParameterGeom(name='H_FE_ROT_B : iron height of rotor of bearing',
              expression='H_ROT_B*(1-H_PERCENT_PM_TO_FE_BNG_ROT)')

lastInstance = ParameterGeom(name='H_PM_ROT_B : iron height of rotor of bearing',
              expression='H_ROT_B*H_PERCENT_PM_TO_FE_BNG_ROT/2')                 
                 
##PARAMETERS FOR ROTOR DISPLACEMENT
lastInstance = ParameterGeom(name='DTHETA',
              expression='0')

lastInstance = ParameterGeom(name='DALPHA',
              expression='0')

lastInstance = ParameterGeom(name='DBETA',
              expression='0')

lastInstance = ParameterGeom(name='DX',
              expression='0')

lastInstance = ParameterGeom(name='DY',
              expression='0')

lastInstance = ParameterGeom(name='X_H_DIFF : abs val of height dif between st and rot',
              expression='0')                 
                 
lastInstance = ParameterGeom(name='DZ',
              expression='0')     

lastInstance = ParameterGeom(name='DR_0',
              expression='0')

lastInstance = ParameterGeom(name='DTHETA_0',
              expression='0')                      

##DRIVE MOTOR     
##separation between inner radius of bearing rotor and outer radius of drive rotor
lastInstance = ParameterGeom(name='R_SEP : separation between rotor bearing magnet and drive iron',
              expression='1.5')     

lastInstance = ParameterGeom(name='R_DR_ROT_OUT : outer radius of drive rotor',
              expression='(R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP)')

##iron                 
lastInstance = ParameterGeom(name='K_D_DR_FE_ROT : prop constant, radial thickness of drive iron in rotor',
              expression='(1.1/(13/2))')
                 
lastInstance = ParameterGeom(name='D_DR_FE_ROT : radial thickness of drive iron in rotor',
              expression='K_D_DR_FE_ROT*R_DR_ROT_OUT')                 

##pm                 
lastInstance = ParameterGeom(name='K_D_DR_PM : constant for radial thickness of drive pms ',
              expression='1/7.5')     
                 
lastInstance = ParameterGeom(name='D_DR_PM : radial thickness of pms of drive',
              expression='R_DR_ROT_OUT*K_D_DR_PM')     

##airgap                 
lastInstance = ParameterGeom(name='D_AGAP_D : drive airgap',
              expression='.75')
                 
lastInstance = ParameterGeom(name='theta_mag : angular width of drive pms',
              expression='60')                      

##slotted stator of drive

ParameterGeom(name='R_DR_ST_OUT : outer radius of stator',
              expression='R_DR_ROT_OUT-D_DR_FE_ROT-D_DR_PM-D_AGAP_D')
                 
ParameterGeom(name='K_W_SLOT',
              expression='2/7.5')

ParameterGeom(name='W_SLOT',
              expression='K_W_SLOT*R_DR_ROT_OUT')                      
                 
lastInstance = ParameterGeom(name='L_SLOT_OUT : outer flank of slot',
              expression='Sqrt(R_DR_ST_OUT^2-(W_SLOT/2)^2)')                      

#! Flux3D 18.1

#########################################################################################################################################################
##define application
#########################################################################################################################################################                 
lastInstance = ApplicationMagneticDC3D(formulationModel=MagneticDC3DAutomatic(),
                        scalarVariableOrder=ScalarVariableAutomaticOrder(),
                        vectorNodalVariableOrder=VectorNodalVariableAutomaticOrder(),
                        coilCoefficient=CoilCoefficientAutomatic())     

closeModelerContext()

#! Flux3D 18.1

# Pour pouvoir mailler plus petit
# GeomMeshOptions[1].meshRelativeEpsilon = 1.0E-7
     

AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.9)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowUnassigned())                       

#! Flux3D 18.1

##COORDINATE SYSTEMS
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['0',
                          '0',
                          '-H_ST_BNG/2*0'],
                  rotationAngles=RotationAngles(angleX='0',
                                                angleY='0',
                                                angleZ='30'),
                  visibility=Visibility['VISIBLE'])     
#rotated in 30° degrees so drive stator looks nicer ...                      
##rotor coordinate system                 
lastInstance = CoordSysCartesian(name='COORD_SYS_ROT',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['DX+DR_0*Cosd(DTHETA_0)',
                          'DY+DR_0*Sind(DTHETA_0)',
                          'DZ+Abs(ALPHA_H-1)*H_ST_BNG/2*X_H_DIFF'],
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
                 uvw=['R_OUT_ST_BNG',
                      '0',
                      '-H_FE_BNG_ST/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_OUT_ST_BNG',
                      '0',
                      '-H_FE_BNG_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-R_OUT_ST_BNG+D_ST_BNG',
                      '0',
                      '-H_FE_BNG_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_OUT_ST_BNG-D_ST_BNG',
                      '0',
                      '-H_FE_BNG_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG',
              defPoint=[Point[1],
                        Point[2]],
              nature=Nature['STANDARD'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG',
              defPoint=[Point[2],
                        Point[1]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG-D_ST_BNG',
              defPoint=[Point[4],
                        Point[3]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG-D_ST_BNG',
              defPoint=[Point[3],
                        Point[4]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = TransfTranslationVector(name='H_FE_BNG_ST',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'H_FE_BNG_ST'])
                   
## DO STATOR IRON POINTS                    
result = LineArcRadius[1,2,3,4].extrude(transformation=Transf['H_FE_BNG_ST'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')

## DO STATOR PM RING TOP POINTS
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_OUT_ST_BNG-D_ST_BNG',
                      '0',
                      'H_ST_BNG/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_OUT_ST_BNG-D_ST_BNG)',
                      '0',
                      'H_ST_BNG/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_OUT_ST_BNG-0*D_ST_BNG',
                      '0',
                      'H_ST_BNG/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_OUT_ST_BNG-0*D_ST_BNG)',
                      '0',
                      'H_ST_BNG/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
                     
# lastInstance = PointCoordinates(color=Color['White'],
                 # visibility=Visibility['VISIBLE'],
                 # coordSys=CoordSys['COORD_SYS_ST'],
                 # uvw=['-(R_OUT_ST_BNG-D_ST_BNG+D_PM_B_ST)',
                      # '0',
                      # 'H_ST_BNG/2-H_PM_BNG_ST'],
                 # nature=Nature['STANDARD'],
                 # mesh=MeshPoint['AIDED_MESHPOINT'])

# lastInstance = PointCoordinates(color=Color['White'],
                 # visibility=Visibility['VISIBLE'],
                 # coordSys=CoordSys['COORD_SYS_ST'],
                 # uvw=['(R_OUT_ST_BNG-D_ST_BNG+D_PM_B_ST)',
                      # '0',
                      # 'H_ST_BNG/2-H_PM_BNG_ST'],
                 # nature=Nature['STANDARD'],
                 # mesh=MeshPoint['AIDED_MESHPOINT'])                     

## CLOSE TOP OF PM                     
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_OUT_ST_BNG-0*D_ST_BNG)',
              defPoint=[Point[12],
                        Point[11]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_OUT_ST_BNG-0*D_ST_BNG)',
              defPoint=[Point[11],
                        Point[12]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_OUT_ST_BNG-D_ST_BNG)',
              defPoint=[Point[9],
                        Point[10]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='(R_OUT_ST_BNG-D_ST_BNG)',
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
                 uvw=['R_OUT_ST_BNG-D_ST_BNG',
                      '0',
                      '-H_ST_BNG/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_OUT_ST_BNG-D_ST_BNG)',
                      '0',
                      '-H_ST_BNG/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['-(R_OUT_ST_BNG-0*D_ST_BNG)',
                      '0',
                      '-H_ST_BNG/2-H_PM_BNG_ST*0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['(R_OUT_ST_BNG-0*D_ST_BNG)',
                      '0',
                      '-H_ST_BNG/2-H_PM_BNG_ST*0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])          
                     
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG-0*D_ST_BNG',
              defPoint=[Point[15],
                        Point[16]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG-0*D_ST_BNG',
              defPoint=[Point[16],
                        Point[15]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG-D_ST_BNG',
              defPoint=[Point[13],
                        Point[14]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_OUT_ST_BNG-D_ST_BNG',
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
##########################

## upper pm, bearing rotor
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_OUT_PM_ROT_BNG',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_OUT_PM_ROT_BNG',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'])                     

## outer perimeter                 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_OUT_PM_ROT_BNG',
              defPoint=[Point[17],
                        Point[18]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_OUT_PM_ROT_BNG',
              defPoint=[Point[18],
                        Point[17]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])     
                                 
## inner perimeter points                 
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_OUT_PM_ROT_BNG-D_PM_B_ROT',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_OUT_PM_ROT_BNG+D_PM_B_ROT',
                      '0',
                      'H_ROT_B/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])                 

## inner perimeter                      
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_OUT_PM_ROT_BNG-D_PM_B_ROT',
              defPoint=[Point[19],
                        Point[20]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_OUT_PM_ROT_BNG-D_PM_B_ROT',
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
          
## start doing drive rotor
## outer radius
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['R_DR_ROT_OUT*Cosd(THETA_MAG/2)',
                      'R_DR_ROT_OUT*Sind(THETA_MAG/2)',
                      'H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['-R_DR_ROT_OUT*Cosd(THETA_MAG/2)',
                      '-R_DR_ROT_OUT*Sind(THETA_MAG/2)',
                      'H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])


## close drive fe circle                     
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_DR_ROT_OUT',
              defPoint=[Point[33],
                        Point[34]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_DR_ROT_OUT',
              defPoint=[Point[34],
                        Point[33]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

## do pms
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['(R_DR_ROT_OUT-D_DR_FE_ROT)*Cosd(THETA_MAG/2)',
                      '(R_DR_ROT_OUT-D_DR_FE_ROT)*Sind(THETA_MAG/2)',
                      'H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['(R_DR_ROT_OUT-D_DR_FE_ROT)*Cosd(THETA_MAG/2)',
                      '-(R_DR_ROT_OUT-D_DR_FE_ROT)*Sind(THETA_MAG/2)',
                      'H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['(R_DR_ROT_OUT-D_DR_FE_ROT-D_DR_PM)*Cosd(THETA_MAG/2)',
                      '(R_DR_ROT_OUT-D_DR_FE_ROT-D_DR_PM)*Sind(THETA_MAG/2)',
                      'H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ROT'],
                 uvw=['(R_DR_ROT_OUT-D_DR_FE_ROT-D_DR_PM)*Cosd(THETA_MAG/2)',
                      '-(R_DR_ROT_OUT-D_DR_FE_ROT-D_DR_PM)*Sind(THETA_MAG/2)',
                      'H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])
##close pms innerly
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='(R_DR_ROT_OUT-D_DR_FE_ROT-0*D_DR_PM)',
              defPoint=[Point[36],
                        Point[35]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[37],
                      Point[35]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[36],
                      Point[38]],
            nature=Nature['STANDARD'])

## propagate pms
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_DRIVE_PMS',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='90'))

result = Line[59,60,61].propagate(transformation=Transf['ROT_DRIVE_PMS'],
          repetitionNumber=3)          

##close fe of drive rotor
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_DR_ROT_OUT-D_DR_FE_ROT-0*D_DR_PM',
              defPoint=[Point[35],
                        Point[39]],
              nature=Nature['STANDARD'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
##close pms of drive rotor                 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ROT'],
              radius='R_DR_ROT_OUT-D_DR_FE_ROT-1*D_DR_PM',
              defPoint=[Point[38],
                        Point[37]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])                 
##close inner radii stator fe and stator pms                 
result = Line[71,72].propagate(transformation=Transf['ROT_DRIVE_PMS'],
          repetitionNumber=3)                      

##extrude drive rotor            
lastInstance = TransfTranslationVector(name='H_DR_ROTOR',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-H_DRV'])

result = Line[74,57,58,71,73,75,59,62,63,64,78,72,76,77,66,70,67,61,60,68,65,69].extrude(transformation=Transf['H_DR_ROTOR'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Lines')
          
##outer points of stator teeth                                                                             
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['L_SLOT_OUT',
                      '-W_SLOT/2',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['L_SLOT_OUT',
                      'W_SLOT/2',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

## close teeth     
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_DR_ST_OUT',
              defPoint=[Point[69],
                        Point[70]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
                     
##points were stator teeth meet
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['(W_SLOT/2)/Tand(30)',
                      '-W_SLOT/2',
                      '-H_DRV/2'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['(W_SLOT/2)/Tand(30)',
                      'W_SLOT/2',
                      '-H_DRV/2'],
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

result = LineArcRadius[119].propagate(transformation=Transf['ROT_TEETH'],
          repetitionNumber=5)
                                                                             
##propagate (rotate) slot junction
result = PointCoordinates[72].propagate(transformation=Transf['ROT_TEETH'],
          repetitionNumber=4)

##close sides
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[70],
                      Point[72]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[69],
                      Point[71]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

##close sides               
result = LineSegment[125,126].propagate(transformation=Transf['ROT_TEETH'],
          repetitionNumber=5)

##extrude upwards
lastInstance = TransfTranslationVector(name='DR_H_ST',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                'H_DRV'])     

result = Line[119,120,121,122,123,124,126,125,132,127,133,128,134,129,135,130,136,131].extrude(transformation=Transf['DR_H_ST'],
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
                                                     
## close iron of drive rotor
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[34],
                      Point[42]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[54],
                      Point[51]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

## build infinte box
lastInstance = InfiniteBoxCylinderZ(size=['3*R_OUT_ST_BNG',
                           '4*R_OUT_ST_BNG',
                           '3*Max(H_ROT_B,H_DRV)',
                           '4*Max(H_ROT_B,H_DRV)'])               
                                 
## build faces
buildFaces()
                  
## invisible cylinder
InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

## delete strange airgap faces
FaceAutomatic[52].delete()
FaceAutomatic[19].delete()
FaceAutomatic[34].delete()
FaceAutomatic[15].delete()
FaceAutomatic[6].delete()
FaceAutomatic[23].delete()
FaceAutomatic[41].delete()
FaceAutomatic[77].delete()
FaceAutomatic[27].delete()
FaceAutomatic[46].delete()

## build volumes
buildVolumes()          

ParameterGeom['DX'].expression='2'


ParameterGeom['DX'].expression='1'


ParameterGeom['DX'].expression='0'


ParameterGeom['DY'].expression='2'


ParameterGeom['DY'].expression='0'


ParameterGeom['DZ'].expression='3'


closeProject()

exit()
