#! Flux3D 18.1
newProject()

GeomMeshOptions[1].methodAutomaticMeshVolume=OptimizeMeshGemsActivated(level=OptimizationStandard())

openModelerContext()

closeModelerContext()

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

null
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

#! Flux3D 18.1

#M270-50A import @ 60 Hz
# Material(name='Cogent_M270_50A_60Hz : AC Curve 60 Hz - Magsoft 11-27-13', propertyJE=PropertyJeLinear(rho='5.5E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=30.14897145455453, b=0.5583195383544677), BHPoint(h=57.47147683524457, b=0.8014669589602983), BHPoint(h=114.94295367048915, b=1.0554113872521187), BHPoint(h=173.82766354266596, b=1.1828586189728878), BHPoint(h=247.43355088288698, b=1.2726841983189632), BHPoint(h=339.44091005816324, b=1.3385008839945494), BHPoint(h=454.4501090272586, b=1.388316882513333), BHPoint(h=598.2116077386278, b=1.4271905946570458), BHPoint(h=777.9134811278393, b=1.4585163635993679), BHPoint(h=1002.5408228643537, b=1.4847032356509042), BHPoint(h=1283.3250000349967, b=1.5075606100537984), BHPoint(h=1634.3052214983004, b=1.5285329183638185), BHPoint(h=2073.03049832743, b=1.5488529348897677), BHPoint(h=2621.437094363842, b=1.5696502300451567), BHPoint(h=3306.945339409357, b=1.5920352462391996), BHPoint(h=4163.830645716251, b=1.617171360718385), BHPoint(h=5234.937278599868, b=1.646343099980897), BHPoint(h=6573.820569704389, b=1.6810265315423274), BHPoint(h=8247.42468358504, b=1.7229668832636367), BHPoint(h=10339.429825935855, b=1.7742681824379336), BHPoint(h=12954.436253874374, b=1.8340388022204785), BHPoint(h=16223.19428879752, b=1.888024421320848), BHPoint(h=20309.141832451456, b=1.934588181077391), BHPoint(h=25416.576262018876, b=1.9742566116964841), BHPoint(h=31800.86929897815, b=2.00770641431493), BHPoint(h=39781.23559517724, b=2.03568294053627), BHPoint(h=49756.6934654261, b=2.058939298562508), BHPoint(h=62226.015803237184, b=2.078195517643845), BHPoint(h=68448.61738356091, b=2.0860150694082296)], equivalentHarmonicCurve=EquivalentBhUnmodified()), volumicMass='7600')

##M270-50A import @ 50 Hz
Material(name='Cogent_M270_50A_50Hz : AC Curve 50 Hz - Magsoft 11-27-13', propertyJE=PropertyJeLinear(rho='5.5E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=25.335410773000902, b=0.5094095664557834), BHPoint(h=48.29562678603297, b=0.7454092508250769), BHPoint(h=96.59125357206594, b=1.0017970717433387), BHPoint(h=146.07447773808332, b=1.1344364688373194), BHPoint(h=207.92850794560505, b=1.229527244853858), BHPoint(h=285.2460457050072, b=1.300012211798584), BHPoint(h=381.8929679042599, b=1.3537654064900504), BHPoint(h=502.7016206533258, b=1.3958885445691518), BHPoint(h=653.7124365896582, b=1.4298715604430412), BHPoint(h=842.4759565100736, b=1.4582263472240313), BHPoint(h=1078.430356410593, b=1.482856944062607), BHPoint(h=1373.3733562862421, b=1.5052900520340753), BHPoint(h=1742.0521061308036, b=1.5268284928566516), BHPoint(h=2202.9005434365054, b=1.548661354467694), BHPoint(h=2778.9610900686325, b=1.5719502020275844), BHPoint(h=3499.036773358792, b=1.5979033017505093), BHPoint(h=4399.131377471491, b=1.6278458927617978), BHPoint(h=5524.249632612364, b=1.663292525794019), BHPoint(h=6930.647451538455, b=1.7059732977090576), BHPoint(h=8688.644725196069, b=1.753407597419617), BHPoint(h=10886.141317268088, b=1.8024404970229542), BHPoint(h=13633.01205735811, b=1.8516679534963991), BHPoint(h=17066.60048247064, b=1.899527941220615), BHPoint(h=21358.5860138613, b=1.9444152373205), BHPoint(h=26723.567928099623, b=1.9847898884010333), BHPoint(h=33429.79532089753, b=2.0192546990803937), BHPoint(h=41812.57956189491, b=2.046585611555856), BHPoint(h=52291.05986314165, b=2.0657108838057883), BHPoint(h=57520.16584945582, b=2.072281972186367)], equivalentHarmonicCurve=EquivalentBhUnmodified()), volumicMass='7600')


##MUMETAL import
Material(name='Imphy_Mumetal : Annealed at 1170C (4h)', propertyJE=PropertyJeLinear(rho='6.0E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=0.07730337052716346, b=0.04602790951232145), BHPoint(h=0.19142247126788856, b=0.10461819800940673), BHPoint(h=0.3828449425357771, b=0.18390674271156043), BHPoint(h=0.6707130314576181, b=0.27256669471182327), BHPoint(h=1.1169085692864718, b=0.36641484021222653), BHPoint(h=1.808511652921195, b=0.4568239710389393), BHPoint(h=2.8804964325550166, b=0.5363431733989547), BHPoint(h=4.54207284098744, b=0.6008591956808994), BHPoint(h=7.117516274057696, b=0.6498302372724394), BHPoint(h=11.109453595316594, b=0.6851048726067008), BHPoint(h=17.296956443267888, b=0.7094828510107992), BHPoint(h=26.887585857592395, b=0.7257160890365061), BHPoint(h=41.75306144979538, b=0.736039703330057), BHPoint(h=64.79454861771002, b=0.74205041483429), BHPoint(h=100.50885372797771, b=0.7447386380251969), BHPoint(h=155.86602664889264, b=0.7450817557495342), BHPoint(h=241.6696446763108, b=0.7452726177975624), BHPoint(h=374.66525261880895, b=0.7455648825875318), BHPoint(h=580.8084449296812, b=0.7460097433508142), BHPoint(h=900.3303930115333, b=0.7466811655891662), BHPoint(h=1395.5894125384038, b=0.7476831419417013), BHPoint(h=2163.2408928050536, b=0.7491578111557223), BHPoint(h=3353.1006872183607, b=0.7512963061089424), BHPoint(h=5197.383368558987, b=0.7543600097338129), BHPoint(h=8056.021524636959, b=0.7587286674261435), BHPoint(h=12486.910666557815, b=0.7649963126697421), BHPoint(h=19354.788836535146, b=0.7741298427653783), BHPoint(h=30000.0, b=0.7876991118430775), BHPoint(h=33000.0, b=0.7914690230273853)], equivalentHarmonicCurve=EquivalentBhUnmodified()))

## ndfeb50 import
#! Preflu2D 10.3
#! Preflu3D 10.3
#! FluxSkewed 10.3

Material(name='BMT_50H : BMT_NdFeB', propertyBH=PropertyBhMagnetOneDirection(br='1.41', mur='1.0447'), volumicMass='7600')     

## ndfeb42uh import
#! Preflu2D 10.3
#! Preflu3D 10.3
#! FluxSkewed 10.3

Material(name='BMT_42UH : BMT_NdFeB', propertyBH=PropertyBhMagnetOneDirection(br='1.31', mur='1.0561'), volumicMass='7600')


##METGLAS http://magweb.us/free-bh-curves/ + extrapolation in DATASHEET folder
lastInstance = Material(name='METGLAS',
         propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    b=0.0),
                                                            BHPoint(h=0.9491626252,
                                                                    b=0.023724686),
                                                            BHPoint(h=1.2126102414,
                                                                    b=0.032310921),
                                                            BHPoint(h=1.4633573684,
                                                                    b=0.042258681),
                                                            BHPoint(h=1.8202602134,
                                                                    b=0.059140911),
                                                            BHPoint(h=2.1645023577,
                                                                    b=0.075660091),
                                                            BHPoint(h=2.3387043684,
                                                                    b=0.084645811),
                                                            BHPoint(h=3.7196995418,
                                                                    b=0.157366666),
                                                            BHPoint(h=5.925144266,
                                                                    b=0.269697236),
                                                            BHPoint(h=8.2028369485,
                                                                    b=0.363638296),
                                                            BHPoint(h=10.3699733049,
                                                                    b=0.441967576),
                                                            BHPoint(h=12.7836153342,
                                                                    b=0.513561616),
                                                            BHPoint(h=15.7496570244,
                                                                    b=0.591127466),
                                                            BHPoint(h=21.3417874608,
                                                                    b=0.708591176),
                                                            BHPoint(h=26.2710176141,
                                                                    b=0.794886336),
                                                            BHPoint(h=31.4127501882,
                                                                    b=0.872267896),
                                                            BHPoint(h=37.2343806926,
                                                                    b=0.947088936),
                                                            BHPoint(h=43.5233589603,
                                                                    b=1.016735676),
                                                            BHPoint(h=59.5434504615,
                                                                    b=1.149),
                                                            BHPoint(h=74.8410942105,
                                                                    b=1.232395221),
                                                            BHPoint(h=91.2860871032,
                                                                    b=1.284148101),
                                                            BHPoint(h=111.5555108274,
                                                                    b=1.319848586),
                                                            BHPoint(h=133.3971373406,
                                                                    b=1.341587081),
                                                            BHPoint(h=155.7487012275,
                                                                    b=1.354974331),
                                                            BHPoint(h=183.9644056522,
                                                                    b=1.365540516),
                                                            BHPoint(h=231.9820348415,
                                                                    b=1.376390326),
                                                            BHPoint(h=279.1497657554,
                                                                    b=1.383211281),
                                                            BHPoint(h=331.8417717978,
                                                                    b=1.388736281),
                                                            BHPoint(h=371.3606808372,
                                                                    b=1.391972381),
                                                            BHPoint(h=447.8489552861,
                                                                    b=1.396941051),
                                                            BHPoint(h=613.9985136522,
                                                                    b=1.404),
                                                            BHPoint(h=792.0462181581,
                                                                    b=1.410014626),
                                                            BHPoint(h=800,
                                                                    b=1.410024621017041)]))

#NO12 https://cogent-power.com/downloads + extrapolation in DATASHEET folder
# lastInstance = Material(name='NO12',
         # propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    # b=0.0),
                                                            # BHPoint(h=25.0,
                                                                    # b=0.1),
                                                            # BHPoint(h=32.0,
                                                                    # b=0.2),
                                                            # BHPoint(h=39.0,
                                                                    # b=0.3),
                                                            # BHPoint(h=45.0,
                                                                    # b=0.4),
                                                            # BHPoint(h=51.0,
                                                                    # b=0.5),
                                                            # BHPoint(h=57.0,
                                                                    # b=0.6),
                                                            # BHPoint(h=65.0,
                                                                    # b=0.7),
                                                            # BHPoint(h=75.0,
                                                                    # b=0.8),
                                                            # BHPoint(h=89.0,
                                                                    # b=0.9),
                                                            # BHPoint(h=105.0,
                                                                    # b=1.0),
                                                            # BHPoint(h=124.0,
                                                                    # b=1.1),
                                                            # BHPoint(h=160.0,
                                                                    # b=1.2),
                                                            # BHPoint(h=248.0,
                                                                    # b=1.3),
                                                            # BHPoint(h=470.0,
                                                                    # b=1.4),
                                                            # BHPoint(h=1290.0,
                                                                    # b=1.5),
                                                            # BHPoint(h=3050.0,
                                                                    # b=1.6),
                                                            # BHPoint(h=5350.0,
                                                                    # b=1.7),
                                                            # BHPoint(h=9420.0,
                                                                    # b=1.8),
                                                            # BHPoint(h=10000.0,
                                                                    # b=1.800728849495633)]))
                                                                                     
# NO12 https://cogent-power.com/downloads ONLY DATASHEET INFORMATION, BUT IT STOPS TOO EARLY
# lastInstance = Material(name='NO12',
         # propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    # b=0.0),
                                                            # BHPoint(h=25.0,
                                                                    # b=0.1),
                                                            # BHPoint(h=32.0,
                                                                    # b=0.2),
                                                            # BHPoint(h=39.0,
                                                                    # b=0.3),
                                                            # BHPoint(h=45.0,
                                                                    # b=0.4),
                                                            # BHPoint(h=51.0,
                                                                    # b=0.5),
                                                            # BHPoint(h=57.0,
                                                                    # b=0.6),
                                                            # BHPoint(h=65.0,
                                                                    # b=0.7),
                                                            # BHPoint(h=75.0,
                                                                    # b=0.8),
                                                            # BHPoint(h=89.0,
                                                                    # b=0.9),
                                                            # BHPoint(h=105.0,
                                                                    # b=1.0),
                                                            # BHPoint(h=124.0,
                                                                    # b=1.1),
                                                            # BHPoint(h=160.0,
                                                                    # b=1.2),
                                                            # BHPoint(h=248.0,
                                                                    # b=1.3),
                                                            # BHPoint(h=470.0,
                                                                    # b=1.4),
                                                            # BHPoint(h=1290.0,
                                                                    # b=1.5),
                                                            # BHPoint(h=3050.0,
                                                                    # b=1.6),
                                                            # BHPoint(h=5350.0,
                                                                    # b=1.7),
                                                            # BHPoint(h=9420.0,
                                                                    # b=1.8)]))                                                            

# NO12 https://cogent-power.com/downloads + LOG EXTRAPOLATION WITH EXCEL (SEE DATASHEETS) EARLY                                                                                     
lastInstance = Material(name='NO12',
         propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    b=0.0),
                                                            BHPoint(h=25.0,
                                                                    b=0.1),
                                                            BHPoint(h=32.0,
                                                                    b=0.2),
                                                            BHPoint(h=39.0,
                                                                    b=0.3),
                                                            BHPoint(h=45.0,
                                                                    b=0.4),
                                                            BHPoint(h=51.0,
                                                                    b=0.5),
                                                            BHPoint(h=57.0,
                                                                    b=0.6),
                                                            BHPoint(h=65.0,
                                                                    b=0.7),
                                                            BHPoint(h=75.0,
                                                                    b=0.8),
                                                            BHPoint(h=89.0,
                                                                    b=0.9),
                                                            BHPoint(h=105.0,
                                                                    b=1.0),
                                                            BHPoint(h=124.0,
                                                                    b=1.1),
                                                            BHPoint(h=160.0,
                                                                    b=1.2),
                                                            BHPoint(h=248.0,
                                                                    b=1.3),
                                                            BHPoint(h=470.0,
                                                                    b=1.4),
                                                            BHPoint(h=1290.0,
                                                                    b=1.5),
                                                            BHPoint(h=3050.0,
                                                                    b=1.6),
                                                            BHPoint(h=5350.0,
                                                                    b=1.7),
                                                            BHPoint(h=9420.0,
                                                                    b=1.8),
                                                            BHPoint(h=20000.0,
                                                                    b=1.876631403201),                                                                                     
                                                            BHPoint(h=30000.0,
                                                                    b=1.930274437003),          
                                                            BHPoint(h=40000.0,
                                                                    b=1.968334775189),     
                                                            BHPoint(h=50000.0,
                                                                    b=1.997856667027),     
                                                            BHPoint(h=60000.0,
                                                                    b=2.021977808991),     
                                                            BHPoint(h=70000.0,
                                                                    b=2.042371943932),          
                                                            BHPoint(h=80000.0,
                                                                    b=2.060038147177),          
                                                            BHPoint(h=90000.0,
                                                                    b=2.075620842794),                                                                                          
                                                            BHPoint(h=100000.0,
                                                                    b=2.089560039016)]))

ParameterGeom['DX'].expression='2'


ParameterGeom['DX'].expression='.5'


ParameterGeom['DX'].expression='1'


ParameterGeom['DX'].expression='0'


#! Flux3D 18.1
                         
##parameters of winding
lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')     

lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')                              
                         
##geometric parameters of coil as IO parameters, slots are now filled !!!
lastInstance = VariationParameterFormula(name='DRV_R_SC : radius stator center, pg 36 reichert',
                          formula='(K_W_SLOT*R_OUT_PM_ROT_BNG)/2*1/Sin(pi()/6)')

lastInstance = VariationParameterFormula(name='DRV_R_DR_ROT_OUT_PH : drv rot outer radius, auxiliary actually',
                          formula='R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP')
                                
lastInstance = VariationParameterFormula(name='DRV_R_ST_OUT_PH : outer radius of teeth',
                          formula='DRV_R_DR_ROT_OUT_PH-R_OUT_PM_ROT_BNG*(K_D_DR_FE_ROT+K_D_DR_PM)-D_AGAP_D')
                                
for i in range(1,7):
     ## coordinate system for coils
     lastInstance = CoordSysCartesian(name='COORD_COIL_DRV_'+str(i),
                         parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                                            angleUnit=AngleUnit['DEGREE']),
                         origin=['R_DR_ST_OUT*cosd(30+60*'+str(i-1)+')',
                                   'R_DR_ST_OUT*sind(30+60*'+str(i-1)+')',
                                   '0'],
                         rotationAngles=RotationAngles(angleX='90',
                                                                 angleY='120+60*'+str(i-1)+'',
                                                                 angleZ='0'),
                         visibility=Visibility['VISIBLE'])
     # equations for torque current
     lastInstance = VariationParameterFormula(name='I_T_'+str(i),
                                     formula='IT_HAT*Cosd(2*DTHETA-DRV_THETA_T+'+str((i-1)*120)+')')                         

     # define current                                   
     lastInstance = CurrentStrandedCoil(name='I_DRV_'+str(i)+' : current in first drive coil',
                              rmsModulus='I_T_'+str(i))                                     
     #do coils
     lastInstance = CoilRectangular(name='Coil_DRV_'+str(i),
                strandedCoil=CoilConductor['I_DRV_'+str(i)],
                turnNumber='1',
                seriesOrParallel=AllInSeries(),
                coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
                coordSys=CoordSys['COORD_COIL_DRV_'+str(i)],
                center=['0',
                        '0',
                        '-1/2*K_COIL*R_DR_ST_OUT'],
                dimensions=['W_SLOT+K_COIL*R_OUT_ST_BNG/2',
                            'H_DRV+K_COIL*R_OUT_ST_BNG'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='K_COIL*R_OUT_ST_BNG',
                                                       width='K_COIL*R_OUT_ST_BNG'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])                                

ParameterGeom['R_SEP'].expression='5'


