#! Flux3D 18.1
#! executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/8_icems_journal_2018_3d/00_main.py')

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

##scenario
##general values
alpha_min = 1.0
alpha_max = 2
d_alpha= 0.2
 
beta_min = 0.1
beta_max = 0.3
d_beta= 0.1

n=1

##changing values
r_rot=10
wslot=7
dst=8
lslot=7

Scenario(name='PJ_ROT_'+str(r_rot)+'_N'+str(10*n))

startMacroTransaction()

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=60.0,
                                                                               stepValue=1.0)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                                  intervals=[IntervalStepValue(minValue=alpha_min,
                                                                               maxValue=alpha_max,
                                                                               stepValue=d_alpha)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                                  intervals=[IntervalStepValue(minValue=beta_min,
                                                                               maxValue=beta_max,
                                                                               stepValue=d_beta)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                                value=dst))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                                value=lslot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['N_PROP'],
                                                value=n))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=r_rot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                                value=wslot))

endMacroTransaction()

##changing values
r_rot=15
wslot=12
dst=13
lslot=9

Scenario(name='PJ_ROT_'+str(r_rot)+'_N'+str(10*n))

startMacroTransaction()

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=60.0,
                                                                               stepValue=1.0)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                                  intervals=[IntervalStepValue(minValue=alpha_min,
                                                                               maxValue=alpha_max,
                                                                               stepValue=d_alpha)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                                  intervals=[IntervalStepValue(minValue=beta_min,
                                                                               maxValue=beta_max,
                                                                               stepValue=d_beta)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                                value=dst))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                                value=lslot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['N_PROP'],
                                                value=n))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=r_rot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                                value=wslot))

endMacroTransaction()


##changing values
r_rot=20
wslot=16
dst=18
lslot=11

Scenario(name='PJ_ROT_'+str(r_rot)+'_N'+str(10*n))

startMacroTransaction()

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=60.0,
                                                                               stepValue=1.0)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['ALPHA_H'],
                                                  intervals=[IntervalStepValue(minValue=alpha_min,
                                                                               maxValue=alpha_max,
                                                                               stepValue=d_alpha)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MultiValues(parameter=VariationParameter['BETA'],
                                                  intervals=[IntervalStepValue(minValue=beta_min,
                                                                               maxValue=beta_max,
                                                                               stepValue=d_beta)]))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['D_ST'],
                                                value=dst))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                                value=lslot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['N_PROP'],
                                                value=n))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=r_rot))

Scenario['PJ_ROT_'+str(r_rot)+'_N'+str(10*n)].addPilot(pilot=MonoValue(parameter=VariationParameter['W_SLOT'],
                                                value=wslot))

endMacroTransaction()

saveProject()

