#! Flux3D 12.0

#########################################################################################################################################################
##define application
#########################################################################################################################################################			  
lastInstance = ApplicationMagneticDC3D(formulationModel=MagneticDC3DAutomatic(),
                        scalarVariableOrder=ScalarVariableAutomaticOrder(),
                        vectorNodalVariableOrder=VectorNodalVariableAutomaticOrder(),
                        coilCoefficient=CoilCoefficientAutomatic())	