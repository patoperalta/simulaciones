selectCurrentStep(activeScenario=Scenario['10_DX'],
                  parameterValue=['ALPHA_H=1.4',
                                  'D_ST=9.0',
                                  'DX=0.5'])

f_pass = computeForceElecMagVolumeRegion(volumeRegion=[RegionVolume['IRON_ST']],
                                resultName='f_pass_fe')

selectCurrentStep(activeScenario=Scenario['9_FORCE'],
                  parameterValue=['ALPHA_H=1.4',
                                  'D_ST=9.0',
                                  'JF_RMS=6.0'])

f_act = computeForceElecMagVolumeRegion(volumeRegion=[RegionVolume['PM']],
                                resultName='fe_act_pm')
								
theta_f = ComputeCurrentValueParameter(formula='IF_HAT',
                             result='theta_jf6')
								
aturns_startup= abs(f_pass.value[0].value/f_act.value[0].value*theta_f.value)
aturns_startup