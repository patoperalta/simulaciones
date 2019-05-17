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
              expression='DALPHA_MULT*R_ROT_OUT/4')

lastInstance = ParameterGeom(name='DBETA',
              expression='DBETA_MULT*R_ROT_OUT/4')

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

##and apply          
# result = Line[ALL].propagate(transformation=Transf['ROT_ST_60'],
          # repetitionNumber=5)
            
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

lastInstance = PointCoordinates(color=Color['White'],
                 visibility=Visibility['VISIBLE'],
                 coordSys=CoordSys['COORD_SYS_ST'],
                 uvw=['sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)',
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
                     
                     
##define outer arc now     
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[33],
                        Point[39]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])
                 
lastInstance = LineArcRadius(color=Color['White'],
              visibility=Visibility['VISIBLE'],
              coordSys=CoordSys['COORD_SYS_ST'],
              radius='R_ST_OUT',
              defPoint=[Point[39],
                        Point[36]],
              nature=Nature['STANDARD'],
              mesh=MeshLine['AIDED_MESHLINE'],
              relaxation=RelaxLine['AIDED_RELAXLINE'])                 
 
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
# and backiron
lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[37],
                      Point[39]],
            nature=Nature['STANDARD'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])               

## generate face again
buildFaces()
Face[13,14,15,16].meshGenerator=MeshGenerator['MAPPED']
## rotate
result = FaceAutomatic[13,14,15,16].propagate(transformation=Transf['ROT_ST_60'],
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
            defPoint=[Point[109],
                      Point[112]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[112],
                      Point[111]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[111],
                      Point[110]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])

lastInstance = LineSegment(color=Color['White'],
            visibility=Visibility['VISIBLE'],
            defPoint=[Point[110],
                      Point[109]],
            nature=Nature['STANDARD'],
            mesh=MeshLine['AIDED_MESHLINE'],
            relaxation=RelaxLine['AIDED_RELAXLINE'])
                     
## build faces
buildFaces()
FaceAutomatic[164].delete()
FaceAutomatic[163].delete()

## and make mapped faces                     
Face[165].meshGenerator=MeshGenerator['MAPPED']
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
result = FaceAutomatic[165].extrude(transformation=Transf['ROT_ROTOR'],
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
result = Volume[37,38].propagateVolume(transformation=Transf['AX_SIM_ROT'],
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
result = FaceAutomatic[97,70,106].extrude(transformation=Transf['H_COILS_PLUS'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Volumes')
##down
result = FaceAutomatic[14,7,17].extrude(transformation=Transf['H_COILS_MINUS'],
        repetitionNumber=1,
        extrusionType='standard',
        buildingOption='Volumes')
#propagate
result = Volume[41,42,43,44,45,46].propagateVolume(transformation=Transf['ROT_ST_60'],
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

FaceAutomatic[323].delete()
FaceAutomatic[322].delete()
FaceAutomatic[321].delete()
FaceAutomatic[324].delete()

buildVolumes()

CoordSys['COORD_SYS_ST'].rotationAngles=RotationAngles(angleX='0',
                                                       angleY='0',
                                                       angleZ='-30')


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

#! Flux3D 12.0

##see 2.2.2018                         
##parameters of winding

##rev F is for ICEMS, no whole and stator outer radius is defined 18.05.2018

lastInstance = ParameterGeom(name='COIL_KCU : copper filling factor',
              expression='.4')     

lastInstance = ParameterGeom(name='RHO_CU',
              expression='1.68e-8')     

# ##geometry of coil                 
# lastInstance = VariationParameterFormula(name='D_ST_PH : stator thickness',
                          # formula='6+4*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')

# lastInstance = VariationParameterFormula(name='L_SLOT_PH : slot length',
                          # formula='7+ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*1.25')

# lastInstance = VariationParameterFormula(name='W_SLOT_PH',
                          # formula='6+3*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')

## now i have to define them otherwise...  since they are defined through functions (and not hard coded)                 
## copied from the checked 2d version of the slotted...
if tuning==1:
     lastInstance = VariationParameterFormula(name='L_SLOT_PH',
                                     formula='7+ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*5/4')                                                      
                                     
     lastInstance = VariationParameterFormula(name='W_SLOT_PH',
                                     formula='6+3*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')                                                                                      
     lastInstance = VariationParameterFormula(name='D_ST_PH',
                                     formula='6+4*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')
elif tuning==2:                                          
     lastInstance = VariationParameterFormula(name='L_SLOT_PH',
                                     formula='9.25+3/2*ValidLR(R_ROT_OUT,11,21,1,1)+2.25*ValidLR(R_ROT_OUT,19,21,1,1)')
                                     
     lastInstance = VariationParameterFormula(name='W_SLOT_PH',
                                     formula='10+4*ValidLR(R_ROT_OUT,11,21,1,1)+6*ValidLR(R_ROT_OUT,19,21,1,1)')                                                                                      
     lastInstance = VariationParameterFormula(name='D_ST_PH',
                                     formula='10+5*ValidLR(R_ROT_OUT,11,21,1,1)+7*ValidLR(R_ROT_OUT,19,21,1,1)')
elif tuning==3:                                          
     lastInstance = VariationParameterFormula(name='L_SLOT_PH',
                                     formula='7.5+2*ValidLR(R_ROT_OUT,11,21,1,1)+1*ValidLR(R_ROT_OUT,19,21,1,1)')
                                     
     lastInstance = VariationParameterFormula(name='W_SLOT_PH',
                                     formula='7+5*ValidLR(R_ROT_OUT,11,21,1,1)+4*ValidLR(R_ROT_OUT,19,21,1,1)')                                                                                      
     lastInstance = VariationParameterFormula(name='D_ST_PH',
                                     formula='8+5*ValidLR(R_ROT_OUT,11,21,1,1)+5*ValidLR(R_ROT_OUT,19,21,1,1)')          
elif tuning==4:                         
                    #free to roll with the parameters
     lastInstance = VariationParameterFormula(name='L_SLOT_PH',
                                     formula='L_SLOT')
                                     
     lastInstance = VariationParameterFormula(name='W_SLOT_PH',
                                     formula='W_SLOT')
                                     
     lastInstance = VariationParameterFormula(name='D_ST_PH',
                                     formula='D_ST')                                

lastInstance = VariationParameterFormula(name='R_ST_IN_PH',
                          formula='R_ROT_OUT+D_AGAP+L_SLOT_PH')     
                                
lastInstance = VariationParameterFormula(name='R_ST_OUT_PH',
                          formula='R_ST_IN_PH+D_ST_PH')                                

lastInstance = VariationParameterFormula(name='ST_A_SLOT : stator area/slot',
                          formula='pi()*(R_ST_OUT_PH^2-(R_ST_OUT_PH-D_ST_PH-L_SLOT_PH)^2)/6')

lastInstance = VariationParameterFormula(name='ST_BI_SLOT : backiron area / slot',
                          formula='Pi()*(R_ST_OUT_PH**2-(R_ST_OUT_PH-D_ST_PH)**2)/6')

lastInstance = VariationParameterFormula(name='ST_TOOTH_A : tooth',
                          formula='W_SLOT_PH*L_SLOT_PH')

lastInstance = VariationParameterFormula(name='A_SLOT : = 2*A_COIL',
                          formula='ST_A_SLOT-ST_BI_SLOT-ST_TOOTH_A')

lastInstance = VariationParameterFormula(name='A_COIL',
                          formula='A_SLOT/2')

lastInstance = VariationParameterFormula(name='A_CU',
                          formula='A_COIL*COIL_KCU')
                                
lastInstance = VariationParameterFormula(name='TH_COIL : coil thickness to the sides, see 2.2.2018',
                          formula='((R_ST_IN_PH-W_SLOT_PH/2)*pi()/3-W_SLOT_PH)/2')

lastInstance = VariationParameterFormula(name='ALPHA_CASE_PH : needed for stator height',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')                                     
                                
lastInstance = VariationParameterFormula(name='H_ST_PH : needed for coil length',
                          formula='2*R_ST_OUT_PH*(ALPHA_CASE_PH*BETA+(1-ALPHA_CASE_PH)*BETA/ALPHA_H)')     
                                
lastInstance = VariationParameterFormula(name='L_BAR_PH',
                          formula='2*(H_ST_PH+W_SLOT_PH)+2*pi()*TH_COIL/2')                                 
                                
## parameters for torque
lastInstance = VariationParameterPilot(name='I_T_PEAK : peak value of torque excitation, ATURNS',
                        referenceValue=0.0)
                              
lastInstance = VariationParameterPilot(name='THETA_T : torque generation angle degrees',
                        referenceValue=270)

lastInstance = VariationParameterPilot(name='JT_RMS : torque current density',
                        referenceValue=0.0)     

lastInstance = VariationParameterFormula(name='IT_HAT',
                          formula='(I_T_PEAK+JT_RMS*A_CU*sqrt(2))')                                                      

## parameters for force

lastInstance = VariationParameterPilot(name='I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=180)

lastInstance = VariationParameterPilot(name='THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
                              
lastInstance = VariationParameterFormula(name='THETA_F : force direction angle degrees',
                        formula='THETA_F0-THETA_F_DIR')
                                
lastInstance = VariationParameterPilot(name='JF_RMS : force current density',
                        referenceValue=0.0)          

lastInstance = VariationParameterFormula(name='IF_HAT',
                          formula='(I_F_PEAK+JF_RMS*A_CU*sqrt(2))')     

lastInstance = VariationParameterFormula(name='R_COIL',
                          formula='rho_cu*L_BAR_PH*1e-3/(A_CU*1e-6)')       
##losses                                
lastInstance = VariationParameterFormula(name='P_CU_TOT',
                          formula='6*R_COIL*(IF_HAT+IT_HAT)^2/2')     
                                
##do the coils nicely as in the last version
lastInstance = ParameterGeom(name='TH_COIL_OFFSET : space between stator and coil start',
              expression='R_ST_IN-Sqrt(R_ST_IN^2-(W_SLOT/2+TH_COIL)^2)+.1*0')

ParameterGeom(name='L_COIL : radial depth of coil',
              expression='R_ST_IN-sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)-TH_COIL_OFFSET')

# ParameterGeom(name='M_TH_COIL : m for radial thickness of coil',
              # expression='.184')                         
                 
# ParameterGeom(name='N_TH_COIL : n for radial thickness of coil',
              # expression='0')                      

# ParameterGeom(name='TH_COIL : width obtained with matlab + excel',
              # expression='M_TH_COIL*r_st_out+N_TH_COIL')                 

for i in range(1,7):
     ## coordinate system for coils
     lastInstance = CoordSysCartesian(name='COORD_COIL_'+str(i),
                         parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                                            angleUnit=AngleUnit['DEGREE']),
                         origin=['R_ST_IN*cosd(30*0+60*'+str(i-1)+')',
                                   'R_ST_IN*sind(30*0+60*'+str(i-1)+')',
                                   '0*H_ST'],
                         rotationAngles=RotationAngles(angleX='90',
                                                                 angleY='-90+60*'+str(i-1)+'',
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
                        'TH_COIL_OFFSET+L_COIL/2'],
                dimensions=['W_SLOT+TH_COIL',
                            'H_ST+TH_COIL'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='L_COIL',
                                                       width='TH_COIL'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])                                     
                    
## calculate volumes of different materials
lastInstance = VariationParameterFormula(name='V_FE_ST_RING : volume of iron ring of stator',
                          formula='pi()*(R_ST_OUT^2-(R_ST_OUT-D_ST_PH)^2)*H_ST_PH')     
                      
lastInstance = VariationParameterFormula(name='V_FE_ST_SLOTS : square volume of iron ring of stator',
                          formula='6*W_SLOT_PH*L_SLOT_PH*H_ST')     

lastInstance = VariationParameterFormula(name='H_ROT_PH',
                          formula='2*R_ST_OUT*(ALPHA_CASE_PH*ALPHA_H*beta+(1-ALPHA_CASE_PH)*beta)')          
                                
lastInstance = VariationParameterFormula(name='V_PM : volume of pm ring',
                          formula='pi()*R_ROT_OUT^2*H_ROT_PH')          
                                
lastInstance = VariationParameterFormula(name='V_CU : volume of copper',
                          formula='6*L_BAR*A_CU')                                     
                                
lastInstance = VariationParameterFormula(name='DENS_NO12 : no12 cogent google in g/mm^3',
                          formula='7.65/1000')                                     
                                
lastInstance = VariationParameterFormula(name='DENS_CU : cu wiki in g/mm^3',
                          formula='8.96/1000')          

lastInstance = VariationParameterFormula(name='DENS_NDFEB : ndfeb wiki in g/mm^3',
                          formula='1/2*(7.3+7.7)/1000')          

lastInstance = VariationParameterFormula(name='MASS_ST',
                          formula='(V_FE_ST_RING+V_FE_ST_SLOTS)*DENS_NO12')
                                
lastInstance = VariationParameterFormula(name='MASS_CU',
                          formula='V_CU*DENS_CU')
                                
lastInstance = VariationParameterFormula(name='MASS_PM',
                          formula='V_PM*DENS_NDFEB')                                     

#! Flux3D 12.0
#########################################################################################################################################################
##assign
#########################################################################################################################################################                     

##made for geometry revE!!!
## changed a little for disc rotor

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
                
for i in range(1,7):                
     lastInstance = RegionVolume(name='COIL_'+str(i),
                     magneticDC3D=MagneticDC3DVolumeVacuum(),
                     color=Color['Magenta'],
                     visibility=Visibility['VISIBLE'])     
                     
# ##solid coils, which are not really needed...
# for i in range(1,7):
     # lastInstance = RegionVolume(name='COIL_'+str(i),
                     # magneticDC3D=MagneticDC3DVolumeCoilConductor(coilConductor=CoilConductor3D(turnNumber='1',
                                                                                                                   # seriesParallel=AllInSeries(),
                                                                                                                   # electricComponent=CoilConductor['I_'+str(i)],
                                                                                                                   # fillFactor='1'),
                                                                             # material=Material['AIR']),
                     # color=Color['Red'],
                     # visibility=Visibility['INVISIBLE'])
                
InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

Volume[38,37,40,39].assignRegion(region=RegionVolume['PM'])

##iron teeth
Volume[5,6,7,1,3,4].assignRegion(region=RegionVolume['IRON_ST'])
##steel backiron
Volume[12,27,32,2,28,33,8,29,34,9,30,35,10,31,11,15,16,36].assignRegion(region=RegionVolume['IRON_ST'])
##coils
Volume[57,52,47,22,18,62,67,72].assignRegion(region=RegionVolume['COIL_1'])

Volume[48,53,58,19,23,63,68,73].assignRegion(region=RegionVolume['COIL_2'])

Volume[49,54,59,20,24,74,69,64].assignRegion(region=RegionVolume['COIL_3'])

Volume[50,55,60,21,25,65,70,75].assignRegion(region=RegionVolume['COIL_4'])

Volume[51,56,61,13,26,66,71,76].assignRegion(region=RegionVolume['COIL_5'])

Volume[41,42,43,17,14,44,45,46].assignRegion(region=RegionVolume['COIL_6'])
##domain
assignRegionToVolumes(volume=[Volume[78],
                              Volume[80],
                              Volume[79],
                              Volume[82],
                              Volume[81],
                              Volume[83]],
                      region=RegionVolume['AIR_DOMAIN'])

assignRegionToVolumes(volume=[Volume[77]],
                      region=RegionVolume['AIR_DOMAIN'])

orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

# ## mapped slots and their backiron
# #backiron
# Volume[12,2,8,9,10,11].meshGenerator=MeshGenerator['MAPPED']
# #slots     
# Volume[3,1,7,6,5,4].meshGenerator=MeshGenerator['MAPPED']
# #coil volume on top and under slots     
# Volume[47,48,49,50,37,46,64,65,39,61,62,63].meshGenerator=MeshGenerator['MAPPED']
# #coil sides, up and down
# Volume[41,52,42,53,43,54,44,55,45,36,35,51,59,68,58,67,57,66,56,40,38,70,60,69].meshGenerator=MeshGenerator['MAPPED']
# #coil sides at airgap height
# Volume[21,16,17,22,18,23,19,24,20,25,13,14].meshGenerator=MeshGenerator['MAPPED']

##mesh things, meshed equivalently to slotless version
## see 
## C:\Users\jperalta\Documents\github_pato\flux\2_int_rotor\1_int_rotor_slotless\8_icems_journal_2018_3d\7_assign_circular.py
## from line 37
lastInstance = MeshLineArithmetic(name='R_ST',
                   color=Color['White'],
                   number=3)

lastInstance = MeshLineArithmetic(name='R_ROT',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ST : whole height',
                   color=Color['White'],
                   number=6)

lastInstance = MeshLineArithmetic(name='H_ROT : whole height',
                   color=Color['White'],
                   number=10)
                       
lastInstance = MeshLineArithmetic(name='THETA_ROT',
                   color=Color['White'],
                   number=45)
                       
lastInstance = MeshLineArithmetic(name='THETA_ST_ROUND_BI : which is divided into almost 3 pieces',
                   color=Color['White'],
                   number=(45-9)/3)             
                       
lastInstance = MeshLineArithmetic(name='THETA_ST_SLOT : coming out of slot',
                   color=Color['White'],
                   number=(9)/3)          

                          

meshDomain()

deleteMesh()

## assign lines
LinePropagated[165,216,103,102,219,148,145,222,153,150,225,158,155,228,163,160,177,168,264,269,291,329,296,299,334,304,307,339,312,315,344,320,323,349,259,255].assignMeshLine(meshLine=MeshLine['R_ST'])

Line[237,243].assignMeshLine(meshLine=MeshLine['R_ROT'])

LineExtruded[151,149,224,156,154,227,161,159,176,166,164,215,99,100,218,146,144,221,180,96,94,185,109,107,190,117,115,195,125,123,200,133,131,169,141,139,105,192,112,113,197,120,121,202,129,171,136,137,182,91,92,187,104].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[236,242].assignMeshLine(meshLine=MeshLine['H_ROT'])

LineExtruded[241,245].assignMeshLine(meshLine=MeshLine['THETA_ROT'])

LinePropagated[231,223,226,233,229,234,232,220,230,217,179,178].assignMeshLine(meshLine=MeshLine['THETA_ST_ROUND_BI'])

LinePropagated[101,147,152,157,162,167].assignMeshLine(meshLine=MeshLine['THETA_ST_SLOT'])

meshDomain()

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

Scenario(name='Scenario_1',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['JT_RMS'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=4.0,
                                                                               stepValue=2.0)]))

endMacroTransaction()

Scenario['SCENARIO_1'].solve(projectName='../../../../../../Desktop/slotted_3d_journal.FLU')

EvolutiveCurve2D(name='TZ_ROT_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterXVariable(paramEvol=VariationParameter['JT_RMS'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=4.0)]),
                 formula=['TZ_ROT'])

lastInstance = IsovalueSpatialGroup(name='ISOVAL_1',
                     formula='B',
                     forceVisibility='yes',
                     smoothValues='yes',
                     regionInternalExternal='Automatic',
                     internalComputation='no',
                     regionType='volumeRegion',
                     group=[Groupspatial['V_IRON_ST']])

lastInstance = IsovalueSpatialGroup(name='ISOVAL_2',
                     formula='B',
                     forceVisibility='yes',
                     smoothValues='yes',
                     regionInternalExternal='Automatic',
                     internalComputation='no',
                     regionType='volumeRegion',
                     group=[Groupspatial['V_COIL_1']])

result = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_1']]),
               spatialFormula='ModV(B)^2',
               resultName='IntegralVol_1')

IsovalueSpatialGroup['ISOVAL_1'].displayIsovalue()

lastInstance = IsovalueSpatialGroup(name='ISOVAL_3',
                     formula='B',
                     forceVisibility='yes',
                     smoothValues='yes',
                     regionInternalExternal='Automatic',
                     internalComputation='no',
                     regionType='volumeRegion',
                     group=[Groupspatial['V_COIL_6']])

result = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               spatialFormula='ModV(B)^2',
               resultName='IntegralVol_2')

IsovalueSpatialGroup['ISOVAL_1'].displayIsovalue()

selectCurrentStep(activeScenario=Scenario['SCENARIO_1'],
                  parameterValue=['JT_RMS=0.0'])

saveProject()

Scenario(name='SCENARIO_2',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['SCENARIO_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['L_SLOT'],
                                                  intervals=[IntervalStepValue(minValue=7.5,
                                                                               maxValue=9.0,
                                                                               stepValue=0.5)]))

endMacroTransaction()

Scenario['SCENARIO_2'].solve(projectName='../../../../../../Desktop/slotted_3d_journal.FLU')

Scenario['SCENARIO_2'].deleteAllResults()

startMacroTransaction()
Scenario['SCENARIO_2'].removePilot(parameter=VariationParameter['L_SLOT'])
Scenario['SCENARIO_2'].addPilot(pilot=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                  intervals=[IntervalStepValue(minValue=7.0,
                                                                               maxValue=10.0,
                                                                               stepValue=1.0)]))
endMacroTransaction()

Scenario['SCENARIO_2'].solve(projectName='../../../../../../Desktop/slotted_3d_journal.FLU')

Scenario(name='SCENARIO_3',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['SCENARIO_3'].addPilot(pilot=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                  intervals=[IntervalStepValue(minValue=8.0,
                                                                               maxValue=8.5,
                                                                               stepValue=0.5)]))

endMacroTransaction()

Scenario['SCENARIO_3'].solve(projectName='../../../../../../Desktop/slotted_3d_journal.FLU')

displayIsovalues()

lastInstance = Grid2DAnnular(name='Grid2D_1',
              coordSys=CoordSys['XYZ1'],
              visibility=Visibility['VISIBLE'],
              color=Color['Turquoise'],
              origin=['0',
                      '0',
                      '0'],
              radius=['R_ROT_OUT+D_AGAP',
                      'R_ST_OUT',
                      '50'],
              theta=['0',
                     '360',
                     '361'])

lastInstance = IsovalueGrid2d(name='ISOVAL_4',
               formula='B',
               forceVisibility='yes',
               smoothValues='yes',
               regionInternalExternal='Automatic',
               internalComputation='no',
               regionType='volumeRegion',
               grid2d=[Grid2D['GRID2D_1']])

selectCurrentStep(activeScenario=Scenario['SCENARIO_2'],
                  parameterValue=['W_SLOT=7.0'])

selectCurrentStep(activeScenario=Scenario['SCENARIO_1'],
                  parameterValue=['JT_RMS=0.0'])

displayIsovalues()

saveProject()

closeProject()

exit()
