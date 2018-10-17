all the geometry is manually changed !!!
and the material ferrite is also changed manually

MAGNET D20
https://www.magnetmax.de/Neodym-Ringmagnete/Ringmagnet-O-20-0-x-6-0-x-8-0-mm-Neodym-N45-vernickelt-diametral::144.html

WURTH FERRITE
https://www.mouser.ch/ProductDetail/Wurth-Electronics/742701112?qs=sGAEpiMZZMs2JV%252bnT%2fvX8M6liuu7KVKqfnuJCTeD5RI=

lastInstance = Material(name='FERRITE : Wuerth 742701112',
         propertyBH=PropertyBhLinear(mur='800'))


TDK FERRITE		 
B64290L0674X065 EPCOS / TDK | Mouser Schweiz
https://www.mouser.ch/ProductDetail/EPCOS-TDK/B64290L0674X065?qs=sGAEpiMZZMs2JV%252bnT%2fvX8Df1W1GtRs01pTWTGFCoXDY%3d

lastInstance = Material(name='FERRITE_TDK_T65',
         propertyBH=PropertyBhNonlinearJmu(initialMur='5200',
                                           js='.460'))

										   
FERROXCUBE FERRITE 3E27
TX36/23/10-3E27 Ferroxcube | Magnetik - Transformatoren, Induktorkomponenten | DigiKey
https://www.digikey.ch/product-detail/de/ferroxcube/TX36-23-10-3E27/1779-1582-ND/8021296

lastInstance = Material(name='FERRITE_3E27',
         propertyBH=PropertyBhNonlinearJmu(initialMur='6000',
                                           js='.430'))								   

see flux down

ParameterGeom['D_AGAP'].expression='3'

ParameterGeom['R_ST_OUT'].expression='(R_ROT_OUT+D_AGAP+D_ST)*0+36/2'

VariationParameter['R_ST_OUT_PH'].formula='(R_ST_IN_PH+D_ST_PH)*0+36/2'

%ROTOR HEIGHT / DMOT

ParameterGeom['BETA'].expression='8/36'

%STAYS THE SAME, GIVEN ROTOR

ParameterGeom['K_D_ROT'].expression='7/10'

%WE GIVE THE THE SAME HEIGHT

ParameterGeom['ALPHA_H'].expression='1'
		 