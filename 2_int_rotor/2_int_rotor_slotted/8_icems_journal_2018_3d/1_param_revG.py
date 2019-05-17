#! Flux3D 12.0

print("FICHIER PARAM.PY\n")
##copy parameters from ext rotor rout14 in
## C:\Users\jperalta\Desktop\08_flux_ext_rotor\4_ext_rotor_script_2
##however, change beta definition

## revF is made for the ICEMS paper simulation, so we start from outside to inside building up the rotor...
## for revision F see 18.05.2018
#########################################################################################################################################################
## geometric parameters
#########################################################################################################################################################

r_rot_out=10
tuning=4
##rotor without hole!
ParameterGeom(name='R_ROT_OUT : outer radius of stator',
              expression=str(r_rot_out))

## mech/mag airgap 			  
lastInstance = ParameterGeom(name='D_AGAP',
			  expression='2')	

##RETUNE FOLLOWING PARAMETERS FOR THE COILS			  
if tuning==1:
##tuning out 2d sims
	ParameterGeom(name='L_SLOT',
				  expression='7+ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*1.25')				  
				  
	ParameterGeom(name='W_SLOT',
				  expression='6+3*ValidLR(R_ROT_OUT,11,21,1,1)+ValidLR(R_ROT_OUT,19,21,1,1)*4')				  			  
				  
	ParameterGeom(name='D_ST',
				  expression='6+4*ValidLR(R_ROT_OUT,11,21,1,1)+4*ValidLR(R_ROT_OUT,19,21,1,1)')				  			  			  
elif tuning==2:	
	## help of 3d sims with alpha = 2
	ParameterGeom(name='L_SLOT',
				  expression='9.25+3/2*ValidLR(R_ROT_OUT,11,21,1,1)+2.25*ValidLR(R_ROT_OUT,19,21,1,1)')				  
				  
	ParameterGeom(name='W_SLOT',
				  expression='10+4*ValidLR(R_ROT_OUT,11,21,1,1)+6*ValidLR(R_ROT_OUT,19,21,1,1)')				  			  
				  
	ParameterGeom(name='D_ST',
				  expression='10+5*ValidLR(R_ROT_OUT,11,21,1,1)+7*ValidLR(R_ROT_OUT,19,21,1,1)')			  			  			  			  
elif tuning==3:
	## help of 3d sims with alpha = 1.5
	ParameterGeom(name='L_SLOT',
				  expression='7.5+2*ValidLR(R_ROT_OUT,11,21,1,1)+1*ValidLR(R_ROT_OUT,19,21,1,1)')				  
				  
	ParameterGeom(name='W_SLOT',
				  expression='7+5*ValidLR(R_ROT_OUT,11,21,1,1)+4*ValidLR(R_ROT_OUT,19,21,1,1)')				  			  
				  
	ParameterGeom(name='D_ST',
				  expression='8+5*ValidLR(R_ROT_OUT,11,21,1,1)+5*ValidLR(R_ROT_OUT,19,21,1,1)')	
elif tuning==4:
	## free to change, and commented
	ParameterGeom(name='L_SLOT : r=(10,15,20)->l=(7.5,9.5,10.5)',
				  expression='7.5')
				  
	ParameterGeom(name='W_SLOT : r=(10,15,20)->l=(7,12,16)',
				  expression='7')
				  
	ParameterGeom(name='D_ST : r=(10,15,20)->l=(8,13,18)',
				  expression='8')				  
		  
## stator
lastInstance = ParameterGeom(name='R_ST_IN',
              expression='R_ROT_OUT+D_AGAP+L_SLOT')				  
			  			  
lastInstance = ParameterGeom(name='R_ST_OUT : outside stator radius',
              expression='R_ST_IN+D_ST')
			  
lastInstance = ParameterGeom(name='D_MOT',
              expression='R_ST_OUT*2')				  	  
			  
lastInstance = ParameterGeom(name='Y : for beginning of slot',
              expression='sqrt(R_ST_IN^2-(W_SLOT/2)^2)')

## for new build
lastInstance = ParameterGeom(name='Y2 : length of y to rstout',
              expression='Sqrt(R_ST_OUT**2-(W_SLOT/2)**2)')			  

# height definition alpha_h=h_rot/h_st			  
# DO NOT START WITH 1 OTHERWISE YOU LOSE 3 HOURS OF YOUR LIFE SEARCHING FOR YOUR ERROR
# (because planes have to be erased)
# become irrelevant in 2D
lastInstance = ParameterGeom(name='beta : times total diameter gives away stator height if alpha_h <= 1',
              expression='.5')
			  
lastInstance = ParameterGeom(name='alpha_h : h_rot/h_st',
              expression='1.5')  			  

## heights				  
lastInstance = ParameterGeom(name='alpha_case : case of alpha, equals to 1 if he\'s between 0 and 1',
              expression='ValidLR(ALPHA_H,0,1,1,1)')	
		  
ParameterGeom(name='h_st : height of stator',
              expression='D_MOT*(ALPHA_CASE*beta+(1-ALPHA_CASE)*beta/alpha_h)')			  

lastInstance = ParameterGeom(name='H_ROT',
              expression='D_MOT*(ALPHA_CASE*ALPHA_H*beta+(1-ALPHA_CASE)*beta)')		
			  
## displacements booleans
lastInstance = ParameterGeom(name='DALPHA_MULT',
              expression='0')

lastInstance = ParameterGeom(name='DBETA_MULT',
              expression='0')

lastInstance = ParameterGeom(name='DX_MULT',
              expression='0')

lastInstance = ParameterGeom(name='DY_MULT',
              expression='0')	  
			  
lastInstance = ParameterGeom(name='DZ_MULT',
              expression='0')	
			  
##rotor position for relative displacements...
lastInstance = ParameterGeom(name='DTHETA',
              expression='0')

lastInstance = ParameterGeom(name='DALPHA',
              expression='DALPHA_MULT*R_ROT_OUT/4')

lastInstance = ParameterGeom(name='DBETA',
              expression='DBETA_MULT*R_ROT_OUT/4')

lastInstance = ParameterGeom(name='DX',
              expression='DX_MULT*R_ROT_OUT/12')

lastInstance = ParameterGeom(name='DY',
              expression='DY_MULT*R_ROT_OUT/12')	  
			  
lastInstance = ParameterGeom(name='DZ',
              expression='DZ_MULT*R_ROT_OUT/5')	

lastInstance = ParameterGeom(name='DR_0',
              expression='0')

lastInstance = ParameterGeom(name='DTHETA_0',
              expression='0')				  

## for coil extrusion, see 14.05.2019, which is better than the previous approximation
lastInstance = ParameterGeom(name='TH_COIL : see 14.05.2019',
              expression='(Pi()/6-Atan2(W_SLOT/2,Y-L_SLOT))*sqrt((Y-L_SLOT)^2+(W_SLOT/2)^2)')
##or the definition from coils_concentric from TH_COIL
# lastInstance = VariationParameterFormula(name='TH_COIL : coil thickness to the sides, see 2.2.2018',
                          # formula='((R_ST_IN_PH-W_SLOT_PH/2)*pi()/3-W_SLOT_PH)/2')
# lastInstance = ParameterGeom(name='H_COIL : see 14.05.2019',
              # expression='((R_ST_IN-W_SLOT/2)*pi()/3-W_SLOT)/2')						  
			  