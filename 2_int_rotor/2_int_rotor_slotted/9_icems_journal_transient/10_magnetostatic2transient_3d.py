#! Flux2D 18.1

##save
convertApplicationToMagneticTransient(projectName='test_1.FLU')

##define conductivity of NdFeB
startMacroTransaction()
Material['BMT_42UH'].propertyJE=PropertyJeLinear(rho='140*10**(-8)')

Material['BMT_42UH'].name='BMT_42UH : BMT_NdFeB, rho from wiki'

endMacroTransaction()

##make magnet a conductor
RegionVolume['PM'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['BMT_42UH'])

##reorient magnet
orientRegVolMaterial(region=RegionVolume['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

##define copper conductivity
lastInstance = Material(name='COPPER',
         propertyJE=PropertyJeLinear(rho='1.68*10**(-8)'))

##and coils are no further made out of air
# startMacroTransaction()
# RegionVolume['COIL_1'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['COPPER'])

# RegionVolume['COIL_2'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['COPPER'])

# RegionVolume['COIL_3'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['COPPER'])

# RegionVolume['COIL_4'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['COPPER'])

# RegionVolume['COIL_5'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['COPPER'])

# RegionVolume['COIL_6'].magneticTransient3D=MagneticTransient3DVolumeSolidConductor(material=Material['COPPER'])

# endMacroTransaction()

#define rotor speed in RPM

lastInstance = VariationParameterPilot(name='N_PROP',
                        referenceValue=1.0)

lastInstance = VariationParameterFormula(name='N',
                          formula='N_PROP*161/(R_ROT_OUT/1000)*(60/(2*pi()))')

##make mechanical set
lastInstance = MechanicalSetRotation1Axis(name='ROTOR',
                           kinematics=RotatingImposedSpeed(velocity='N',
                                                           initialPosition='0'),
                           rotationAxis=RotationZAxis(coordSys=CoordSys['COORD_SYS_ROT'],
                                                      pivot=['0',
                                                             '0',
                                                             '0']))

lastInstance = MechanicalSetFixed(name='STATOR')

##define region's mechanical set
##for 'concentric coils'
RegionVolume['AIR_DOMAIN','COIL_1','COIL_2','COIL_3','COIL_4','COIL_5','COIL_6','IRON_ST'].mechanicalSet=MechanicalSet['STATOR']
##for virtual coils
CoilRectangular[ALL].mechanicalSet=MechanicalSet['STATOR']

RegionVolume['PM'].mechanicalSet=MechanicalSet['ROTOR']

##define loss sensor
lastInstance = SensorPredefinedLosses(name='P_JOULE_ROT',
                       support=ComputationSupportLossesVolumeRegion(region=[RegionVolume['PM']]))