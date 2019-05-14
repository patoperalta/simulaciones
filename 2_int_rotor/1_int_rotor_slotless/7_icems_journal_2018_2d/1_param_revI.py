#! Flux2D 18.1
print("FICHIER PARAM.PY\n")
##copy parameters from ext rotor rout14 in
## C:\Users\jperalta\Desktop\08_flux_ext_rotor\4_ext_rotor_script_2
##however, change beta definition

## rev F was made for sonceboz CTI #6 presentation... with fixed rotor size

## rev G was for ECCE paper

## rev H is for ICEMS paper... see notebook 18.05.2018 
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## define rotor and then towards the outside

## rotor with NO HOLE

r_rot_out = 10
	  
ParameterGeom(name='R_ROT_OUT : outer radius of rotor',
              expression=str(r_rot_out))	

lastInstance = ParameterGeom(name='D_MECHGAP : d_cu= d_agap-d_mechgap',
			  expression='2')				  
			  
## airgap			  
lastInstance = ParameterGeom(name='D_AGAP : mechanic + cu',
			  expression='5')		

ParameterGeom(name='D_ST',
			  expression='5+4*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*7/2')				  			  			  			  
			  
# if r_rot_out==10:		  
	# ## D_ST is now a parameter, so there is no proportionality constant			  		  
	# lastInstance = ParameterGeom(name='D_ST : stator thickness',
				  # expression='5')	
# elif r_rot_out==15:
	# ## D_ST is now a parameter, so there is no proportionality constant			  		  
	# lastInstance = ParameterGeom(name='D_ST : stator thickness',
				  # expression='9')					  				  
# elif r_rot_out==20:
	# ## D_ST is now a parameter, so there is no proportionality constant			  		  
	# lastInstance = ParameterGeom(name='D_ST : stator thickness',
				  # expression='12.5')	

lastInstance = ParameterGeom(name='R_ST_IN : stator inner radius',
              expression='R_ROT_OUT+D_AGAP')			  			  
## stator
lastInstance = ParameterGeom(name='R_ST_OUT : stator outer radius',
              expression='R_ST_IN+D_ST')
			  
lastInstance = ParameterGeom(name='D_MOT : stator outer diameter',
              expression='R_ST_OUT*2')				  		  		  
			  
# height parameters become irrelevant for 2D

# lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              # expression='.3')			  
			  
# lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              # expression='1.8')	

# lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              # expression='ValidLR(ALPHA_H,0,1,1,1)')	  
			  
# ParameterGeom(name='h_st : height of stator',
              # expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')			  

# lastInstance = ParameterGeom(name='H_ROT',
              # expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')				  	
			  
##rotor position parameters which are relevant for 2D		  
lastInstance = ParameterGeom(name='DTHETA',
              expression='0')

# lastInstance = ParameterGeom(name='DALPHA',
              # expression='0')

# lastInstance = ParameterGeom(name='DBETA',
              # expression='0')

lastInstance = ParameterGeom(name='DX',
              expression='0')

lastInstance = ParameterGeom(name='DY',
              expression='0')

# lastInstance = ParameterGeom(name='X_H_DIFF : abs val of height dif between st and rot',
              # expression='0')			  
			  
# lastInstance = ParameterGeom(name='DZ',
              # expression='0')	

lastInstance = ParameterGeom(name='DR_0',
              expression='0')

lastInstance = ParameterGeom(name='DTHETA_0',
              expression='0')	