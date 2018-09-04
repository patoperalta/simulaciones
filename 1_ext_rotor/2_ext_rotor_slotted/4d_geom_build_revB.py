#! Flux3D 12.0
# annoying things like domain und clean faces

lastInstance = InfiniteBoxCylinderZ(size=['3*r_rot_out',
                           '4*r_rot_out',
                           '3*Max(H_ROT,H_ST)',
                           '4*Max(H_ROT,H_ST)'])


buildFaces()

InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()
##erase unnecesary faces
FaceAutomatic[193].delete()
FaceAutomatic[194].delete()
FaceAutomatic[195].delete()

# ##finally build volumes
buildVolumes()

InfiniteBoxCylinderZ['InfiniteBoxCylinderZ'].setInvisible()

# ##check geometry
checkGeometry()		
