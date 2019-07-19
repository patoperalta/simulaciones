#design space definition
## alpha export
x0=1.0
dx=0.2
N=6
alpha=[None]*N
alpha[0]=x0
for i in range(N-1):
	alpha[i+1]=round(alpha[i]+dx,2)

## beta export
x0=0.1
dx=0.1
N=3
beta=[None]*N
beta[0]=x0
for i in range(N-1):
	beta[i+1]=round(beta[i]+dx,2)

# ## dgap
# x0=3.0			#init
# dx=1			#diff
# N=4				#length
# d_gap=[None]*N 	#initialize size
# d_gap[0]=x0		#first value
# for i in range(N-1):	
	# d_gap[i+1]=round(d_gap[i]+dx,2)	
	
## rmot
r_mot=[15]

#### path inside stator iron								  
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

#### path through slot			 
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

# to be able to export values of integral
rev='1'
mot='slotted'
dir='mot_'+mot+'/' ##create this folder manually	
								  
import sys
f = open(dir+mot+'_0_brms_a_around_teeth_rev'+rev+'_R15.csv','w')
headers = 'ALPHA_H;BETA;D_AGAP;R_ST_OUT;BRMS/A'
f.write(headers) 
f.write('\n')	 

blah='25'

for m in range(0,1):
	for l in range(0,len(r_mot)):
		for k in range(0,4):
			for j in range(0,len(beta)):
				for i in range(0,len(alpha)):
					##size of the airgap... we  have to transform it afterwards
					if r_mot[l]==10:
						d_st=8
						w_slot=7
						l_0=7.0
					elif r_mot[l]==15:
						d_st=13
						w_slot=12
						l_0=9.0
					elif r_mot[l]==20:
						d_st=18
						w_slot=16
						l_0=11.0
						
					dx=1	#diff
					N=4		#length
					l_slot=[None]*N 	#initialize size
					l_slot[0]=l_0		#first value
					for z in range(N-1):	
						l_slot[z+1]=round(l_slot[z]+dx,1)							
			
					if (alpha[i]==2 and beta[j]==0.1 and r_mot[l]==20 and l_slot[k]==11) or (alpha[i]==1.6 and beta[j]==0.3 and r_mot[l]==10 and l_slot[k]==7) or (alpha[i]==2 and beta[j]==0.1 and r_mot[l]==10 and l_slot[k]==8) or (alpha[i]==1.6 and beta[j]==0.2 and r_mot[l]==10 and l_slot[k]==8) or (alpha[i]==2 and beta[j]==0.1 and r_mot[l]==10 and l_slot[k]==8):
						print('exception')	
						brms_3D = 0;
						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(l_slot[k])+';'+str(r_mot[l])					
					else:
						print('alright')	
						aux='_alpha'+str(alpha[i])+'_beta_'+str(beta[j])+'_lslot_'+str(l_slot[k])+'_rout_'+str(r_mot[l])
						aux=aux.replace('.', '')
						
						####select the step
						selectCurrentStep(activeScenario=Scenario['0_FIELD_R'+str(r_mot[l])],
										parameterValue=['ALPHA_H='+str(alpha[i]),
														'BETA='+str(beta[j]),
														'L_SLOT='+str(l_slot[k]),
														'R_ROT_OUT='+str(r_mot[l]),
														'W_SLOT='+str(w_slot),
														'D_ST='+str(d_st)])
						#circle in rotor
						#do curve
						SpatialCurve(name='perimeter'+blah+aux,
						compoundPath=CompoundPath['FE_PER'],
								formula=['Comp(1,B)',
								'Comp(2,B)',
								'Comp(3,B)'])
						# export 
						CurveSpatial2D['perimeter'+blah+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/perimeter_int_rotor_slotted'+aux,
								mode='add')

						# slot
						SpatialCurve(name='slot'+blah+aux,
							compoundPath=CompoundPath['FE_SLOT'],
							formula=['Comp(1,B)',
									 'Comp(2,B)',
									 'Comp(3,B)'])		

						CurveSpatial2D['slot'+blah+aux].exportExcel(xlsFile=dir+mot+'_b_fields_out_rev'+rev+'/slot_int_rotor_slotted'+aux,
							mode='add')					

						#### around teeth
						bsquare= IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
									   spatialFormula='Comp(1,B)^2+Comp(2,B)^2+Comp(3,B)^2',
									   resultName='IntegralVol_1_B_'+blah+'_'+aux)
						
						vol= IntegralVolume(support=SupportIntegralRegionVolume(region=[RegionVolume['COIL_6']]),
									   spatialFormula='1',
									   resultName='IntegralVol_1_'+blah+'_'+aux)
						
						brms_3D = sqrt(bsquare.value/vol.value);
							
						values_scn=str(alpha[i])+';'+str(beta[j])+';'+str(l_slot[k])+';'+str(r_mot[l])	
					
					#write
					line=values_scn+';'+str(brms_3D)+'\n'
					f.write(line)
					n=n+1	#counter
f.close()
n