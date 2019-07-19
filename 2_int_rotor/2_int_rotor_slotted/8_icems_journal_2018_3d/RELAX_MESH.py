# deleteMesh()

# AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               # meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.95)),
                                               # meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             # faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             # volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               # meshShadow=MeshShadowAssigned(type=MeshShadowMedium()))


# AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               # meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.95)),
                                               # meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationMedium()),
                                                                             # faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationMedium()),
                                                                             # volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationMedium())),
                                               # meshShadow=MeshShadowAssigned(type=MeshShadowMedium()))

# deleteMesh()

# AidedMesh[1].synchronize()

# AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               # meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.95)),
                                               # meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationMedium()),
                                                                             # faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationMedium()),
                                                                             # volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationMedium())),
                                               # meshShadow=MeshShadowUnassigned())


# AidedMesh[1].synchronize()

# deleteMesh()

# AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               # meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.95)),
                                               # meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             # faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             # volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               # meshShadow=MeshShadowAssigned(type=MeshShadowHigh()))


# AidedMesh[1].synchronize()


# Face[ALL].meshGenerator=MeshGenerator['AIDED_MESHGENERATOR']


# Volume[ALL].meshGenerator=MeshGenerator['AUTOMATIC']


# meshDomain()

####ALTERNATIVELY
deleteMesh()

ParameterGeom['L_SLOT'].expression='7'


AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.85)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowAssigned(type=MeshShadowHigh()))

MeshGenerator['MeshGeneratorExtrusive_ROT_ROTOR','MeshGeneratorExtrusive_ST_H_ST','MeshGeneratorLinked_AX_SIM_ROT','MeshGeneratorLinked_ROT_ST_60'].deleteForce()