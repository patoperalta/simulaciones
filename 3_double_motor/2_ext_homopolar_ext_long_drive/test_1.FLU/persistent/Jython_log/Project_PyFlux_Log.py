#! Flux3D 18.1


# Your project log file has become too 
# large and it is unsafe to open in Flux.
# It has been archived as C:\Users\jperalta\Documents\github_pato\flux\3_double_motor\1_ext_homopolar_int_long_drive\..\2_ext_homopolar_ext_long_drive\test_1.FLU\persistent\Jython_log\Project_PyFlux_Log_0.py.
# If needed, consider opening it in a high 
# performance dedicated editor.

saveProjectAs('../2_ext_homopolar_ext_long_drive/test_1.FLU')

##for aesthetic purposes
lastInstance = ParameterGeom(name='BNG_M_R_THEO : m * x + n',
              expression='.15')     
                 
lastInstance = ParameterGeom(name='BNG_N_R_THEO : m * x + n',
              expression='0')                 

lastInstance = ParameterGeom(name='BNG_COIL_R_THEO : theoretical coil radial thickness, see excel',
              expression='BNG_M_R_THEO*R_OUT_ST_BNG+BNG_N_R_THEO')     
                 
lastInstance = ParameterGeom(name='BNG_COIL_R_CASE : if 0, max coil thickness is limited by airgap',
              expression='Valid(BNG_COIL_R_THEO,0,D_AGAP_B-1)')                      

lastInstance = ParameterGeom(name='BNG_COIL_R : real coil radial thickness, see excel v2',
              expression='BNG_COIL_R_CASE*BNG_COIL_R_THEO+(1-BNG_COIL_R_CASE)*(D_AGAP_B-1)')     
                 
lastInstance = ParameterGeom(name='BNG_COIL_WCOIL : toroidal coil width, motor is very small, so width also',
              expression='2*pi()/6*(R_OUT_ST_BNG-D_ST_B-BNG_COIL_R)*0+3')          

lastInstance = VariationParameterFormula(name='BNG_H_L_PH : height of the bearing coil',
                          formula='2*R_OUT_PM_ROT_BNG*(ALPHA_CASE_PH*BETA_B+(1-ALPHA_CASE_PH)*BETA_B/ALPHA_H)')                         

lastInstance = VariationParameterFormula(name='BNG_L_BAR_PH',
                          formula='2*(BNG_H_L_PH+D_ST_B)+2*pi()*BNG_TH_COIL_CIRC/2')     

##everything ready for the resistance                                
lastInstance = VariationParameterFormula(name='BNG_R_COIL',
                          formula='rho_cu*BNG_H_L_PH*1e-3/(BNG_A_CU*1e-6)')               

##force
lastInstance = VariationParameterPilot(name='BNG_I_F_PEAK : peak value of force excitation, ATURNS',
                        referenceValue=0.0)

lastInstance = VariationParameterPilot(name='BNG_THETA_F0 : if 90, and THETA_F is 0, force goes in x direction',
                        referenceValue=0)

lastInstance = VariationParameterPilot(name='BNG_THETA_F_DIR : gives force direction in stator coordinates',
                        referenceValue=0.0)
                              
lastInstance = VariationParameterFormula(name='BNG_THETA_F : force direction angle degrees',
                        formula='BNG_THETA_F0-BNG_THETA_F_DIR')                              
     
lastInstance = VariationParameterPilot(name='BNG_JF_RMS : force current density',
                        referenceValue=0.0)                                                              
                              
lastInstance = VariationParameterFormula(name='BNG_IF_HAT',
                          formula='(BNG_I_F_PEAK+BNG_JF_RMS*BNG_A_CU*sqrt(2))')          



##coordinate systems, currents and coils
for i in range(1,7):
     ## coordinate system for coils
     lastInstance = CoordSysCartesian(name='COORD_COIL_BNG_'+str(i),
                         parentCoordSys=GlobalUnits(lengthUnit=LengthUnit['MILLIMETER'],
                                                            angleUnit=AngleUnit['DEGREE']),
                         origin=['(R_OUT_ST_BNG-1/2*D_ST_B)*cosd(60*'+str(i-1)+')',
                                   '(R_OUT_ST_BNG-1/2*D_ST_B)*sind(60*'+str(i-1)+')',
                                   '0'],
                         rotationAngles=RotationAngles(angleX='90',
                                                                 angleY='60*'+str(i-1)+'',
                                                                 angleZ='0'),
                         visibility=Visibility['VISIBLE'])                    
     ##### equations for force current                                     
     lastInstance = VariationParameterFormula(name='I_F_'+str(i),
                                     formula='BNG_IF_HAT*Cosd(2*DTHETA-BNG_THETA_F+'+str((i-1)*60)+')')
     #####      define current                                   
     lastInstance = CurrentStrandedCoil(name='I_BNG_'+str(i)+' : current in first drive coil',
                              rmsModulus='I_F_'+str(i))                                     
     #####      do coils
     lastInstance = CoilRectangular(name='Coil_BNG_'+str(i),
                strandedCoil=CoilConductor['I_BNG_'+str(i)],
                turnNumber='1',
                seriesOrParallel=AllInSeries(),
                coilDuplicationBySymmetriesPeriodicities=CoilDuplication(),
                coordSys=CoordSys['COORD_COIL_BNG_'+str(i)],
                center=['0',
                        '0',
                        '0'],
                dimensions=['D_ST_B+BNG_COIL_R',
                            'H_ST_BNG+BNG_COIL_R'],
                filletRadius='.1',
                section=ComposedCoilRectangularSection(height='BNG_COIL_WCOIL',
                                                       width='BNG_COIL_R'),
                fillFactor='1',
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])                                     

ParameterGeom['DX'].expression='.5'


ParameterGeom['DX'].expression='0'


ParameterGeom['DY'].expression='.5'


ParameterGeom['DY'].expression='0'


######BNG STATOR

lastInstance = VariationParameterFormula(name='R_OUT_ST_BNG_AUX : aux for outer radius of bearing stator',
                          formula='R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG')

lastInstance = VariationParameterFormula(name='A_BNG_ST : circular base area of bearing rotor',
                          formula='pi()*(R_OUT_ST_BNG_AUX^2-(R_OUT_ST_BNG_AUX-D_ST_BNG)^2)')
                                
lastInstance = VariationParameterFormula(name='D_MOT_AUX : ',
                          formula='2*(R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG)')     

lastInstance = VariationParameterFormula(name='ALPHA_CASE_AUX : ',
                          formula='ValidLR(ALPHA_H,0,1,1,1)')                                     

lastInstance = VariationParameterFormula(name='H_ST_BNG_AUX : height of BNG stator',
                          formula='D_MOT_AUX*(ALPHA_CASE_AUX*BETA_B+(1-ALPHA_CASE_AUX)*BETA_B/ALPHA_H)')                                
                                
lastInstance = VariationParameterFormula(name='H_PM_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_PERCENT_PM_TO_FE_BNG_ST*H_ST_BNG_AUX/2')                                
                                
lastInstance = VariationParameterFormula(name='H_FE_BNG_ST_AUX : height of one rotor BNG PM',
                          formula='H_ST_BNG_AUX-2*H_PM_BNG_ST_AUX')                                

lastInstance = VariationParameterFormula(name='V_PM_BNG_ST : means ONE magnet, so count double the volume at end x2',
                          formula='A_BNG_ST*H_PM_BNG_ST_AUX')

lastInstance = VariationParameterFormula(name='V_FE_BNG_ST : ',
                          formula='A_BNG_ST*H_FE_BNG_ST_AUX')
                                
############################### BNG ROTOR
                                
lastInstance = VariationParameterFormula(name='A_BNG_ROT : circular base area of bearing rotor',
                          formula='pi()*(R_OUT_PM_ROT_BNG^2-(R_OUT_PM_ROT_BNG-D_PM_B_ROT)^2)')

lastInstance = VariationParameterFormula(name='H_ROT_B_AUX : height of BNG rotor',
                          formula='D_MOT_AUX*(ALPHA_CASE_AUX*ALPHA_H*BETA_B+(1-ALPHA_CASE_AUX)*BETA_B)')                                                                
                                
lastInstance = VariationParameterFormula(name='H_PM_ROT_B_AUX : height of one rotor BNG PM',
                          formula='H_ROT_B_AUX*H_PERCENT_PM_TO_FE_BNG_ROT/2')     
                                
lastInstance = VariationParameterFormula(name='V_PM_BNG_ROT : considers only one pm ring',
                          formula='A_BNG_ROT*H_PM_ROT_B_AUX')
                                
lastInstance = VariationParameterFormula(name='V_FE_BNG_ROT : ',
                          formula='A_BNG_ROT*H_ROT_B_AUX*(1-H_PERCENT_PM_TO_FE_BNG_ROT)')     

lastInstance = VariationParameterFormula(name='D_DR_FE_ROT_PH : aux for fe_drv_rot',
                          formula='K_D_DR_FE_ROT*R_OUT_PM_ROT_BNG')

lastInstance = VariationParameterFormula(name='R_ROT_OUT_DRV_AUX : out radius of drv rotor',
                          formula='(R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP)')

lastInstance = VariationParameterFormula(name='A_FE_DRV_ROT : area of drive rotor FE ',
                          formula='pi()*(R_ROT_OUT_DRV_AUX^2-(R_ROT_OUT_DRV_AUX-D_DR_FE_ROT_PH)^2)')     

lastInstance = VariationParameterFormula(name='V_FE_DRV_ROT : volume iron in drive rotor',
                          formula='A_FE_DRV_ROT*D_MOT_AUX*beta_d')

lastInstance = VariationParameterFormula(name='D_DR_PM_PH : aux for pm_drv_rot, pm drive rotor thickness',
                          formula='K_D_DR_PM*R_OUT_PM_ROT_BNG')     

lastInstance = VariationParameterFormula(name='R_OUT_PM : aux once again, outer radius drive pms',
                          formula='R_ROT_OUT_DRV_AUX-D_DR_FE_ROT_PH')

lastInstance = VariationParameterFormula(name='V_PM_DRV_ROT',
                          formula='pi()*(R_OUT_PM-(R_OUT_PM-D_DR_PM_PH)^2)*D_MOT_AUX*beta_d*THETA_MAG/90')     

saveProject()

saveProject()

#! Flux3D 18.1
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
lastInstance = RegionVolume(name='DRV_ROT_PM_R_1',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='DRV_ROT_PM_R_2',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='DRV_ROT_PM_R_3',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

lastInstance = RegionVolume(name='DRV_ROT_PM_R_4',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['BMT_42UH']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])
                
lastInstance = RegionVolume(name='DRV_ROT_IRON_D',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])                
                
##drive stator
lastInstance = RegionVolume(name='DRV_ST_IRON_D',
             magneticDC3D=MagneticDC3DVolumeMagnetic(material=Material['Cogent_M270_50A_50Hz']),
             color=Color['Turquoise'],
             visibility=Visibility['VISIBLE'])

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

Volume[8].assignRegion(region=RegionVolume['DRV_ROT_IRON_D'])

Volume[9].assignRegion(region=RegionVolume['DRV_ROT_PM_R_1'])

Volume[10].assignRegion(region=RegionVolume['DRV_ROT_PM_R_2'])

Volume[11].assignRegion(region=RegionVolume['DRV_ROT_PM_R_3'])

Volume[12].assignRegion(region=RegionVolume['DRV_ROT_PM_R_4'])

Volume[13].assignRegion(region=RegionVolume['DRV_ST_IRON_D'])



##for air
assignRegionToVolumes(volume=[Volume[3],
                              Volume[14],
                              Volume[15],
                              Volume[16],
                              Volume[17],
                              Volume[18],
                              Volume[19]],
                      region=RegionVolume['AIR'])

##orient radial magnets
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_1'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='0')
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_2'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='270')
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_3'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='180')
orientRegVolMaterial(region=RegionVolume['DRV_ROT_PM_R_4'],coordSys=CoordSys['COORD_SYS_ROT'],orientation='Direction',angle='90')           

## orient vertical pms of bearing stator
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_TOP'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',center=['0','0','0'],angle='0')
orientRegVolMaterial(region=RegionVolume['BNG_ST_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ST_VERT'],orientation='Direction',angle='180')

## orient vertical pms of bearing rotor
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_TOP'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',center=['0','0','0'],angle='180')
orientRegVolMaterial(region=RegionVolume['BNG_ROT_PM_BOTTOM'],coordSys=CoordSys['COORD_SYS_ROT_VERT'],orientation='Direction',angle='0')

#########################################################################################################################################################                 
##appeareance
#########################################################################################################################################################        
##change colors
RegionVolume['DRV_ROT_IRON_D','BNG_ST_IRON','DRV_ST_IRON_D'].color=Color['Black']

RegionVolume['BNG_ST_PM_BOTTOM','BNG_ROT_PM_TOP','DRV_ROT_PM_R_1','DRV_ROT_PM_R_3'].color=Color['Red']

RegionVolume['BNG_ST_PM_TOP','BNG_ROT_PM_BOTTOM','DRV_ROT_PM_R_2','DRV_ROT_PM_R_4'].color=Color['Green']

RegionVolume['AIR'].setInvisible()

saveProject()

meshDomain()

displayArrowsOnMagnet()

deleteArrows()

deleteMesh()

saveProject()

