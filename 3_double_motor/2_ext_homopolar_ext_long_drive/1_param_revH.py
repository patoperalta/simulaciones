#! Flux3D 18.1


print("FICHIER PARAM.PY\n")
##################################################################################################################################################################
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## define the motor by the radius of bearing pm
# lastInstance = ParameterGeom(name='R_OUT_PM_ROT_BNG : outer radius of rotor bearing pm',
              # expression='10')
lastInstance = ParameterGeom(name='R_OUT_PM_ROT_BNG : outer radius of rotor bearing pm',
              expression='10')			  

##now, define the airgap and the stator thickness, then we know the total radius of the motor
lastInstance = ParameterGeom(name='D_AGAP_B : bearing air gap',
              expression='1.5')
			  
lastInstance = ParameterGeom(name='D_ST_BNG : radial thickness of bearing stator and its PMs',
              expression='1')				  
			  
##PARAMETERS FOR BEARING STATOR
lastInstance = ParameterGeom(name='R_OUT_ST_BNG : outer radius of bearing stator',
              expression='R_OUT_PM_ROT_BNG+D_AGAP_B+D_ST_BNG')

lastInstance = ParameterGeom(name='D_MOT : diameter of whole motor magnetics',
              expression='2*R_OUT_ST_BNG')

##rotor height and diameter parameters			  
lastInstance = ParameterGeom(name='ALPHA_H : ratio H_ROT_B/H_ST_BNG',
              expression='1.8')

lastInstance = ParameterGeom(name='ALPHA_CASE : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = ParameterGeom(name='beta_b : times total diameter gives away motor height if alpha_h <= 1',
              expression='.2')
			  
lastInstance = ParameterGeom(name='beta_d : times total diameter gives away motor height if alpha_h <= 1',
              expression='.5')			  

lastInstance = ParameterGeom(name='H_DRV : total drive height',
              expression='d_mot*beta_d')			  
			  
## height of the bearing stator			  
lastInstance = ParameterGeom(name='H_ST_BNG : bearing stator height, f(dmot,alpha,beta_b) ',
              expression='D_MOT*(ALPHA_CASE*beta_b+(1-ALPHA_CASE)*beta_b/ALPHA_H)')

##total height of pms in bearing stator, that it, each pm has the half of this percentage			  
lastInstance = ParameterGeom(name='H_PERCENT_PM_TO_FE_BNG_ST : %(h of pm  / total height) of stator bearing',
              expression='.6')  			  

##each pm with half the height
lastInstance = ParameterGeom(name='H_PM_BNG_ST : actual height of each pm of bearing stator',
              expression='H_PERCENT_PM_TO_FE_BNG_ST*H_ST_BNG/2')
			  
##total iron			  
lastInstance = ParameterGeom(name='H_FE_BNG_ST : iron height of bearing stator ',
              expression='H_ST_BNG-2*H_PM_BNG_ST')			  

##start with rotor			  
lastInstance = ParameterGeom(name='H_ROT_B : rotor height',
              expression='d_mot*(alpha_case*alpha_h*beta_b+(1-alpha_case)*beta_b)')
		  			  
lastInstance = ParameterGeom(name='D_PM_B_ROT : thickness of rotor bearing pm',
              expression='1')	

##amount of pm and fe in bearing rotor
lastInstance = ParameterGeom(name='H_PERCENT_PM_TO_FE_BNG_ROT : %(h of pm  / total height) of rotor of bearing',
              expression='0.8')

lastInstance = ParameterGeom(name='H_FE_ROT_B : iron height of rotor of bearing',
              expression='H_ROT_B*(1-H_PERCENT_PM_TO_FE_BNG_ROT)')

lastInstance = ParameterGeom(name='H_PM_ROT_B : iron height of rotor of bearing',
              expression='H_ROT_B*H_PERCENT_PM_TO_FE_BNG_ROT/2')			  
			  
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
              expression='1.5')	

lastInstance = ParameterGeom(name='R_DR_ROT_OUT : outer radius of drive rotor',
              expression='(R_OUT_PM_ROT_BNG-D_PM_B_ROT-R_SEP)')

##iron			  
lastInstance = ParameterGeom(name='K_D_DR_FE_ROT : prop constant, radial thickness of drive iron in rotor',
              expression='(1.1/(13/2))')
			  
lastInstance = ParameterGeom(name='D_DR_FE_ROT : radial thickness of drive iron in rotor',
              expression='K_D_DR_FE_ROT*R_DR_ROT_OUT')			  

##pm			  
lastInstance = ParameterGeom(name='K_D_DR_PM : constant for radial thickness of drive pms ',
              expression='1/7.5')	
			  
lastInstance = ParameterGeom(name='D_DR_PM : radial thickness of pms of drive',
              expression='R_DR_ROT_OUT*K_D_DR_PM')	

##airgap			  
lastInstance = ParameterGeom(name='D_AGAP_D : drive airgap',
              expression='.75')
			  
lastInstance = ParameterGeom(name='theta_mag : angular width of drive pms',
              expression='60')				  

##slotted stator of drive

ParameterGeom(name='R_DR_ST_OUT : outer radius of stator',
              expression='R_DR_ROT_OUT-D_DR_FE_ROT-D_DR_PM-D_AGAP_D')
			  
ParameterGeom(name='K_W_SLOT',
              expression='2/7.5')

ParameterGeom(name='W_SLOT',
              expression='K_W_SLOT*R_DR_ROT_OUT')				  
			  
lastInstance = ParameterGeom(name='L_SLOT_OUT : outer flank of slot',
              expression='Sqrt(R_DR_ST_OUT^2-(W_SLOT/2)^2)')				  