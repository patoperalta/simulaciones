#! Flux3D 18.1
newProject()

GeomMeshOptions[1].methodAutomaticMeshVolume=OptimizeMeshGemsActivated(level=OptimizationStandard())

openModelerContext()

closeModelerContext()


lastInstance = VariationParameterFormula(name='R_ROT_DRV_AUX : aux once again, outer radius drive pms',
                          formula='R_OUT_ST_DRV_AUX-D_DRV_ST-D_AGAP_D')

lastInstance = VariationParameterFormula(name='V_PM_DRV_ROT',
                          formula='pi()*(R_ROT_DRV_AUX^2)*(D_MOT_AUX*BETA_D)')

###########################

lastInstance = VariationParameterFormula(name='OUT_V_FE',
                          formula='V_FE_BNG_ST+V_FE_BNG_ROT+V_FE_DRV_ST')

lastInstance = VariationParameterFormula(name='OUT_V_PM',
                          formula='V_PM_BNG_ROT*2+V_PM_BNG_ST*2+V_PM_DRV_ROT')

lastInstance = VariationParameterFormula(name='OUT_V_CU',
                          formula='(6*BNG_A_CU*BNG_L_BAR_PH+3*DRV_A_CU*DRV_LCA)/COIL_KCU')

#! Flux3D 12.0
############################                 
##assign
#########################################################################################################################################################        
##definitions


##bearing stator
lastInstance = RegionVolume(name='BNG_ST_PM_TOP',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='BNG_ST_PM_BOTTOM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
                
lastInstance = RegionVolume(name='BNG_ST_IRON',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])                

##bearing rotor                
lastInstance = RegionVolume(name='BNG_ROT_IRON',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])                
                
lastInstance = RegionVolume(name='BNG_ROT_PM_TOP',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='BNG_ROT_PM_BOTTOM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])                

##drive rotor
lastInstance = RegionVolume(name='DRV_ROT_PM',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])      
                
##drive stator
lastInstance = RegionVolume(name='DRV_ST_IRON',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
##air
lastInstance = RegionVolume(name='AIR',
             magneticDC3D=MagneticDC3DVolumeVacuum(),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

Volume[1].assignRegion(region=RegionVolume['BNG_ST_IRON'])

Volume[2].assignRegion(region=RegionVolume['BNG_ST_PM_BOTTOM'])

Volume[4].assignRegion(region=RegionVolume['BNG_ST_PM_TOP'])

Volume[5].assignRegion(region=RegionVolume['BNG_ROT_PM_TOP'])

Volume[6].assignRegion(region=RegionVolume['BNG_ROT_IRON'])

Volume[7].assignRegion(region=RegionVolume['BNG_ROT_PM_BOTTOM'])

Volume[8].assignRegion(region=RegionVolume['DRV_ST_IRON'])

Volume[9].assignRegion(region=RegionVolume['DRV_ROT_PM'])

##assign air volumes
assignRegionToVolumes(volume=[Volume[3],
                              Volume[10],
                              Volume[11],
                              Volume[12],
                              Volume[13],
                              Volume[14],
                              Volume[15]],
                      region=RegionVolume['AIR'])

## orient vertical pms of bearing stator
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_TOP'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',center=['0','0','0'],angle='0')
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',angle='180')

## orient vertical pms of bearing rotor
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_TOP'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',center=['0','0','0'],angle='180')
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',angle='0')

## diametral magnetization drive
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')

#########################################################################################################################################################                 
##appeareance
#########################################################################################################################################################        
##change colors
RegionVolume['BNG_ROT_PM_BOTTOM','BNG_ST_PM_TOP'].color=Color['Red']

RegionVolume['BNG_ROT_PM_TOP','BNG_ST_PM_BOTTOM'].color=Color['Green']

RegionVolume['BNG_ROT_IRON','BNG_ST_IRON','DRV_ST_IRON'].color=Color['Black']

RegionVolume['DRV_ROT_PM'].color=Color['Cyan']

RegionVolume['AIR'].setInvisible()

meshDomain()

displayArrowsOnMagnet()

saveProjectAs('test_4.FLU')

deleteArrows()

executeBatchSpy('8_sensors_revE.py')                              # Defines different parameters

deleteMesh()

ParameterGeom['R_SEP'].expression='5'


ParameterGeom['R_SEP'].expression='2'


ParameterGeom['R_SEP'].expression='1'


ParameterGeom['R_SEP'].expression='2'


ParameterGeom['R_SEP'].expression='4'


ParameterGeom['R_SEP'].expression='3.5'


ParameterGeom['DZ'].expression='2'


ParameterGeom['DZ'].expression='0'


ParameterGeom['DALPHA'].expression='2'


ParameterGeom['DALPHA'].expression='0'


ParameterGeom['DBETA'].expression='10'


ParameterGeom['DBETA'].expression='0'


ParameterGeom['DX'].expression='2'


ParameterGeom['DX'].expression='0'


ParameterGeom['DX'].expression='2'


ParameterGeom['DTHETA'].expression='90'


ParameterGeom['DTHETA'].expression='0'


ParameterGeom['DX'].expression='0'


executeBatchSpy('9_make_scenarios_passive_revD.py')      # Defines different parameters

executeBatchSpy('10_make_scenarios_active_revD.py')         # Defines different parameters

meshDomain()

meshDomain()

generateSecondOrderElements()

saveProjectAs('../../../../../Desktop/double_mot_test.FLU')

Scenario(name='ReferenceValues')

Scenario['ReferenceValues'].adaptive = InactivatedAdaptive()

Scenario['ReferenceValues'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

buildMagneticCircuitCut()

#! Flux3D 12.0
buildMagneticCircuitCut()

meshDomain()

generateSecondOrderElements()


Scenario(name='REFERENCEVALUES_1')

Scenario['REFERENCEVALUES_1'].adaptive = InactivatedAdaptive()

Scenario['REFERENCEVALUES_1'].solve(projectName='../../../../../Desktop/double_mot_test.FLU')

