#! Flux3D 12.0

print("FICHIER PARAM.PY\n")
##copy parameters from ext rotor rout14 in
## C:\Users\jperalta\Desktop\08_flux_ext_rotor\4_ext_rotor_script_2
##however, change beta definition

##rev G is made for the ECCE 2018 final paper, and therefore starts building the motor from the stator towards the inside
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## stator out
lastInstance = ParameterGeom(name='R_ST_OUT',
              expression='10')
			  
lastInstance = ParameterGeom(name='D_MOT',
              expression='R_ST_OUT*2')						  
			  
## stator in
lastInstance = ParameterGeom(name='K_D_ST : prop stator thickness',
              expression='2.75/10')
			  
lastInstance = ParameterGeom(name='D_ST : stator thickness',
              expression='K_D_ST*R_ST_OUT')	
			  
lastInstance = ParameterGeom(name='R_ST_IN',
              expression='R_ST_OUT-D_ST')		

##airgap			  
lastInstance = ParameterGeom(name='FIX_AGAP : 1 if fixed, 0 is constant',
              expression='1')			  
			  
lastInstance = ParameterGeom(name='DEF_AGAP : if airgap is fixed, it takes this value',
              expression='3')						  
			  
lastInstance = ParameterGeom(name='K_AGAP : if airgap is fixed, it takes this value',
              expression='3/30')
			  
lastInstance = ParameterGeom(name='D_AGAP : airgap thickness for both cases',
              expression='DEF_AGAP*FIX_AGAP+(1-FIX_AGAP)*K_AGAP*R_ST_OUT')				  

##rotor out			  
ParameterGeom(name='R_ROT_OUT : outer radius of stator',
              expression='R_ST_IN-D_AGAP')	
			  
##rotor in			  
lastInstance = ParameterGeom(name='K_D_ROT : proprotor thickness',
              expression='1/10')			  
			  
lastInstance = ParameterGeom(name='D_ROT : rotor thickness',
              expression='K_D_ROT*R_ST_OUT')			  
			  
lastInstance = ParameterGeom(name='R_ROT_IN : stator thickness',
              expression='R_ROT_OUT-D_ROT')				  
			  
# height definition alpha_h=h_rot/h_st			  
# DO NOT START WITH 1 OTHERWISE YOU LOSE 3 HOURS OF YOUR LIFE SEARCHING FOR YOUR ERROR
# (because planes have to be erased)
lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              expression='.3')

lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              expression='1.8')		  

lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')	  	  

ParameterGeom(name='h_st : height of stator',
              expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')			  

lastInstance = ParameterGeom(name='H_ROT',
              expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')		
			  
##rotor position			  
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