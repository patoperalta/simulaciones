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
# n=n+1	#counter