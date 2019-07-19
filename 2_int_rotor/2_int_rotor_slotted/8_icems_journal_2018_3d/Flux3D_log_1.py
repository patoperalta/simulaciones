#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/8_icems_journal_2018_3d/00_main.py')

deleteMesh()

ParameterGeom['L_SLOT'].expression='7'


AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.85)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowAssigned(type=MeshShadowHigh()))


alpha=2
beta=0.1
l_slot=8
rrot=10
n=25

Scenario(name='BRMS_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

endMacroTransaction()

meshDomain()

generateSecondOrderElements()

Scenario['BRMS_25'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_1.FLU')

result = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
               resultName='IntegralVol_1')

result = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               spatialFormula='1',
               resultName='IntegralVol_2')

saveProject()

alpha=2
beta=0.1
l_slot=11
rrot=20
n=151

Scenario(name='BRMS_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['BRMS_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

endMacroTransaction()

Scenario['BRMS_151'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_1.FLU')

result = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
               resultName='IntegralVol_3')

result = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               spatialFormula='1',
               resultName='IntegralVol_4')

saveProject()

selectCurrentStep(activeScenario=Scenario['BRMS_25'],
                  parameterValue=['ALPHA_H=2.0',
                                  'BETA=0.1',
                                  'L_SLOT=8.0',
                                  'R_ROT_OUT=10.0'])

# path inside stator iron                                          
PathArcCenterAngle(name='Path_1',
                   pathDiscretization=PointPathDiscretization(pointNumber=1024),
                   regionVolume='IRON_ST',
                   color=Color['White'],
                   visibility=Visibility['VISIBLE'],
                   coordSys=CoordSys['COORD_SYS_ST'],
                   centerCoord=['0',
                                '0',
                                'h_st/2'],
                   angle=['0',
                          '359'],
                   radius='.5*(R_ST_OUT+R_ST_IN)')

lastInstance = CompoundPath(name='FE_PER',
             paths=[Path['PATH_1']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])     

# path through slot                
PathStraightLine2PTS(name='PATH_2',
                     pathDiscretization=PointPathDiscretization(pointNumber=1024),
                     color=Color['White'],
                     visibility=Visibility['VISIBLE'],
                     startPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                          uvw=['(R_ROT_OUT+D_AGAP)*Cosd(30)', '(R_ROT_OUT+D_AGAP)*Sind(30)', 'h_st/2']),
                     endPoint=PathPoint(coordSys=CoordSys['COORD_SYS_ST'],
                                        uvw=['(R_ROT_OUT+D_AGAP+L_SLOT)*Cosd(30)', '(R_ROT_OUT+D_AGAP+L_SLOT)*Sind(30)', 'h_st/2']))                
                                          
lastInstance = CompoundPath(name='FE_SLOT',
             paths=[Path['PATH_2']],
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

n=1

alpha='20'
beta='01'
lslot='80'
rout='10'
name=alpha+'_BETA_'+beta+'_LSLOT_'+lslot+'_ROUT_'+rout

# n=n+1

SpatialCurve(name='PERIMETER_INT_SLOTTED_ALPHA_'+name,
             compoundPath=CompoundPath['FE_PER'],
             formula=['Comp(1,B)',
                      'Comp(2,B)',
                      'Comp(3,B)'])

# CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_'+name].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_'+name,
            # mode='add')

SpatialCurve(name='SLOT_INT_SLOTTED_ALPHA_'+name,
             compoundPath=CompoundPath['FE_SLOT'],
             formula=['Comp(1,B)',
                      'Comp(2,B)',
                      'Comp(3,B)'])

# CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_'+name].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/SLOT_INT_SLOTTED_ALPHA_'+name,
            # mode='add')

# bsquare = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               # spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
               # resultName='IntegralVol_'+str(n))


# vol = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               # spatialFormula='1',
               # resultName='IntegralVol_'+str(n))

# f = open(dir+mot+'_0_brms_a_around_teeth_rev'+str(1)+'_'+name+'.csv','w')
# headers = 'ALPHA_H;BETA;L_SLOT;R_ST_OUT;BRMS/A'
# f.write(headers) 
# f.write('\n')
# line=values_scn+';'+str(brms_3D)+'\n'
# f.write(line)
# f.close()
# n=n+1     #counter

n=1

alpha='20'
beta='01'
lslot='11'
rout='20'
name=alpha+'_BETA_'+beta+'_LSLOT_'+lslot+'_ROUT_'+rout

# n=n+1

SpatialCurve(name='PERIMETER_INT_SLOTTED_ALPHA_'+name,
             compoundPath=CompoundPath['FE_PER'],
             formula=['Comp(1,B)',
                      'Comp(2,B)',
                      'Comp(3,B)'])

# CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_'+name].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_'+name,
            # mode='add')

SpatialCurve(name='SLOT_INT_SLOTTED_ALPHA_'+name,
             compoundPath=CompoundPath['FE_SLOT'],
             formula=['Comp(1,B)',
                      'Comp(2,B)',
                      'Comp(3,B)'])

# CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_'+name].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/SLOT_INT_SLOTTED_ALPHA_'+name,
            # mode='add')

# bsquare = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               # spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
               # resultName='IntegralVol_'+str(n))


# vol = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               # spatialFormula='1',
               # resultName='IntegralVol_'+str(n))

# f = open(dir+mot+'_0_brms_a_around_teeth_rev'+str(1)+'_'+name+'.csv','w')
# headers = 'ALPHA_H;BETA;L_SLOT;R_ST_OUT;BRMS/A'
# f.write(headers) 
# f.write('\n')
# line=values_scn+';'+str(brms_3D)+'\n'
# f.write(line)
# f.close()
# n=n+1     #counter

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20.xls',
            mode='add')

Curve2d['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].visible=0

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_08_ROUT_10.xls',
            mode='add')

Curve2d['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].visible=0

CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].DisplayCurve()

CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].DisplayCurve()

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_08_ROUT_10.xls',
            mode='add')

Curve2d['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].visible=0

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20.xls',
            mode='add')

selectCurrentStep(activeScenario=Scenario['BRMS_151'],
                  parameterValue=['ALPHA_H=2.0',
                                  'BETA=0.1',
                                  'L_SLOT=11.0',
                                  'R_ROT_OUT=20.0'])

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20','SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].delete()
CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_08_ROUT_10.xls',
            mode='add')

n=1

alpha='20'
beta='01'
lslot='11'
rout='20'
name=alpha+'_BETA_'+beta+'_LSLOT_'+lslot+'_ROUT_'+rout

# n=n+1

SpatialCurve(name='PERIMETER_INT_SLOTTED_ALPHA_'+name,
             compoundPath=CompoundPath['FE_PER'],
             formula=['Comp(1,B)',
                      'Comp(2,B)',
                      'Comp(3,B)'])

# CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_'+name].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_'+name,
            # mode='add')

SpatialCurve(name='SLOT_INT_SLOTTED_ALPHA_'+name,
             compoundPath=CompoundPath['FE_SLOT'],
             formula=['Comp(1,B)',
                      'Comp(2,B)',
                      'Comp(3,B)'])

# CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_'+name].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/SLOT_INT_SLOTTED_ALPHA_'+name,
            # mode='add')

# bsquare = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               # spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
               # resultName='IntegralVol_'+str(n))


# vol = IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
               # spatialFormula='1',
               # resultName='IntegralVol_'+str(n))

# f = open(dir+mot+'_0_brms_a_around_teeth_rev'+str(1)+'_'+name+'.csv','w')
# headers = 'ALPHA_H;BETA;L_SLOT;R_ST_OUT;BRMS/A'
# f.write(headers) 
# f.write('\n')
# line=values_scn+';'+str(brms_3D)+'\n'
# f.write(line)
# f.close()
# n=n+1     #counter

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20.xls',
            mode='add')

CurveSpatial2D['PERIMETER_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].HideCurve()

Curve2d['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_80_ROUT_10'].visible=0

CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].HideCurve()

CurveSpatial2D['SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20'].exportExcel(xlsFile='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/results_missing_sims/SLOT_INT_SLOTTED_ALPHA_20_BETA_01_LSLOT_11_ROUT_20.xls',
            mode='add')

saveProject()

saveProject()

saveProjectAs('../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

alpha=1.4
beta=0.3
l_slot=7
rrot=10
n=16

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_16'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

alpha=1.8
beta=0.3
l_slot=7
rrot=10
n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_18'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

alpha=2
beta=0.1
l_slot=8
rrot=10
n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_25'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

alpha=1.6
beta=0.2
l_slot=8
rrot=10
n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_29'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

alpha=1
beta=0.3
l_slot=9
rrot=15
n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_86'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

alpha=1.2
beta=0.3
l_slot=9
rrot=15
n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_87'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DX_86'].deleteAllResults()

Scenario['DX_87'].deleteAllResults()

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

alpha=1
beta=0.3
l_slot=10
rrot=15
n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_104'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DX_104'].deleteAllResults()

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

alpha=1.2
beta=0.3
l_slot=10
rrot=15
n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

alpha=1
beta=0.3
l_slot=11
rrot=15
n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_122'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DX_122'].deleteAllResults()

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

alpha=1
beta=0.3
l_slot=11
rrot=15
n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_158'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['BRMS_151'].deleteAllResults()

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

alpha=1
beta=0.3
l_slot=12
rrot=20
n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_176'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DX_176'].deleteAllResults()

# alpha=1.4
# beta=0.3
# l_slot=7
# rrot=10
# n=16

# alpha=1.8
# beta=0.3
# l_slot=7
# rrot=10
# n=18

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

alpha=1
beta=0.3
l_slot=13
rrot=20
n=194

Scenario(name='DX_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

endMacroTransaction()

startMacroTransaction()

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DX_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))
endMacroTransaction()

Scenario['DX_194'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DX_194'].deleteAllResults()

selectCurrentStep(activeScenario=Scenario['DX_16'],
                  parameterValue=['ALPHA_H=1.4',
                                  'BETA=0.3',
                                  'L_SLOT=7.0',
                                  'R_ROT_OUT=10.0',
                                  'DX_MULT=1.0'])

alpha=1.4
beta=0.2
l_slot=7
rrot=10
n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

Scenario['DY_10'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

alpha=2
beta=0.1
l_slot=8
rrot=10
n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

alpha=1.6
beta=0.2
l_slot=8
rrot=10
n=29

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

alpha=1
beta=0.3
l_slot=9
rrot=15
n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

alpha=1.2
beta=0.3
l_slot=9
rrot=15
n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

alpha=1
beta=0.3
l_slot=10
rrot=15
n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

alpha=1.2
beta=0.3
l_slot=10
rrot=15
n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

alpha=1
beta=0.3
l_slot=11
rrot=15
n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

alpha=1
beta=0.3
l_slot=11
rrot=20
n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

alpha=1
beta=0.3
l_slot=12
rrot=20
n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

alpha=1
beta=0.3
l_slot=13
rrot=20
n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

alpha=1.2
beta=0.3
l_slot=13
rrot=20
n=195

# alpha=1
# beta=0.3
# l_slot=14
# rrot=20
# n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

# alpha=1.4
# beta=0.2
# l_slot=7
# rrot=10
# n=10

# alpha=2
# beta=0.1
# l_slot=8
# rrot=10
# n=25

# alpha=1.6
# beta=0.2
# l_slot=8
# rrot=10
# n=29

# alpha=1
# beta=0.3
# l_slot=9
# rrot=15
# n=86

# alpha=1.2
# beta=0.3
# l_slot=9
# rrot=15
# n=87

# alpha=1
# beta=0.3
# l_slot=10
# rrot=15
# n=104

# alpha=1.2
# beta=0.3
# l_slot=10
# rrot=15
# n=105

# alpha=1
# beta=0.3
# l_slot=11
# rrot=15
# n=122

# alpha=1
# beta=0.3
# l_slot=11
# rrot=20
# n=158

# alpha=1
# beta=0.3
# l_slot=12
# rrot=20
# n=176

# alpha=1
# beta=0.3
# l_slot=13
# rrot=20
# n=194

# alpha=1.2
# beta=0.3
# l_slot=13
# rrot=20
# n=195

alpha=1
beta=0.3
l_slot=14
rrot=20
n=212


Scenario(name='DY_'+str(n),
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['ALPHA_H'],
                                           value=alpha))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['BETA'],
                                           value=beta))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['L_SLOT'],
                                           value=l_slot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                           value=rrot))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DTHETA'],
                                           value=90))

Scenario['DY_'+str(n)].addPilot(pilot=MonoValue(parameter=VariationParameter['DX_MULT'],
                                           value=1.0))

endMacroTransaction()

Scenario['DY_25'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DY_29'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

saveProject()

Scenario['DY_86'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_2.FLU')

Scenario['DY_86'].deleteAllResults()

saveProjectAs('../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_3.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.85)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowAssigned(type=MeshShadowUser(value=0.9)))


checkMesh()

Scenario['DX_86'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_3.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.95)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowAssigned(type=MeshShadowUser(value=0.9)))


Scenario['DX_86'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_3.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

deleteMesh()

AidedMesh[1].aidedMeshState=AidedMeshActivated(meshPoint=MeshPointAssigned(type=MeshPointDynamic()),
                                               meshDeviation=MeshDeviationAssignedExcludeIB(type=MeshDeviationExcludeIBRelative(value=0.95)),
                                               meshRelaxation=MeshRelaxation(lineMeshRelaxation=LineMeshRelaxationAssigned(type=LineMeshRelaxationLow()),
                                                                             faceMeshRelaxation=FaceMeshRelaxationAssigned(type=FaceMeshRelaxationLow()),
                                                                             volumeMeshRelaxation=VolumeMeshRelaxationAssigned(type=VolumeMeshRelaxationLow())),
                                               meshShadow=MeshShadowAssigned(type=MeshShadowUser(value=0.95)))


meshDomain()

generateSecondOrderElements()

Scenario['DX_86'].solve(projectName='../../../../../../Desktop/02_flux_int_rotor_slotted/6_icems_journal_3d/20190717_slotted_missing_sims_v2_3.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

Volume[ALL].meshGenerator=MeshGenerator['AUTOMATIC']


deleteMesh()

closeProject()

exit()
