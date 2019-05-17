#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/8_icems_journal_2018_3d/00_main.py')

InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

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

deleteMesh()

Line[8,21].assignMeshLine(meshLine=MeshLine['R_ST'])

meshDomain()

deleteMesh()

meshDomain()



deleteMesh()

Line[7,37].assignMeshLine(meshLine=MeshLine['H_ST'])

meshDomain()

deleteMesh()

Line[1,10].assignMeshLine(meshLine=MeshLine['R_ROT'])

meshDomain()

deleteMesh()

Line[2,28].assignMeshLine(meshLine=MeshLine['H_ROT'])

meshDomain()

deleteMesh()

Line[9,22,14,19,27,24].assignMeshLine(meshLine=MeshLine['THETA'])     

meshDomain()

closeProject()

exit()
