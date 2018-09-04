#! Flux3D 12.0
############################			  
##assign
#########################################################################################################################################################	   
##new coordinate systems for radial magnetization purposes


lastInstance = CoordSysCylindrical(name='COORD_ST_CYL',
                    parentCoordSys=Local(coordSys=CoordSys['COORD_SYS_ST']),
                    origin=['0',
                            '0',
                            '0'],
                    rotationAngles=RotationAngles(angleX='0',
                                                  angleY='0',
                                                  angleZ='0'),
                    visibility=Visibility['VISIBLE'])

lastInstance = CoordSysCylindrical(name='COORD_ROT_CYL',
                    parentCoordSys=Local(coordSys=CoordSys['COORD_SYS_ROT']),
                    origin=['0',
                            '0',
                            '0'],
                    rotationAngles=RotationAngles(angleX='0',
                                                  angleY='0',
                                                  angleZ='0'),
                    visibility=Visibility['VISIBLE'])

					
##now change coordinate systems and magnet orientation 					
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_BOTTOM'],coordSys=CoordSys['COORD_ROT_CYL'],orientation='Positive_Radial',center=['0','0','0'])
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_TOP'],coordSys=CoordSys['COORD_ROT_CYL'],orientation='Positive_Radial',center=['0','0','0'])
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_BOTTOM'],coordSys=CoordSys['COORD_ST_CYL'],orientation='Positive_Radial',center=['0','0','0'])
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_TOP'],coordSys=CoordSys['COORD_ST_CYL'],orientation='Positive_Radial',center=['0','0','0'])
