#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

#! Flux2D 18.1

##save
convertApplicationToMagneticTransient(projectName='test_1.FLU')

##define conductivity
startMacroTransaction()
Material['BMT_42UH'].propertyJE=PropertyJeLinear(rho='140*10**(-8)')

Material['BMT_42UH'].name='BMT_42UH : BMT_NdFeB, rho from wiki'

endMacroTransaction()

orientRegSurfMaterial(region=RegionFace['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

#define speed
# lastInstance = ParameterGeom(name='N_PROP : fraction of full mech speed',
              # expression='1')

# lastInstance = ParameterGeom(name='N : rpm for mechanical set',
              # expression='N_PROP*161/(R_ROT_OUT/1000)*(60/(2*pi()))')

# lastInstance = ParameterGeom(name='N : rpm for mechanical set',
              # expression='20000')

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
                                                             '0']))


lastInstance = MechanicalSetFixed(name='STATOR')

#define region's mechanical set
RegionFace['AIRGAP','COIL_MINUS_1','COIL_MINUS_2','COIL_MINUS_3','COIL_MINUS_4','COIL_MINUS_5','COIL_MINUS_6','COIL_PLUS_1','COIL_PLUS_2','COIL_PLUS_3','COIL_PLUS_4','COIL_PLUS_5','COIL_PLUS_6','INFINITE','IRON_ST'].mechanicalSet=MechanicalSet['STATOR']

RegionFace['PM'].mechanicalSet=MechanicalSet['ROTOR']

## PM is no longer non conducting volume, but a solid conductor with open circuit
RegionFace['PM'].magneticTransient2D=MagneticTransient2DFaceSolidConductor(material=Material['BMT_42UH'],
                                                                           circuitType=OpenCircuit())

##it loses its orientation after previous definition
orientRegSurfMaterial(region=RegionFace['PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

# Scenario(name='Scenario_1')

# startMacroTransaction()

# Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  # intervals=[IntervalStepValue(minValue=0.0,
                                                                               # maxValue=360.0,
                                                                               # stepValue=1.0)]))

# endMacroTransaction()

Scenario(name='Scenario_1')

startMacroTransaction()

Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=180.0,
                                                                               stepValue=1.0)]))

Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['N_PROP'],
                                                  intervals=[IntervalStepValue(minValue=0.5,
                                                                               maxValue=1.0,
                                                                               stepValue=0.5)]))

endMacroTransaction()

Scenario['SCENARIO_1'].solve(projectName='test_1.FLU')

lastInstance = IsovalueSpatialGroup(name='ISOVAL_1',
                     formula='Comp(3,J)',
                     forceVisibility='yes',
                     smoothValues='yes',
                     group=[Groupspatial['S_PM']])

selectCurrentStep(activeScenario=Scenario['SCENARIO_1'],
                  parameterValue=['N_PROP=0.5',
                                  'ANGPOS_ROTOR=180.0'])

lastInstance = SensorPredefinedLosses(name='Sensor_1',
                       support=ComputationSupportLossesFaceRegion(region=[RegionFace['PM']]))

EvolutiveCurve2D(name='N_05',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['N_PROP'],
                                                                             currentValue=0.5),
                                                           SetParameterXVariable(paramEvol=VariationParameter['ANGPOS_ROTOR'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=180.0)]),
                 formula=['SENSOR_1'])

EvolutiveCurve2D(name='SENSOR_1_1',
                 evolutivePath=EvolutivePath(parameterSet=[SetParameterFixed(paramEvol=VariationParameter['N_PROP'],
                                                                             currentValue=1.0),
                                                           SetParameterXVariable(paramEvol=VariationParameter['ANGPOS_ROTOR'],
                                                                                 limitMin=0.0,
                                                                                 limitMax=180.0)]),
                 formula=['SENSOR_1'])

saveProjectAs('../../../../../../Desktop/02_flux_int_rotor_slotted/7_icems_journal_2d_transient/test_2.FLU')

