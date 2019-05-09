#! Flux3D 18.1


#########################################################################################################################################################			  
##sensors
#########################################################################################################################################################	   
			  
#### TOTAL FORCES
lastInstance = SensorPredefinedMagForce(name='F_DRV_BNG_ST',
                         support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ST_IRON'],
                                                                        RegionVolume['BNG_ST_PM_BOTTOM'],
                                                                        RegionVolume['BNG_ST_PM_TOP'],
                                                                        RegionVolume['DRV_ST_IRON_D']]))

lastInstance = SensorPredefinedMagForce(name='F_DRV_BNG_ROT',
                         support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ROT_IRON'],
																		RegionVolume['BNG_ROT_PM_BOTTOM'],
																		RegionVolume['BNG_ROT_PM_TOP'],
                                                                        RegionVolume['DRV_ROT_PM_R_1'],
                                                                        RegionVolume['DRV_ROT_PM_R_2'],
                                                                        RegionVolume['DRV_ROT_PM_R_3'],
                                                                        RegionVolume['DRV_ROT_PM_R_4'],
                                                                        RegionVolume['DRV_ROT_IRON_D']]))

#### TOTAL TORQUES
## stator
lastInstance = SensorPredefinedMagTorque(name='TX_DRV_BNG_ST',
                          axis=xAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['XYZ1'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ST_IRON'],
                                                                         RegionVolume['BNG_ST_PM_BOTTOM'],
                                                                         RegionVolume['BNG_ST_PM_TOP'],
                                                                         RegionVolume['DRV_ST_IRON_D']]))

lastInstance = SensorPredefinedMagTorque(name='TY_DRV_BNG_ST',
                          axis=yAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['XYZ1'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ST_IRON'],
                                                                         RegionVolume['BNG_ST_PM_BOTTOM'],
                                                                         RegionVolume['BNG_ST_PM_TOP'],
                                                                         RegionVolume['DRV_ST_IRON_D']]))
																		 
lastInstance = SensorPredefinedMagTorque(name='TZ_DRV_BNG_ST',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['XYZ1'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ST_IRON'],
                                                                         RegionVolume['BNG_ST_PM_BOTTOM'],
                                                                         RegionVolume['BNG_ST_PM_TOP'],
                                                                         RegionVolume['DRV_ST_IRON_D']]))													 

## rotor
lastInstance = SensorPredefinedMagTorque(name='TX_DRV_BNG_ROT',
                          axis=xAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ROT_IRON'],
																		 RegionVolume['BNG_ROT_PM_BOTTOM'],
																		 RegionVolume['BNG_ROT_PM_TOP'],
                                                                         RegionVolume['DRV_ROT_PM_R_1'],
                                                                         RegionVolume['DRV_ROT_PM_R_2'],
                                                                         RegionVolume['DRV_ROT_PM_R_3'],
                                                                         RegionVolume['DRV_ROT_PM_R_4'],
                                                                         RegionVolume['DRV_ROT_IRON_D']]))

lastInstance = SensorPredefinedMagTorque(name='TY_DRV_BNG_ROT',
                          axis=yAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ROT_IRON'],
																		 RegionVolume['BNG_ROT_PM_BOTTOM'],
																		 RegionVolume['BNG_ROT_PM_TOP'],						  
                                                                         RegionVolume['DRV_ROT_PM_R_1'],
                                                                         RegionVolume['DRV_ROT_PM_R_2'],
                                                                         RegionVolume['DRV_ROT_PM_R_3'],
                                                                         RegionVolume['DRV_ROT_PM_R_4'],
                                                                         RegionVolume['DRV_ROT_IRON_D']]))

lastInstance = SensorPredefinedMagTorque(name='TZ_DRV_BNG_ROT',
                          axis=zAxis(pivotPoint=AnalysingPoint(coordSys=CoordSys['COORD_SYS_ROT'],
                                                               uvw=['0',
                                                                    '0',
                                                                    '0'])),
                          support=ComputationSupportVolumeRegion(region=[RegionVolume['BNG_ROT_IRON'],
																		 RegionVolume['BNG_ROT_PM_BOTTOM'],
																		 RegionVolume['BNG_ROT_PM_TOP'],						  
                                                                         RegionVolume['DRV_ROT_PM_R_1'],
                                                                         RegionVolume['DRV_ROT_PM_R_2'],
                                                                         RegionVolume['DRV_ROT_PM_R_3'],
                                                                         RegionVolume['DRV_ROT_PM_R_4'],
                                                                         RegionVolume['DRV_ROT_IRON_D']]))
																		 
																		 