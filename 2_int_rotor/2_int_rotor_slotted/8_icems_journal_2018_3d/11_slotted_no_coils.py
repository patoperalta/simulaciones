#! Flux3D 18.1

##rather meant for tilting exercises !
newProject()

GeomMeshOptions[1].methodAutomaticMeshVolume=OptimizeMeshGemsActivated(level=OptimizationStandard())

openModelerContext()

closeModelerContext()

#! Flux3D 12.0

print("FICHIER PARAM.PY\n")
##copy parameters from ext rotor rout14 in
## C:\Users\jperalta\Desktop\08_flux_ext_rotor\4_ext_rotor_script_2
##however, change beta definition

## revF is made for the ICEMS paper simulation, so we start from outside to inside building up the rotor...
## for revision F see 18.05.2018
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

r_rot_out=10
tuning=4
##rotor without hole!
ParameterGeom(name='R_ROT_OUT : outer radius of stator',
              expression=str(r_rot_out))

## mech/mag airgap                  
lastInstance = ParameterGeom(name='D_AGAP',
                 expression='2')     

##RETUNE FOLLOWING PARAMETERS FOR THE COILS                 
if tuning==1:
##tuning out 2d sims
     ParameterGeom(name='L_SLOT',
                      expression='7+ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*1.25')                      
                      
     ParameterGeom(name='W_SLOT',
                      expression='6+3*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')                                       
                      
     ParameterGeom(name='D_ST',
                      expression='6+4*ValidLR(R_ROT_OUT,11,21,1,1)+4*ValidLR(R_ROT_OUT,19,21,1,1)')                                                        
elif tuning==2:     
     ## help of 3d sims with alpha = 2
     ParameterGeom(name='L_SLOT',
                      expression='9.25+3/2*ValidLR(R_ROT_OUT,11,21,1,1)+2.25*ValidLR(R_ROT_OUT,19,21,1,1)')                      
                      
     ParameterGeom(name='W_SLOT',
                      expression='10+4*ValidLR(R_ROT_OUT,11,21,1,1)+6*ValidLR(R_ROT_OUT,19,21,1,1)')                                       
                      
     ParameterGeom(name='D_ST',
                      expression='10+5*ValidLR(R_ROT_OUT,11,21,1,1)+7*ValidLR(R_ROT_OUT,19,21,1,1)')                                                                    
elif tuning==3:
     ## help of 3d sims with alpha = 1.5
     ParameterGeom(name='L_SLOT',
                      expression='7.5+2*ValidLR(R_ROT_OUT,11,21,1,1)+1*ValidLR(R_ROT_OUT,19,21,1,1)')                      
                      
     ParameterGeom(name='W_SLOT',
                      expression='7+5*ValidLR(R_ROT_OUT,11,21,1,1)+4*ValidLR(R_ROT_OUT,19,21,1,1)')                                       
                      
     ParameterGeom(name='D_ST',
                      expression='8+5*ValidLR(R_ROT_OUT,11,21,1,1)+5*ValidLR(R_ROT_OUT,19,21,1,1)')     
elif tuning==4:
     ## free to change, and commented
     ParameterGeom(name='L_SLOT : r=(10,15,20)->l=(7.5,9.5,10.5)',
                      expression='7.5')
                      
     ParameterGeom(name='W_SLOT : r=(10,15,20)->l=(7,12,16)',
                      expression='7')
                      
     ParameterGeom(name='D_ST : r=(10,15,20)->l=(8,13,18)',
                      expression='8')                      
            
## stator
lastInstance = ParameterGeom(name='R_ST_IN',
              expression='R_ROT_OUT+D_AGAP+L_SLOT')                      
                                  
lastInstance = ParameterGeom(name='R_ST_OUT : outside stator radius',
              expression='R_ST_IN+D_ST')
                 
lastInstance = ParameterGeom(name='D_MOT',
              expression='R_ST_OUT*2')                             
                 
lastInstance = ParameterGeom(name='Y : for beginning of slot',
              expression='sqrt(R_ST_IN^2-(W_SLOT/2)^2)')

## for new build
lastInstance = ParameterGeom(name='Y2 : length of y to rstout',
              expression='Sqrt(R_ST_OUT**2-(W_SLOT/2)**2)')                 

# height definition alpha_h=h_rot/h_st                 
# DO NOT START WITH 1 OTHERWISE YOU LOSE 3 HOURS OF YOUR LIFE SEARCHING FOR YOUR ERROR
# (because planes have to be erased)
# become irrelevant in 2D
lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              expression='.5')
                 
lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              expression='1.5')                   

## heights                      
lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')     
            
ParameterGeom(name='h_st : height of stator',
              expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')                 

lastInstance = ParameterGeom(name='H_ROT',
              expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')          
                 
## displacements booleans
lastInstance = ParameterGeom(name='DALPHA_MULT',
              expression='0')

lastInstance = ParameterGeom(name='DBETA_MULT',
              expression='0')

lastInstance = ParameterGeom(name='DX_MULT',
              expression='0')

lastInstance = ParameterGeom(name='DY_MULT',
              expression='0')       
                 
lastInstance = ParameterGeom(name='DZ_MULT',
              expression='0')     
                 
##rotor position for relative displacements...
lastInstance = ParameterGeom(name='DTHETA',
              expression='0')

lastInstance = ParameterGeom(name='DALPHA',
              expression='DALPHA_MULT*R_ROT_OUT/5')

lastInstance = ParameterGeom(name='DBETA',
              expression='DBETA_MULT*R_ROT_OUT/5')

lastInstance = ParameterGeom(name='DX',
              expression='DX_MULT*R_ROT_OUT/12')

lastInstance = ParameterGeom(name='DY',
              expression='DY_MULT*R_ROT_OUT/12')       
                 
lastInstance = ParameterGeom(name='DZ',
              expression='DZ_MULT*R_ROT_OUT/5')     

lastInstance = ParameterGeom(name='DR_0',
              expression='0')

lastInstance = ParameterGeom(name='DTHETA_0',
              expression='0')                      

## for coil extrusion, see 14.05.2019, which is better than the previous approximation
lastInstance = ParameterGeom(name='TH_COIL : see 14.05.2019',
              expression='(Pi()/6-Atan2(W_SLOT/2,Y-L_SLOT))*sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)')
##or the definition from coils_concentric from TH_COIL
# lastInstance = VariationParameterFormula(name='TH_COIL : coil thickness to the sides, see 2.2.2018',
                          # formula='((R_ST_IN_PH-W_SLOT_PH/2)*pi()/3-W_SLOT_PH)/2')
# lastInstance = ParameterGeom(name='H_COIL : see 14.05.2019',
              # expression='((R_ST_IN-W_SLOT/2)*pi()/3-W_SLOT)/2')                                
                 

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
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.85)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowUnassigned())                       

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
Face[ALL].meshGenerator=MeshGenerator['MAPPED']
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

result = FaceAutomatic[ALL].propagate(transformation=Transf['ROT_ST_60'],
          repetitionNumber=5,
          buildingOption='FacesWithMeshGenerator',
          regionPropagation='None')

##########################################################
##separating point of coil and outer stator, so that we can mesh it as mapped
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['r_ST_IN',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])

##separating point of coil and outer stator, so that we can mesh it as mapped
lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['r_ST_OUT',
                      '0',
                      '0'],
                 nature=Nature['STANDARD'],
                 mesh=MeshPoint['AIDED_MESHPOINT'])     

# saveProjectAs('20190531_slotted_rev2_R20_6_DALPHA_DBETA.FLU')

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_IN',
              defPoint=[Point[21],
                        Point[26]],
              nature=Nature['STANDARD'])

lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[33],
                        Point[36]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])

buildFaces()

Face[13].meshGenerator=MeshGenerator['MAPPED']

result = FaceAutomatic[13].propagate(transformation=Transf['ROT_ST_60'],
          repetitionNumber=5,
          buildingOption='FacesWithMeshGenerator',
          regionPropagation='None')

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

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[75],
                      Point[78]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[78],
                      Point[77]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[77],
                      Point[76]],
            nature=Nature['STANDARD'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[76],
                      Point[75]],
            nature=Nature['STANDARD'])




buildFaces()

FaceAutomatic[92].delete()
FaceAutomatic[91].delete()
Face[93].meshGenerator=MeshGenerator['MAPPED']

## and make mapped faces                     
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
result = FaceAutomatic[93].extrude(transformation=Transf['ROT_ROTOR'],
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
result = Volume[19,20].propagateVolume(transformation=Transf['AX_SIM_ROT'],
                repetionNumber=1,
                buildingOption='VolumesWithMeshGenerator',
                regionPropagation='Same')


lastInstance = InfiniteBoxCylinderZ(size=['3*r_st_out',
                           '4*r_st_out',
                           '3*Max(H_ROT,H_ST)',
                           '4*Max(H_ROT,H_ST)'])          


buildFaces()  

InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

FaceAutomatic[106].delete()
FaceAutomatic[105].delete()

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
																	
lastInstance = Material(name='AIR',
         propertyBH=PropertyBhLinear(mur='1'))		

lastInstance = RegionVolume(name='IRON_ST',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['NO12']),
             color=Color['Black'],
             visibility=Visibility['VISIBLE'])
			 
lastInstance = RegionVolume(name='AIR_DOMAIN',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Magenta'],
             visibility=Visibility['VISIBLE'])		 

lastInstance = RegionVolume(name='PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Red'],
             visibility=Visibility['VISIBLE'])																

Volume[19,20,21,22].assignRegion(region=RegionVolume['PM'])

Volume[2,1,15,8,3,16,9,17,10,5,4,18,11,6,13,12,7,14].assignRegion(region=RegionVolume['IRON_ST'])

assignRegionToVolumes(volume=[Volume[23],
                              Volume[24],
                              Volume[25],
                              Volume[26],
                              Volume[27],
                              Volume[28],
                              Volume[29]],
                      region=RegionVolume['AIR_DOMAIN'])

orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

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


####ALTERNATIVELY
deleteMesh()


AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.85)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowAssigned(type=MeshShadowHigh()))

MeshGenerator['MeshGeneratorExtrusive_ROT_ROTOR','MeshGeneratorExtrusive_ST_H_ST','MeshGeneratorLinked_AX_SIM_ROT','MeshGeneratorLinked_ROT_ST_60'].deleteForce()

alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

j=8
## specific for motor size
r_rot=10
wslot=7
dst=8

lslot_min = 7
lslot_max = 10 
lslot_dgap= 1

Scenario(name='2_DALPHA_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))     

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))     

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))                                                                                           
                                                                                           
endMacroTransaction()

##############################

Scenario(name='3_DBETA_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1))                                                           

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
                                                                                           
Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))     

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))     

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))                                                                                                     

endMacroTransaction()

## tilting stiffnesses with and no slots...

Scenario(name='8_DALPHA2_R'+str(r_rot))

startMacroTransaction()

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1.0))
										  
Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()


Scenario(name='9_DBETA2_R'+str(r_rot))

startMacroTransaction()

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1.0))
										  
Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

####################################

## specific for motor size
r_rot=15
wslot=12
dst=13

lslot_min = 9
lslot_max = 12 
lslot_dgap= 1

Scenario(name='2_DALPHA_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))     

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))     

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))                                                                                           
                                                                                           
endMacroTransaction()

##############################

Scenario(name='3_DBETA_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1))                                                           

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
                                                                                           
Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))     

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))     

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))                                                                                                     
endMacroTransaction()

## tilting stiffnesses with and no slots...

Scenario(name='8_DALPHA2_R'+str(r_rot))

startMacroTransaction()

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1.0))
										  
Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()


Scenario(name='9_DBETA2_R'+str(r_rot))

startMacroTransaction()

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1.0))
										  
Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()

####################################
## specific for motor size
r_rot=20
wslot=16
dst=18

lslot_min = 11
lslot_max = 14 
lslot_dgap= 1

Scenario(name='2_DALPHA_R'+str(r_rot))

startMacroTransaction()

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))     

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))     

Scenario['2_DALPHA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))                                                                                           
                                                                                           
endMacroTransaction()

##############################

Scenario(name='3_DBETA_R'+str(r_rot))

startMacroTransaction()

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1))                                                           

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))
                                                                                           
Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))     

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))     

Scenario['3_DBETA_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))                                                                                                     

endMacroTransaction()

## tilting stiffnesses with and no slots...

Scenario(name='8_DALPHA2_R'+str(r_rot))

startMacroTransaction()

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DBETA_MULT'],
                                          value=1.0))
										  
Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['8_DALPHA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()


Scenario(name='9_DBETA2_R'+str(r_rot))

startMacroTransaction()

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                            intervals=[IntervalStepValue(minValue=alpha_min,
                                                                         maxValue=alpha_max,
                                                                         stepValue=d_alpha)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                            intervals=[IntervalStepValue(minValue=beta_min,
                                                                         maxValue=beta_max,
                                                                         stepValue=d_beta)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DALPHA_MULT'],
                                          value=1.0))
										  
Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                          value=90))										  

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                            intervals=[IntervalStepValue(minValue=lslot_min,
                                                                         maxValue=lslot_max,
                                                                         stepValue=lslot_dgap)]))

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                          value=r_rot))	

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                          value=wslot))	

Scenario['9_DBETA2_R'+str(r_rot)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                          value=dst))																		 
																		 
endMacroTransaction()