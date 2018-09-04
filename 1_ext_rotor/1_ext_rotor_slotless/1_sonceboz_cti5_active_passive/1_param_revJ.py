#! Flux3D 12.0


print("FICHIER PARAM.PY\n")
##################################################################################################################################################################
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################
## stator
## added mods
# insert definitions for geometry
# if alpha <= 1 --> h_st = 2*r_rot_out*beta_1

## rev I has changes from 18.01.2018

## rev J changed for very small diameters and is changed to have the same measurements as the 
## temp 6 from bimotor

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

lastInstance = ParameterGeom(name='K_D_ROT : PROP rotor thickness',
              expression='1.1/(13/2)')				  
			  
lastInstance = ParameterGeom(name='D_ROT : rotor thickness',
              expression='K_D_ROT*R_ROT_OUT')				  

lastInstance = ParameterGeom(name='d_mot : total diameter of motor',
              expression='2*r_rot_out')		

lastInstance = ParameterGeom(name='K_D_ST : PROP stator thickness',
              expression='(1.0/7.5)/1.3')				  
			  
lastInstance = ParameterGeom(name='D_ST : stator thickness',
              expression='K_D_ST*R_ROT_OUT')				  
			  
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
              expression='2')					  
			  
ParameterGeom(name='R_ST_OUT : outer radius of stator',
              expression='R_ROT_IN-D_MAG-D_AGAP')
			  
			  
ParameterGeom(name='R_ST_IN : inner radius of stator',
              expression='R_ST_OUT-D_ST')			  
			  			  
## start with rotor	
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

##parameters for coil		  
lastInstance = ParameterGeom(name='W_SENS : width of sensor in mm',
              expression='0')

lastInstance = ParameterGeom(name='COIL_PHI_PER : percent of coil with z wire',
              expression='80')

lastInstance = ParameterGeom(name='COIL_ST_PER : percent of straight coil height',
              expression='80')

lastInstance = ParameterGeom(name='COIL_KCU : filling factor coil',
              expression='.4')

# lastInstance = ParameterGeom(name='COIL_TH : coil radial thickness in mm',
              # expression='(1-FIXED_AIRGAP)*1/56*(15*R_ROT_OUT-112)+263/224*FIXED_AIRGAP')			  

# lastInstance = ParameterGeom(name='COIL_phi : angular width of z wire in coil in rad',
              # expression='COIL_ALPHA*COIL_PHI_PER/2*1/100')

# lastInstance = ParameterGeom(name='COIL_PSI : angular width of no coil in rad',
              # expression='(COIL_ALPHA-2*COIL_PHI)*.99')			  

# lastInstance = ParameterGeom(name='COIL_WCOIL',
              # expression='2*pi()/6*(R_ST_IN-COIL_TH)')				  	  			  
			  
# lastInstance = ParameterGeom(name='COIL_A_CU',
              # expression='COIL_TH*COIL_KCU*COIL_WCOIL')						  	  
			  
# lastInstance = ParameterGeom(name='COIL_A : without copper filling factor',
              # expression='COIL_TH*COIL_WCOIL')
			  