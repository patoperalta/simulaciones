#! Flux3D 18.1
executeBatchSpy('C:/Users/jperalta/Documents/github_pato/flux/2_int_rotor/1_int_rotor_slotless/6_proto_1/00_main.py')

meshDomain()

generateSecondOrderElements()

buildMagneticCircuitCut()

Scenario['01_DX'].solve(projectName='../../../../../../Desktop/03_flux_int_rotor_slotless/8_market_rotors/20mm_with_hole/sims/20181011_proto_1_characterization')

saveProject()

lastInstance = Grid2DRectangularXZ(name='XZ',
                    coordSys=CoordSys['XYZ1'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['0',
                            '0',
                            '0'],
                    alongX=['R_ST_OUT',
                            'R_ST_OUT',
                            '100'],
                    alongZ=['h_rot',
                            'h_rot',
                            '50'])

startMacroTransaction()
Grid2D['XZ'].alongX=['R_ST_OUT*1.2',
                     'R_ST_OUT*1.2',
                     '100']

Grid2D['XZ'].alongZ=['H_ROT/2*1.2',
                     'H_ROT/2*1.2',
                     '50']

endMacroTransaction()

startMacroTransaction()
Grid2D['XZ'].alongX=['R_ST_OUT*1.5',
                     'R_ST_OUT*1.5',
                     '100']

Grid2D['XZ'].alongZ=['H_ROT/2*1.5',
                     'H_ROT/2*1.5',
                     '50']

endMacroTransaction()

lastInstance = IsovalueGrid2d(name='ISOVAL_1',
               formula='B',
               forceVisibility='yes',
               smoothValues='yes',
               regionInternalExternal='Automatic',
               internalComputation='no',
               regionType='volumeRegion',
               grid2d=[Grid2D['XZ']])

displayIsovalues()

lastInstance = ArrowGrid2d(name='ARROWS_1',
            forceVisibility='yes',
            grid2d=[Grid2D['XZ']],
            formula='B')

lastInstance = Grid2DRectangularYZ(name='YZ',
                    coordSys=CoordSys['XYZ1'],
                    visibility=Visibility['VISIBLE'],
                    color=Color['Turquoise'],
                    origin=['0',
                            '0',
                            '0'],
                    alongY=['R_ST_OUT*1.5',
                            'R_ST_OUT*1.5',
                            '100'],
                    alongZ=['H_ROT/2*1.5',
                            'H_ROT/2*1.5',
                            '50'])

lastInstance = ArrowGrid2d(name='ARROWS_2',
            forceVisibility='yes',
            grid2d=[Grid2D['YZ']],
            formula='B',
            regionType='volumeRegion')

saveProject()

saveProject()

displayArrows()

lastInstance = IsolineGrid2d(name='ISOLIN_1',
              formula='B',
              forceVisibility='yes',
              smoothValues='yes',
              regionInternalExternal='Automatic',
              internalComputation='no',
              regionType='volumeRegion',
              grid2d=[Grid2D['XZ']])

saveProject()

displayIsolines()

saveProject()

cleanInvalidPaths()

sep

saveProject()

i=1

cleanInvalidPaths()

saveProject()

cleanInvalidPaths()

saveProject()

sep=.5 #look at A1366 hall sensor datasheet... 

# define paths were hall sensor path will be read
for i in range(1,7):
     # radial path
     PathStraightLine2PTS(name='PRAD'+str(i),
                               pathDiscretization=DistancePathDiscretization(distance=0.5),
                               regionVolume='AIR',
                               color=Color['White'],
                               visibility=Visibility['VISIBLE'],
                               startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
                                                         uvw=['(R_ROT_OUT+3*'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ROT_OUT+3*'+str(sep)+')*Sind(60*'+str(i-1)+')', '0']),
                               endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
                                                       uvw=['(R_ST_IN-'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ST_IN-'+str(sep)+')*Sind(60*'+str(i-1)+')', '0']))

     lastInstance = CompoundPath(name='HS_R_'+str(i),
                paths=[Path['PRAD'+str(i)]],
                color=Color['Turquoise'],
                visibility=Visibility['VISIBLE'])

     cleanInvalidPaths()                                                  

     PathStraightLine2PTS(name='PAX_TOP'+str(i),
                               pathDiscretization=DistancePathDiscretization(distance=.5),
                               regionVolume='AIR',
                               color=Color['White'],
                               visibility=Visibility['VISIBLE'],
                               startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
                                                         uvw=['(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Sind(60*'+str(i-1)+')', 'H_ST/2+'+str(sep)+'']),
                               endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
                                                       uvw=['R_ST_OUT*Cosd(60*'+str(i-1)+')', 'R_ST_OUT*Sind(60*'+str(i-1)+')', 'H_ST/2+'+str(sep)+'']))


     lastInstance = CompoundPath(name='HS_AX_TOP_'+str(i),
                     paths=[Path['PAX_TOP'+str(i)]],
                     color=Color['Turquoise'],
                     visibility=Visibility['VISIBLE'])

     cleanInvalidPaths()                          
                     
     PathStraightLine2PTS(name='PAX_BOTTOM'+str(i),
                               pathDiscretization=DistancePathDiscretization(distance=.5),
                               regionVolume='AIR',
                               color=Color['White'],
                               visibility=Visibility['VISIBLE'],
                               startPoint=PathPoint(coordSys=CoordSys['XYZ1'],
                                                         uvw=['(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Cosd(60*'+str(i-1)+')', '(R_ROT_OUT+D_MECHGAP+'+str(sep)+')*Sind(60*'+str(i-1)+')', '-H_ST/2-'+str(sep)+'']),
                               endPoint=PathPoint(coordSys=CoordSys['XYZ1'],
                                                       uvw=['R_ST_OUT*Cosd(60*'+str(i-1)+')', 'R_ST_OUT*Sind(60*'+str(i-1)+')', '-H_ST/2-'+str(sep)+'']))


     lastInstance = CompoundPath(name='HS_AX_BOTTOM_'+str(i),
                     paths=[Path['PAX_BOTTOM'+str(i)]],
                     color=Color['Turquoise'],
                     visibility=Visibility['VISIBLE'])                     

     cleanInvalidPaths()

saveProject()

saveProject()

range(0,1)

range(0,5)

range(1,6)

saveProject()

CurveSpatial2D['01_DX_HS_R_1_DX_0'].delete()
folder

hr

saveProject()

closeProject()

exit()
