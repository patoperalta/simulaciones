#! Flux2D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/2_int_rotor_slotted/7_icems_journal_2018_2d/00_main.py')

deleteMesh()

saveProjectAs('../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/2d/post 3d/slotted_w_slot_tuning.FLU')

ParameterGeom['W_SLOT'].expression='6'


Scenario(name='r_10_wslot',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['r_10_wslot'].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=10.0))

Scenario['r_10_wslot'].addPilot(pilot=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                  intervals=[IntervalStepValue(minValue=6.0,
                                                                               maxValue=10.0,
                                                                               stepValue=0.5)]))

endMacroTransaction()

meshDomain()

generateSecondOrderElements()

Scenario['R_10_WSLOT'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/2d/post 3d/slotted_w_slot_tuning.FLU')

displayIsovalues()

selectCurrentStep(activeScenario=Scenario['R_10_WSLOT'],
                  parameterValue=['R_ROT_OUT=10.0',
                                  'W_SLOT=8.0'])

selectCurrentStep(activeScenario=Scenario['R_10_WSLOT'],
                  parameterValue=['R_ROT_OUT=10.0',
                                  'W_SLOT=9.0'])

selectCurrentStep(activeScenario=Scenario['R_10_WSLOT'],
                  parameterValue=['R_ROT_OUT=10.0',
                                  'W_SLOT=10.0'])

selectCurrentStep(activeScenario=Scenario['R_10_WSLOT'],
                  parameterValue=['R_ROT_OUT=10.0',
                                  'W_SLOT=6.0'])

selectCurrentStep(activeScenario=Scenario['R_10_WSLOT'],
                  parameterValue=['R_ROT_OUT=10.0',
                                  'W_SLOT=8.0'])

selectCurrentStep(activeScenario=Scenario['R_10_WSLOT'],
                  parameterValue=['R_ROT_OUT=10.0',
                                  'W_SLOT=10.0'])

Scenario(name='R_15_WSLOT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['R_15_WSLOT'].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                value=15.0))

Scenario['R_15_WSLOT'].addPilot(pilot=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                  intervals=[IntervalStepValue(minValue=10.0,
                                                                               maxValue=16.0,
                                                                               stepValue=1.0)]))

endMacroTransaction()

startMacroTransaction()
Scenario['R_15_WSLOT'].pilots['W_SLOT']=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                    intervals=[IntervalStepValue(minValue=11.0,
                                                                                 maxValue=16.0,
                                                                                 stepValue=1.0)])
endMacroTransaction()

startMacroTransaction()
Scenario['R_15_WSLOT'].pilots['W_SLOT']=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                    intervals=[IntervalStepValue(minValue=11.0,
                                                                                 maxValue=17.0,
                                                                                 stepValue=0.5)])
endMacroTransaction()

Scenario['R_15_WSLOT'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/2d/post 3d/slotted_w_slot_tuning.FLU')

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=13.0'])

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=14.0'])

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=15.0'])

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=16.0'])

lastInstance = Grid2DAnnular(name='Grid2D_WSLOT',
              coordSys=CoordSys['XY1'],
              visibility=Visibility['VISIBLE'],
              color=Color['Turquoise'],
              origin=['0',
                      '0'],
              radius=['r_rot_out+d_agap',
                      'r_st_in',
                      '50'],
              theta=['0',
                     '360',
                     '361'])

lastInstance = IsovalueGrid2d(name='ISOVAL_wslot',
               formula='B',
               forceVisibility='yes',
               smoothValues='yes',
               grid2d=[Grid2D['GRID2D_WSLOT']])

Scenario(name='R_15_WSLOT_1',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario(name='R_20_WSLOT',
         adaptive=InactivatedAdaptive())

startMacroTransaction()

Scenario['R_20_WSLOT'].addPilot(pilot=MonoValue(parameter=VariationParameter['R_ROT_OUT'],
                                                  value=20.0))

Scenario['R_20_WSLOT'].addPilot(pilot=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                    intervals=[IntervalStepValue(minValue=13.0,
                                                                                 maxValue=25.0,
                                                                                 stepValue=1.0)]))

endMacroTransaction()


selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=11.0'])

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=12.0'])

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=13.0'])

selectCurrentStep(activeScenario=Scenario['R_15_WSLOT'],
                  parameterValue=['R_ROT_OUT=15.0',
                                  'W_SLOT=14.0'])

Scenario['R_20_WSLOT'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/2d/post 3d/slotted_w_slot_tuning.FLU')

Scenario['R_20_WSLOT'].deleteAllResults()

startMacroTransaction()
Scenario['R_20_WSLOT'].pilots['W_SLOT']=MultiValues(parameter=VariationParameter['W_SLOT'],
                                                    intervals=[IntervalStepValue(minValue=16.0,
                                                                                 maxValue=22.0,
                                                                                 stepValue=1.0)])
endMacroTransaction()

Scenario['R_20_WSLOT'].solve(projectName='../../../../../../Google Drive/4_EPFL_Dropbox/10_Publications/5_ICEMS_journal/flux_simulations/2d/post 3d/slotted_w_slot_tuning.FLU')

selectCurrentStep(activeScenario=Scenario['R_20_WSLOT'],
                  parameterValue=['R_ROT_OUT=20.0',
                                  'W_SLOT=16.0'])

selectCurrentStep(activeScenario=Scenario['R_20_WSLOT'],
                  parameterValue=['R_ROT_OUT=20.0',
                                  'W_SLOT=18.0'])

selectCurrentStep(activeScenario=Scenario['R_20_WSLOT'],
                  parameterValue=['R_ROT_OUT=20.0',
                                  'W_SLOT=20.0'])

selectCurrentStep(activeScenario=Scenario['R_20_WSLOT'],
                  parameterValue=['R_ROT_OUT=20.0',
                                  'W_SLOT=22.0'])

saveProject()

closeProject()

exit()
