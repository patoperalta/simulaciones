#! Flux3D 12.0


print("FICHIER PARAM.PY\n")
##################################################################################################################################################################
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## define the motor by the radius of bearing pm
lastInstance = ParameterGeom(name='R_B_PM_ROT_OUT : outer radius of rotor bearing pm',
              expression='10')

##now, define the airgap and the stator thickness, then we know the total radius of the motor
lastInstance = ParameterGeom(name='D_AGAP_B : bearing air gap',
              expression='1.5')
			  
lastInstance = ParameterGeom(name='D_ST_B : radial thickness of bearing stator and its PMs',
              expression='1')				  
			  
##PARAMETERS FOR BEARING STATOR
lastInstance = ParameterGeom(name='R_B_ST_OUT : outer radius of bearing stator',
              expression='R_B_PM_ROT_OUT+D_AGAP_B+D_ST_B')

lastInstance = ParameterGeom(name='D_MOT : diameter of whole motor magnetics',
              expression='2*R_B_ST_OUT')

##rotor height and diameter parameters			  
lastInstance = ParameterGeom(name='ALPHA_H : ratio h_rot/H_B_ST',
              expression='1.8')

lastInstance = ParameterGeom(name='ALPHA_CASE : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = ParameterGeom(name='beta_b : bearing, times total diameter gives away motor height if alpha_h <= 1',
              expression='.2')
			  
lastInstance = ParameterGeom(name='beta_d : drive, times total diameter gives away motor height if alpha_h <= 1',
              expression='.5')			  

## height of the bearing stator			  
lastInstance = ParameterGeom(name='H_B_ST : bearing stator height, f(dmot,alpha,beta_b) ',
              expression='D_MOT*(ALPHA_CASE*beta_b+(1-ALPHA_CASE)*beta_b/ALPHA_H)')

##total height of pms in bearing stator, that it, each pm has the half of this percentage			  
lastInstance = ParameterGeom(name='H_PER_PM_ST_B : %(h of pm  / total height) of stator bearing',
              expression='.6')  			  

##each pm with half the height
lastInstance = ParameterGeom(name='H_PM_ST_B : actual height of each pm of bearing stator',
              expression='H_PER_PM_ST_B*H_B_ST/2')
##total iron			  
lastInstance = ParameterGeom(name='H_FE_ST_B : iron height of bearing stator ',
              expression='H_B_ST-2*H_PM_ST_B')			  

##start with rotor			  
lastInstance = ParameterGeom(name='H_ROT_B : rotor height',
              expression='d_mot*(alpha_case*alpha_h*beta_b+(1-alpha_case)*beta_b)')
			  
lastInstance = ParameterGeom(name='H_DRV : drive height',
              expression='d_mot*beta_d')			  
		  			  
lastInstance = ParameterGeom(name='D_PM_B_ROT : thickness of rotor bearing pm',
              expression='1')	

##amount of pm and fe in bearing rotor
lastInstance = ParameterGeom(name='H_PER_PM_ROT_B : %(h of pm  / total height) of rotor of bearing',
              expression='0.8')

lastInstance = ParameterGeom(name='H_FE_ROT_B : iron height of rotor of bearing',
              expression='H_ROT_B*(1-H_PER_PM_ROT_B)')

lastInstance = ParameterGeom(name='H_PM_ROT_B : iron height of rotor of bearing',
              expression='H_ROT_B*H_PER_PM_ROT_B/2')			  
			  
##PARAMETERS FOR ROTOR DISPLACEMENT
lastInstance = ParameterGeom(name='DTHETA',
              expression='0')

lastInstance = ParameterGeom(name='DALPHA',
              expression='0')

lastInstance = ParameterGeom(name='DBETA',
              expression='0')

lastInstance = ParameterGeom(name='DX',
              expression='0')

lastInstance = ParameterGeom(name='DY',
              expression='0')

lastInstance = ParameterGeom(name='X_H_DIFF : abs val of height dif between st and rot',
              expression='0')			  
			  
lastInstance = ParameterGeom(name='DZ',
              expression='0')	

lastInstance = ParameterGeom(name='DR_0',
              expression='0')

lastInstance = ParameterGeom(name='DTHETA_0',
              expression='0')				  

##DRIVE MOTOR	
##separation between inner radius of bearing rotor and outer radius of drive rotor
lastInstance = ParameterGeom(name='R_SEP : separation between rotor bearing magnet and drive iron',
              expression='3.5')	

##drive stator			  
lastInstance = ParameterGeom(name='R_DRV_ST_OUT : outer radius of drive stator',
              expression='(R_B_PM_ROT_OUT-D_PM_B_ROT-R_SEP)')
			  
lastInstance = ParameterGeom(name='D_DRV_ST : drive stator thickness',
              expression='1')			  
			  
##drive airgap			  
lastInstance = ParameterGeom(name='D_AGAP_D : drive airgap',
              expression='2.5')

##rotor
lastInstance = ParameterGeom(name='R_DRV_ROT_OUT : outer radius drive rotor',
              expression='R_DRV_ST_OUT-D_DRV_ST-D_AGAP_D')