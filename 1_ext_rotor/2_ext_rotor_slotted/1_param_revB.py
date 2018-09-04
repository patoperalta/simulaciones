#! Flux3D 12.0
#PARAMS
###########################################################################################################################################################################################################################################
lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              expression='.3')

# height definition alpha_h=h_rot/h_st			  
# DO NOT START WITH 1 OTHERWISE YOU LOSE 3 HOURS OF YOUR LIFE SEARCHING FOR YOUR ERROR
# (because planes have to be erased)
lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              expression='1.8')

lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')

lastInstance = ParameterGeom(name='R_ROT_OUT : motor outer radius, variable actually',
              expression='15/2')

lastInstance = ParameterGeom(name='K_D_ROT : PROP rotor iron thickness',
              expression='1.1/(13/2)')				  
			  
lastInstance = ParameterGeom(name='D_ROT : rotor iron thickness',
              expression='K_D_ROT*R_ROT_OUT')				  

lastInstance = ParameterGeom(name='d_mot : total diameter of motor',
              expression='2*r_rot_out')	
			  
ParameterGeom(name='h_st : height of stator',
              expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')			  
			  
lastInstance = ParameterGeom(name='R_ROT_IN : rotor iron inner radius',
              expression='R_ROT_OUT-D_ROT')				  
			  
lastInstance = ParameterGeom(name='K_D_MAG : PROP rotor magnet thickness ',
              expression='1/(15/2)')			  
			  
lastInstance = ParameterGeom(name='D_MAG : rotor magnet thickness',
              expression='K_D_MAG*R_ROT_OUT')			  

## change ! now airgap is fixed number  
lastInstance = ParameterGeom(name='D_AGAP : airgap thickness for both cases',
              expression='1.5')					  
			  
ParameterGeom(name='R_ST_OUT : outer radius of stator',
              expression='R_ROT_IN-D_MAG-D_AGAP')
			  
## the center of the stator is still circular
lastInstance = ParameterGeom(name='K_R_ST : PROP inner radius stator',
              expression='1.8/14')				  
			  			  
##slot point
ParameterGeom(name='K_W_SLOT',
              expression='2/7.5/1.1')

ParameterGeom(name='W_SLOT',
              expression='K_W_SLOT*R_ROT_OUT')	

##from slot self
lastInstance = ParameterGeom(name='L_SLOT_OUT : outer flank of slot',
              expression='Sqrt(R_ST_OUT^2-(W_SLOT/2)^2)')			  
			  			  
## start with rotor	displacement
lastInstance = ParameterGeom(name='DTHETA : rotor rotation around z axis',
              expression='0')

lastInstance = ParameterGeom(name='DALPHA : rotor rotation around x axis',
              expression='0')

lastInstance = ParameterGeom(name='DBETA : better use dtheta and dalpha ... ',
              expression='0')

lastInstance = ParameterGeom(name='DX : displacement in x rotor direction',
              expression='0')

lastInstance = ParameterGeom(name='DY : displacemen in y direction, also magnetic direction',
              expression='0')

lastInstance = ParameterGeom(name='X_H_DIFF : abs val of height dif between st and rot',
              expression='0')			  
			  
lastInstance = ParameterGeom(name='DZ',
              expression='0')	

lastInstance = ParameterGeom(name='DR_0 : radial displacement',
              expression='0')

lastInstance = ParameterGeom(name='DTHETA_0 : after radial displacement, turning',
              expression='0')			  
##different rotor radii and height

lastInstance = ParameterGeom(name='H_ROT',
              expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')
 
lastInstance = ParameterGeom(name='THETA_MAG : opening angle from pms in rotor',
              expression='80')			  