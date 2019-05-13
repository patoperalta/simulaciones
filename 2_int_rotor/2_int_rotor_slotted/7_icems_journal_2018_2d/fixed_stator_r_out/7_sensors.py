#! Flux2D 18.1

#########################################################################################################################################################
##sensors
#########################################################################################################################################################			 
lastInstance = SensorPredefinedMagForce(name='F_ROT',
                         support=ComputationSupportFaceRegion(region=[RegionFace['PM']]))
						 
lastInstance = SensorPredefinedMagForce(name='F_ST',
                         support=ComputationSupportFaceRegion(region=[RegionFace['IRON_ST']]))						 

lastInstance = SensorPredefinedMagTorque(name='TZ_ROT',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0'])),
                          support=ComputationSupportFaceRegion(region=[RegionFace['PM']]))

lastInstance = SensorPredefinedMagTorque(name='TZ_ST',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                                               uvw=['0',
                                                                    '0'])),
                          support=ComputationSupportFaceRegion(region=[RegionFace['IRON_ST']]))