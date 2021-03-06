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
						  
lastInstance = SensorPredefinedMagTorque(name='TZ_COILS',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                                               uvw=['0',
                                                                    '0'])),
                          support=ComputationSupportFaceRegion(region=[RegionFace['COIL_PLUS_1'],
                                                                       RegionFace['COIL_PLUS_2'],
                                                                       RegionFace['COIL_PLUS_3'],
                                                                       RegionFace['COIL_PLUS_4'],
                                                                       RegionFace['COIL_PLUS_5'],
																	   RegionFace['COIL_MINUS_1'],																	   
																	   RegionFace['COIL_MINUS_2'],
                                                                       RegionFace['COIL_MINUS_3'],
                                                                       RegionFace['COIL_MINUS_4'],
                                                                       RegionFace['COIL_MINUS_5'],																	   
																	   RegionFace['COIL_MINUS_6'],																	   
                                                                       RegionFace['COIL_PLUS_6']]))

lastInstance = SensorPredefinedMagForce(name='F_COILS',
                          support=ComputationSupportFaceRegion(region=[RegionFace['COIL_PLUS_1'],
                                                                       RegionFace['COIL_PLUS_2'],
                                                                       RegionFace['COIL_PLUS_3'],
                                                                       RegionFace['COIL_PLUS_4'],
                                                                       RegionFace['COIL_PLUS_5'],
																	   RegionFace['COIL_MINUS_1'],																	   
																	   RegionFace['COIL_MINUS_2'],
                                                                       RegionFace['COIL_MINUS_3'],
                                                                       RegionFace['COIL_MINUS_4'],
                                                                       RegionFace['COIL_MINUS_5'],																	   
																	   RegionFace['COIL_MINUS_6'],																	   
                                                                       RegionFace['COIL_PLUS_6']]))					  