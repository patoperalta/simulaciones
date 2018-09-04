#! Flux3D 12.0


#########################################################################################################################################################			  
##sensors
#########################################################################################################################################################	   
##rotor
lastInstance = SensorPredefinedMagForce(name='F_ROT',
                         support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ROT'],
                                                                        RegionVolume['PM1'],
                                                                        RegionVolume['PM2'],
                                                                        RegionVolume['PM3'],
                                                                        RegionVolume['PM4']]))

lastInstance = SensorPredefinedMagTorque(name='TX_ROT',
                          axis=xAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ROT'],
                                                                         RegionVolume['PM1'],
                                                                         RegionVolume['PM2'],
                                                                         RegionVolume['PM3'],
                                                                         RegionVolume['PM4']]))

lastInstance = SensorPredefinedMagTorque(name='TY_ROT',
                          axis=yAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ROT'],
                                                                         RegionVolume['PM1'],
                                                                         RegionVolume['PM2'],
                                                                         RegionVolume['PM3'],
                                                                         RegionVolume['PM4']]))

lastInstance = SensorPredefinedMagTorque(name='TZ_ROT',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ROT'],
                                                                         RegionVolume['PM1'],
                                                                         RegionVolume['PM2'],
                                                                         RegionVolume['PM3'],
                                                                         RegionVolume['PM4']]))

##stator
lastInstance = SensorPredefinedMagForce(name='F_ST',
                         support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))

lastInstance = SensorPredefinedMagTorque(name='TX_ST',
                          axis=xAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['XYZ1'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))

lastInstance = SensorPredefinedMagTorque(name='TY_ST',
                          axis=yAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['XYZ1'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))

lastInstance = SensorPredefinedMagTorque(name='TZ_ST',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['XYZ1'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['IRON_ST']]))						  