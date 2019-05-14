#! Flux3D 18.1
newProject()

GeomMeshOptions[1].methodAutomaticMeshVolume=OptimizeMeshGemsActivated(level=OptimizationStandard())

openModelerContext()

closeModelerContext()

#! Flux3D 12.0

print("FICHIER PARAM.PY\n")
##copy parameters from ext rotor rout14 in
## C:\Users\jperalta\Desktop\08_flux_ext_rotor\4_ext_rotor_script_2
##however, change beta definition

## rev F was made for sonceboz CTI #6 presentation... with fixed rotor size

## rev G was for ECCE paper

## rev H is for ICEMS paper... see notebook 18.05.2018 
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## define from outside towars inside
r_rot_out = 20
       
ParameterGeom(name='R_ROT_OUT : outer radius of rotor',
              expression=str(r_rot_out))     
                 
if r_rot_out==10:
     ## airgap                 
     lastInstance = ParameterGeom(name='D_AGAP : mechanic + cu',
                      expression='5.25')     
                      
     ## D_ST is now a parameter, so there is no proportionality constant                             
     lastInstance = ParameterGeom(name='D_ST : stator thickness',
                      expression='5')     
                      
     lastInstance = ParameterGeom(name='D_MECHGAP : d_cu= d_agap-d_mechgap',
                      expression='2')     
elif r_rot_out==15:
     ## airgap                 
     lastInstance = ParameterGeom(name='D_AGAP : mechanic + cu',
                      expression='5')     
     ## D_ST is now a parameter, so there is no proportionality constant                             
     lastInstance = ParameterGeom(name='D_ST : stator thickness',
                      expression='9')     
     lastInstance = ParameterGeom(name='D_MECHGAP : d_cu= d_agap-d_mechgap',
                      expression='2')                                                 
elif r_rot_out==20:
     ## airgap                 
     lastInstance = ParameterGeom(name='D_AGAP : mechanic + cu',
                      expression='5')     
     ## D_ST is now a parameter, so there is no proportionality constant                             
     lastInstance = ParameterGeom(name='D_ST : stator thickness',
                      expression='12.5')     
     lastInstance = ParameterGeom(name='D_MECHGAP : d_cu= d_agap-d_mechgap',
                      expression='2')                      
       
lastInstance = ParameterGeom(name='R_ST_IN : stator inner radius',
              expression='R_ROT_OUT+D_AGAP')                                  
## stator
lastInstance = ParameterGeom(name='R_ST_OUT : stator outer radius',
              expression='R_ST_IN+D_ST')
                 
lastInstance = ParameterGeom(name='D_MOT : stator outer diameter',
              expression='R_ST_OUT*2')                             
       
# height 
# DO NOT START WITH 1 OTHERWISE YOU LOSE 3 HOURS OF YOUR LIFE SEARCHING FOR YOUR ERROR
# (because planes have to be erased)

lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              expression='.3')                 
                 
lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              expression='1.0')     

lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')       
                 
ParameterGeom(name='h_st : height of stator',
              expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')                 

lastInstance = ParameterGeom(name='H_ROT',
              expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')                           
                 
##rotor position                 
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

#! Flux3D 12.0

#########################################################################################################################################################
##define application
#########################################################################################################################################################                 
lastInstance = ApplicationMagneticDC3D(formulationModel=MagneticDC3DAutomatic(),
                        scalarVariableOrder=ScalarVariableAutomaticOrder(),
                        vectorNodalVariableOrder=VectorNodalVariableAutomaticOrder(),
                        coilCoefficient=CoilCoefficientAutomatic())     

#! Flux3D 12.0

# Pour pouvoir mailler plus petit
# GeomMeshOptions[1].meshRelativeEpsilon = 1.0E-7
     

AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.9)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowUnassigned())                       

#! Flux3D 12.0

#########################################################################################################################################################
## coordinate systems
#########################################################################################################################################################     

# rev C still has a hole in the middle

# rev D has no hole and corresponds to ICEMS optimization            

##stator coordinate system
lastInstance = CoordSysCartesian(name='COORD_SYS_ST',
                  parentCoordSys=Local(coordSys=CoordSys['XYZ1']),
                  origin=['0',
                          '0',
                          '-h_st/2*0'],
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
#######################################################

##do all the points
##rotor
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

##stator                     
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_IN',
                      '0',
                      'H_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_OUT',
                      '0',
                      'H_ST/2'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['R_ST_OUT',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

#######################################################                     
## close points with lines
##rotor
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[2],
                      Point[3]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[3],
                      Point[4]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[4],
                      Point[1]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[1],
                      Point[2]],
            nature=Nature['STANDARD'])
##stator
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[6],
                      Point[5]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[5],
                      Point[8]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[8],
                      Point[7]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[7],
                      Point[6]],
            nature=Nature['STANDARD'])

#######################################################
## generate transformation
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ROTOR',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))

lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_ST',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))

buildFaces()

FaceAutomatic[ALL].meshGenerator=MeshGenerator['MAPPED']

#######################################################
## apply transformation
result = FaceAutomatic[1].extrude(transformation=Transf['ROT_ROTOR'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')

result = FaceAutomatic[2].extrude(transformation=Transf['ROT_ST'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='VolumesWithMeshGenerator')
#######################################################
## define transformation

lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_SYM_ROT',
                                coordSys=CoordSys['COORD_SYS_ROT'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))
                                                                             
lastInstance = TransfRotation3AnglesPivotCoord(name='ROT_SYM_ST',
                                coordSys=CoordSys['COORD_SYS_ST'],
                                pivotCoord=['0',
                                            '0',
                                            '0'],
                                rotationAngles=RotationAngles(angleX='0',
                                                              angleY='0',
                                                              angleZ='180'))                                                                             

lastInstance = TransfTranslationVector(name='AX_SIM_ROT',
                        coordSys=CoordSys['COORD_SYS_ROT'],
                        vector=['0',
                                '0',
                                '-H_ROT/2'])

lastInstance = TransfTranslationVector(name='AX_SIM_ST',
                        coordSys=CoordSys['COORD_SYS_ST'],
                        vector=['0',
                                '0',
                                '-H_ST/2'])
                                                                             
#######################################################
## apply transformation
result = Volume[1].propagateVolume(transformation=Transf['ROT_SYM_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')
                    
result = Volume[2].propagateVolume(transformation=Transf['ROT_SYM_ST'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

result = Volume[1,3].propagateVolume(transformation=Transf['AX_SIM_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')

result = Volume[2,4].propagateVolume(transformation=Transf['AX_SIM_ST'],
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

FaceAutomatic[34].delete()
FaceAutomatic[33].delete()
FaceAutomatic[35].delete()

buildVolumes()



#! Flux3D 12.0

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
                                                                                     
Material(name='Cogent_M235_35A_50Hz : AC Curve 50 Hz - Magsoft 11-27-13', propertyJE=PropertyJeLinear(rho='5.9E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=10.609410903823548, b=0.3273247381182948), BHPoint(h=21.165774753127977, b=0.5356124232868341), BHPoint(h=42.33154950625595, b=0.7875250174098541), BHPoint(h=65.6404252619563, b=0.9456105290875018), BHPoint(h=95.94196374436673, b=1.068912907131924), BHPoint(h=135.3339637715003, b=1.1650352014251444), BHPoint(h=186.54356380677393, b=1.2400700535602844), BHPoint(h=253.11604385262967, b=1.2988751266360483), BHPoint(h=339.66026791224215, b=1.3453200073496236), BHPoint(h=452.1677591897384, b=1.3824998965732842), BHPoint(h=598.4274978504834, b=1.4129172117197708), BHPoint(h=788.565158109452, b=1.4386352121148516), BHPoint(h=1035.744116446111, b=1.461409101559607), BHPoint(h=1357.076762283768, b=1.482800537000453), BHPoint(h=1774.809201872722, b=1.5042815706738921), BHPoint(h=2317.8613733383622, b=1.5273340799244424), BHPoint(h=3023.8291962436942, b=1.553550884652498), BHPoint(h=3941.587366020626, b=1.5847451446221081), BHPoint(h=5134.672986730638, b=1.6230753670568718), BHPoint(h=6685.684293653652, b=1.6711945341998606), BHPoint(h=8701.99899265357, b=1.7307693894339407), BHPoint(h=11323.208101353466, b=1.7933518159643456), BHPoint(h=14730.77994266333, b=1.8550604713504568), BHPoint(h=19160.623336366152, b=1.913315772893413), BHPoint(h=24919.419748179826, b=1.96569431071992), BHPoint(h=32405.855083537597, b=2.0101221739127864), BHPoint(h=42138.2210195027, b=2.044942554844638), BHPoint(h=54790.296736257354, b=2.0688515174858524), BHPoint(h=60269.32640988309, b=2.0757366692344377)], equivalentHarmonicCurve=EquivalentBhUnmodified()), volumicMass='7600')

## METGLAS 2605SA1_v2 grabbed from https://metglas.com/wp-content/uploads/2016/12/2605SA1-Magnetic-Alloy.pdf (16/11/2018) and extrapolated in C:\Users\jperalta\Google Drive\4_EPFL_Dropbox\07 Datasheets\stator materials\BH_METGLAS_2605SA1.xlxs
lastInstance = Material(name='METGLAS_2605SA1',
         propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    b=0.0),
                                                            BHPoint(h=1.8688,
                                                                    b=0.8049),
                                                            BHPoint(h=1.9637,
                                                                    b=0.8507),
                                                            BHPoint(h=2.0728,
                                                                    b=0.9039),
                                                            BHPoint(h=2.1736,
                                                                    b=0.9702),
                                                            BHPoint(h=2.2738,
                                                                    b=1.0209),
                                                            BHPoint(h=2.3787,
                                                                    b=1.0708),
                                                            BHPoint(h=2.585,
                                                                    b=1.1223),
                                                            BHPoint(h=2.8855,
                                                                    b=1.1681),
                                                            BHPoint(h=3.2137,
                                                                    b=1.2163),
                                                            BHPoint(h=3.4917,
                                                                    b=1.24),
                                                            BHPoint(h=3.6931,
                                                                    b=1.2604),
                                                            BHPoint(h=4.0576,
                                                                    b=1.28),
                                                            BHPoint(h=4.6103,
                                                                    b=1.3036),
                                                            BHPoint(h=5.2267,
                                                                    b=1.3289),
                                                            BHPoint(h=5.8858,
                                                                    b=1.3526),
                                                            BHPoint(h=6.5539,
                                                                    b=1.3681),
                                                            BHPoint(h=7.6663,
                                                                    b=1.3884),
                                                            BHPoint(h=8.8081,
                                                                    b=1.403),
                                                            BHPoint(h=10.3487,
                                                                    b=1.4144),
                                                            BHPoint(h=12.7437,
                                                                    b=1.4241),
                                                            BHPoint(h=17.2009,
                                                                    b=1.4353),
                                                            BHPoint(h=25.6192,
                                                                    b=1.4457),
                                                            BHPoint(h=34.5012,
                                                                    b=1.4512),
                                                            BHPoint(h=45.7399,
                                                                    b=1.4551),
                                                            BHPoint(h=58.6383,
                                                                    b=1.4598),
                                                            BHPoint(h=70.2915,
                                                                    b=1.4633),
                                                            BHPoint(h=80.3945,
                                                                    b=1.4662),
                                                            BHPoint(h=100.0,
                                                                    b=1.470424438),
                                                            BHPoint(h=200.0,
                                                                    b=1.484426011),
                                                            BHPoint(h=500.0,
                                                                    b=1.502935084),
                                                            BHPoint(h=1000.0,
                                                                    b=1.516936657),
                                                            BHPoint(h=5000.0,
                                                                    b=1.549447302),
                                                            BHPoint(h=10000.0,
                                                                    b=1.563448876),
                                                            BHPoint(h=50000.0,
                                                                    b=1.595959521)]))
## measured by the NETL of the USA https://netl.doe.gov/File%20Library/Research/onsite%20research/publications/METGLAS-2605-SA1-Core-Datasheet_approved.pdf and adapted in C:\Users\jperalta\Google Drive\4_EPFL_Dropbox\07 Datasheets\stator materialsBH_METGLAS_NETL.xlss
lastInstance = Material(name='METGLAS_NETL : measured by NETL USA',
         propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                                     b=0.0),
                                                                           BHPoint(h=1.55435366731285,
                                                                                     b=0.0482090049433856),
                                                                           BHPoint(h=5.49272005606477,
                                                                                     b=0.092968168119094),
                                                                           BHPoint(h=6.8983217212492,
                                                                                     b=0.124822047560834),
                                                                           BHPoint(h=9.03825545327978,
                                                                                     b=0.154089527754296),
                                                                           BHPoint(h=12.6365873357572,
                                                                                     b=0.184211808185341),
                                                                           BHPoint(h=16.5910859838949,
                                                                                     b=0.219499030493114),
                                                                           BHPoint(h=22.0025162134443,
                                                                                     b=0.256502138571918),
                                                                           BHPoint(h=29.9643099949821,
                                                                                     b=0.296077503983307),
                                                                           BHPoint(h=36.1144719984831,
                                                                                     b=0.327910956213487),
                                                                           BHPoint(h=41.1844011527231,
                                                                                     b=0.351138267081078),
                                                                           BHPoint(h=49.8863932772475,
                                                                                     b=0.384682891110392),
                                                                           BHPoint(h=64.769345355009,
                                                                                     b=0.431978171167463),
                                                                           BHPoint(h=82.9384596206403,
                                                                                     b=0.478398223775389),
                                                                           BHPoint(h=99.6609082881053,
                                                                                     b=0.517074791878141),
                                                                           BHPoint(h=121.485550628582,
                                                                                     b=0.560034789112611),
                                                                           BHPoint(h=151.326249804894,
                                                                                     b=0.610709987020865),
                                                                           BHPoint(h=180.456082018921,
                                                                                     b=0.650194215642217),
                                                                           BHPoint(h=204.124620656206,
                                                                                     b=0.681952244322022),
                                                                           BHPoint(h=232.902685811678,
                                                                                     b=0.713688274466301),
                                                                           BHPoint(h=260.585852427539,
                                                                                     b=0.745429018582478),
                                                                           BHPoint(h=288.638384930375,
                                                                                     b=0.774584934774343),
                                                                           BHPoint(h=313.415021228587,
                                                                                     b=0.798588479681211),
                                                                           BHPoint(h=339.288022635446,
                                                                                     b=0.821726225082732),
                                                                           BHPoint(h=361.880728130576,
                                                                                     b=0.842294855799601),
                                                                           BHPoint(h=387.397562771774,
                                                                                     b=0.860267659324395),
                                                                           BHPoint(h=412.542098387927,
                                                                                     b=0.882547461840399),
                                                                           BHPoint(h=435.505636339067,
                                                                                     b=0.899670179099507),
                                                                           BHPoint(h=467.94069613842,
                                                                                     b=0.927085068336881),
                                                                           BHPoint(h=501.844420071465,
                                                                                     b=0.949327159077697),
                                                                           BHPoint(h=527.726220892534,
                                                                                     b=0.967298391278525),
                                                                           BHPoint(h=552.883955630002,
                                                                                     b=0.98182842399349),
                                                                           BHPoint(h=579.857721852613,
                                                                                     b=1.00151711328932),
                                                                           BHPoint(h=595.168702578753,
                                                                                     b=1.01178414408412),
                                                                           BHPoint(h=628.349826997233,
                                                                                     b=1.02972394980563),
                                                                           BHPoint(h=651.319231224513,
                                                                                     b=1.04340232493094),
                                                                           BHPoint(h=671.008339540065,
                                                                                     b=1.0545115853716),
                                                                           BHPoint(h=695.434675348757,
                                                                                     b=1.06990584626795),
                                                                           BHPoint(h=721.693174901977,
                                                                                     b=1.08098682287722),
                                                                           BHPoint(h=739.922418498046,
                                                                                     b=1.09210236861375),
                                                                           BHPoint(h=759.979426131538,
                                                                                     b=1.10148788666355),
                                                                           BHPoint(h=1000.0,
                                                                                     b=1.210861866),
                                                                           BHPoint(h=2000.0,
                                                                                     b=1.485417464),
                                                                           BHPoint(h=3000.0,
                                                                                     b=1.646022194),
                                                                           BHPoint(h=4000.0,
                                                                                     b=1.759973062),
                                                                           BHPoint(h=5000.0,
                                                                                     b=1.848360223),
                                                                           BHPoint(h=6000.0,
                                                                                     b=1.920577792),
                                                                           BHPoint(h=7000.0,
                                                                                     b=1.981636876),
                                                                           BHPoint(h=8000.0,
                                                                                     b=2.034528661),
                                                                           BHPoint(h=9000.0,
                                                                                     b=2.081182521),
                                                                           BHPoint(h=10000.0,
                                                                                     b=2.122915821)]))




##these parameters were taken from rev D, and are there for aesthetic purposes only
lastInstance = ParameterGeom(name='M_R_THEO : m for theoretical radial thickness',
              expression='.3394')     
                 
lastInstance = ParameterGeom(name='N_R_THEO : n for theoretical radial thickness',
              expression='0')                      

lastInstance = ParameterGeom(name='COIL_R_THEO : theoretical coil radial thickness, see excel',
              expression='M_R_THEO*R_ST_OUT+N_R_THEO')     
                 
lastInstance = ParameterGeom(name='COIL_R_CASE : if 0, max coil thickness is limited by airgap',
              expression='Valid(COIL_R_THEO,0,D_AGAP-D_MECHGAP)')                      

lastInstance = ParameterGeom(name='COIL_R : real coil radial thickness, see excel v2',
              expression='COIL_R_CASE*COIL_R_THEO+(1-COIL_R_CASE)*(D_AGAP-D_MECHGAP)')     
                 

lastInstance = ParameterGeom(name='COIL_WCOIL : toroidal coil width',
              expression='2*pi()/6*(R_ST_IN-COIL_R)*0+3')     

lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')     

## now start with the theoretical parameters of the radially oriented coils
lastInstance = VariationParameterFormula(name='TH_COIL_CIRC : theoretical thickness, see 2.2.2018',
                          formula='D_AGAP-D_MECHGAP')     

lastInstance = VariationParameterFormula(name='R_ST_IN_PH',
                          formula='R_ROT_OUT+D_AGAP')
                                
lastInstance = VariationParameterFormula(name='A_COIL : area of each coil',
                          formula='pi()/6*(R_ST_IN_PH^2-(R_ST_IN_PH-TH_COIL_CIRC)^2)')     
                                
lastInstance = VariationParameterFormula(name='A_CU',
                          formula='A_COIL*COIL_KCU')

##now the length and therefore resistance
lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = VariationParameterFormula(name='D_ST_PH',
                          formula='D_ST')
                                
lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ROT_OUT+D_AGAP+D_ST')                                

lastInstance = VariationParameterFormula(name='H_ST_PH',
                          formula='2*R_ST_OUT_PH*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')     
                                
lastInstance = VariationParameterFormula(name='L_BAR_PH',
                          formula='2*(H_ST_PH+D_ST_PH)+2*pi()*TH_COIL_CIRC/2')     
                                
lastInstance = VariationParameterFormula(name='R_ROT_PH',
                          formula='R_ROT_OUT')

##everything ready for the resistance                                
lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')

lastInstance = VariationParameterFormula(name='R_COIL',
                          formula='rho_cu*L_BAR_PH*1e-3/(A_CU*1e-6)')     

##now parameters for currents
##torque     
lastInstance = VariationParameterPilot(name='I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
                              
lastInstance = VariationParameterPilot(name='THETA_T : torque generation angle degrees',
                        referenceValue=0)

lastInstance = VariationParameterPilot(name='JT_RMS : torque current density',
                        referenceValue=0.0)               

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(I_T_PEAK+JT_RMS*A_CU*sqrt(2))')          

##force
lastInstance = VariationParameterPilot(name='I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=270)

lastInstance = VariationParameterPilot(name='THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
                              
lastInstance = VariationParameterFormula(name='THETA_F : force direction angle degrees',
                        formula='THETA_F0-THETA_F_DIR')
                              
lastInstance = VariationParameterPilot(name='JF_RMS : force current density',
                        referenceValue=0.0)                                                              
                              
lastInstance = VariationParameterFormula(name='IF_HAT',
                          formula='(I_F_PEAK+JF_RMS*A_CU*sqrt(2))')          

##now, copper losses
lastInstance = VariationParameterFormula(name='P_CU_TOT',
                          formula='6/2*R_COIL*(IF_HAT+IT_HAT)^2')     

## now volume outputs     
lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ST_OUT_PH*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')
                                
lastInstance = VariationParameterFormula(name='V_FE_ST : volume of the iron of rotor',
                          formula='pi()*((R_ST_OUT_PH)^2-(R_ST_IN_PH)^2)*H_ST_PH')                           
                                
lastInstance = VariationParameterFormula(name='V_PM : PM volume',
                          formula='pi()*R_ROT_PH^2*H_ROT_PH')          

lastInstance = VariationParameterFormula(name='V_CU : copper volume',
                          formula='6*L_BAR_PH*A_CU/COIL_KCU')

##now loop what is needed for each coil     
##define coordinate system, current types, their sum and coils                                
for i in range(1,7):
     ## coordinate system for coils
     lastInstance = CoordSysCartesian(name='COORD_COIL_'+str(i),
                         parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                                            angleUnit=AngleUnit['DEGREE']),
                         origin=['1/2*(R_ST_OUT+r_st_in)*cosd(60*'+str(i-1)+')',
                                   '1/2*(R_ST_OUT+r_st_in)*sind(60*'+str(i-1)+')',
                                   '0'],
                         rotationAngles=RotationAngles(angleX='90',
                                                                 angleY='60*'+str(i-1)+'',
                                                                 angleZ='0'),
                         visibility=Visibility['VISIBLE'])
     # equations for torque current
     lastInstance = VariationParameterFormula(name='I_T_'+str(i),
                                     formula='IT_HAT*Cosd(1*DTHETA-THETA_T+'+str((i-1)*60)+')')                         
     # equations for force current                                     
     lastInstance = VariationParameterFormula(name='I_F_'+str(i),
                                     formula='IF_HAT*Cosd(1*DTHETA-THETA_F+'+str((i-1)*120)+')')
     # define current                                   
     lastInstance = CurrentStrandedCoil(name='I_'+str(i)+' : current in first drive coil',
                              rmsModulus='I_T_'+str(i)+'+I_F_'+str(i))                                     
     #do coils
     lastInstance = CoilRectangular(name='Coil_'+str(i),
                strandedCoil=CoilConductor['I_'+str(i)],
                turnNumber='1',
                seriesOrParallel=AllInSeries(),
                coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
                coordSys=CoordSys['COORD_COIL_'+str(i)],
                center=['0',
                        '0',
                        '0'],
                dimensions=['R_ST_OUT-R_ST_IN+COIL_R',
                            'h_ST+COIL_R'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='COIL_WCOIL',
                                                       width='COIL_R'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])                           

#! Flux3D 12.0
#########################################################################################################################################################
##assign
#########################################################################################################################################################                     

lastInstance = RegionVolume(name='IRON_ST',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
                
lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])                
                
Volume[1,3,5,6].assignRegion(region=RegionVolume['PM'])

Volume[2,4,7,8].assignRegion(region=RegionVolume['IRON_ST'])

assignRegionToVolumes(volume=[Volume[9],
                              Volume[10],
                              Volume[11],
                              Volume[12],
                              Volume[13],
                              Volume[14],
                              Volume[15]],
                      region=RegionVolume['AIR'])

orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

RegionVolume['IRON_ST'].color=Color['Black']

RegionVolume['PM'].color=Color['Red']

##mesh things
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=4)

lastInstance = MeshLineArithmetic(name='R_ROT',
                   color=Color['White'],
                   number=10)

lastInstance = MeshLineArithmetic(name='H_ST',
                   color=Color['White'],
                   number=5)

lastInstance = MeshLineArithmetic(name='H_ROT',
                   color=Color['White'],
                   number=8)
                       
lastInstance = MeshLineArithmetic(name='THETA',
                   color=Color['White'],
                   number=90)
                       

LineSegment[8].assignMeshLine(meshLine=MeshLine['R_ST'])

Line[7,37].assignMeshLine(meshLine=MeshLine['H_ST'])

LineSegment[1].assignMeshLine(meshLine=MeshLine['R_ROT'])

Line[2,28].assignMeshLine(meshLine=MeshLine['H_ROT'])

Line[9,22,24,14].assignMeshLine(meshLine=MeshLine['THETA'])





#! Flux3D 12.0


#########################################################################################################################################################
##sensors
#########################################################################################################################################################                
lastInstance = SensorPredefinedMagForce(name='F_ROT',
                         support=ComputationSupportVolumeRegion(region=[RegionVolume['PM']]))

lastInstance = SensorPredefinedMagTorque(name='TX_ROT',
                          axis=xAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['PM']]))

lastInstance = SensorPredefinedMagTorque(name='TY_ROT',
                          axis=yAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['PM']]))                     
                                
lastInstance = SensorPredefinedMagTorque(name='TZ_ROT',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['PM']]))                                     
                                
lastInstance = SensorPredefinedMagForce(name='F_ST',
                         support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))

lastInstance = SensorPredefinedMagTorque(name='TX_ST',
                          axis=xAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))

lastInstance = SensorPredefinedMagTorque(name='TY_ST',
                          axis=yAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))                     
                                
lastInstance = SensorPredefinedMagTorque(name='TZ_ST',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))                                     

alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.5
d_beta= 0.1

dgap_min = 3
dgap_max = 6 
d_dgap= 1

Scenario(name='1_DZ')

startMacroTransaction()

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['1_DZ'].addPilot(pilot=MonoValue(parameter=VariationParameter['DZ'],
                                          value=r_rot_out/5))

Scenario['1_DZ'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))

endMacroTransaction()

ParameterGeom['DALPHA'].expression='4'


ParameterGeom['DALPHA'].expression='5'


ParameterGeom['DALPHA'].expression='10'


ParameterGeom['DALPHA'].expression='5'


Scenario(name='2_DALPHA')

startMacroTransaction()

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA'].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA'],
                                          value=r_rot_out/4))

Scenario['2_DALPHA'].addPilot(pilot=MultiValues(parameter=VariationParameter['D_AGAP'],
                                            intervals=[IntervalStepValue(minValue=dgap_min,
                                                                         maxValue=dgap_max,
                                                                         stepValue=d_dgap)]))
                                                                                           
endMacroTransaction()

ParameterGeom['DTHETA'].expression='90'


ParameterGeom['DALPHA'].expression='0'


ParameterGeom['DX'].expression='1'


ParameterGeom['DTHETA'].expression='0'


ParameterGeom['DX'].expression='0'


ParameterGeom['DY'].expression='1'


ParameterGeom['DY'].expression='0'


closeProject()

exit()
