#! Flux3D 18.1
deleteMesh()

Volume[12,2,8,9,10,11].meshGenerator=MeshGenerator['MAPPED']


meshDomain()

Volume[3,1,7,6,5,4].meshGenerator=MeshGenerator['MAPPED']


meshDomain()

deleteMesh()

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
                   number=(45-15)/3)             
                       
lastInstance = MeshLineArithmetic(name='THETA_ST_SLOT : coming out of slot',
                   color=Color['White'],
                   number=(15)/3)     

LinePropagated[128,153,83,90,96,133,104,138,146,115,120,148].assignMeshLine(meshLine=MeshLine['R_ST'])

Line[207,213].assignMeshLine(meshLine=MeshLine['R_ROT'])

LineExtruded[152,127,88,82,95,132,103,137,111,142,119,147].assignMeshLine(meshLine=MeshLine['H_ST'])

Line[212,208,206].assignMeshLine(meshLine=MeshLine['H_ROT'])

LineExtruded[211,215].assignMeshLine(meshLine=MeshLine['THETA_ROT'])

LinePropagated[201,202,203,204,164,200].assignMeshLine(meshLine=MeshLine['THETA_ST_ROUND_BI'])

LinePropagated[155,89,135,140,145,150,114,122,130,85,98,106].assignMeshLine(meshLine=MeshLine['THETA_ST_SLOT'])

meshDomain()

deleteMesh()

Volume[47,48,49,50,37,46,64,65,39,61,62,63].meshGenerator=MeshGenerator['MAPPED']


Volume[41,52,42,53,43,54,44,55,45,36,35,51,59,68,58,67,57,66,56,40,38,70,60,69].meshGenerator=MeshGenerator['MAPPED']


Volume[21,16,17,22,18,23,19,24,20,25,13,14].meshGenerator=MeshGenerator['MAPPED']


meshDomain()

deleteMesh()

startMacroTransaction()
MeshLine['THETA_ST_ROUND_BI'].number=12

MeshLine['THETA_ST_SLOT'].number=3

endMacroTransaction()

meshDomain()

deleteMesh()

