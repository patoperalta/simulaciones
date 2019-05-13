#! Flux2D 18.1

print("FICHIER PARAM.PY\n")
##copy parameters from ext rotor rout14 in
## C:\Users\jperalta\Desktop\08_flux_ext_rotor\4_ext_rotor_script_2
##however, change beta definition

## revF is made for the ICEMS paper simulation, so we start from outside to inside building up the rotor...
## for revision F see 18.05.2018
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

## stator

lastInstance = ParameterGeom(name='R_ST_OUT : outside stator radius',
              expression='15')
			  
lastInstance = ParameterGeom(name='D_MOT',
              expression='R_ST_OUT*2')				  
			  
# lastInstance = ParameterGeom(name='K_D_ST : prop stator thickness',
              # expression='1.5/5')	
			  
lastInstance = ParameterGeom(name='D_ST : stator thickness is now directly available',
              expression='3')
			  
lastInstance = ParameterGeom(name='R_ST_IN',
              expression='R_ST_OUT-D_ST')				  

## slot width			  
# ParameterGeom(name='K_W_SLOT : prop factor for teeth length',
              # expression='1.5/5')

ParameterGeom(name='W_SLOT : now directly modifiable',
              expression='5')
			  
lastInstance = ParameterGeom(name='Y : for beginning of slot',
              expression='sqrt(R_ST_IN^2-(W_SLOT/2)^2)')			  

## slot length
# ParameterGeom(name='K_L_SLOT',
              # expression='2/10')	
			  
ParameterGeom(name='L_SLOT',
              expression='2')	

## mech/mag airgap 			  
lastInstance = ParameterGeom(name='D_AGAP',
              expression='2')
			  
##rotor without hole!
ParameterGeom(name='R_ROT_OUT : outer radius of stator',
              expression='R_ST_IN-L_SLOT-D_AGAP')				  

# height definition alpha_h=h_rot/h_st			  
# DO NOT START WITH 1 OTHERWISE YOU LOSE 3 HOURS OF YOUR LIFE SEARCHING FOR YOUR ERROR
# (because planes have to be erased)
# become irrelevant in 2D
# lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              # expression='.5')
			  
# lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              # expression='1.5')  			  

# ## heights				  
# lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              # expression='ValidLR(ALPHA_H,0,1,1,1)')	
		  
# ParameterGeom(name='h_st : height of stator',
              # expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')			  

# lastInstance = ParameterGeom(name='H_ROT',
              # expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')		
			  
##rotor position			  
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
			  
## for new build
lastInstance = ParameterGeom(name='Y2 : length of y to rstout',
              expression='Sqrt(R_ST_OUT**2-(W_SLOT/2)**2)')
			  