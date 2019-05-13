#! Flux2D 18.1
#########################################################################################################################################################
##define application with 1 mm depth, which makes all calculations afterward easier
#########################################################################################################################################################	
		  
lastInstance = ApplicationMagneticDC2D(domain2D=Domain2DPlane(lengthUnit=LengthUnit['MILLIMETER'],
                                               depth='1'),
                        coilCoefficient=CoilCoefficientAutomatic())
