#! Flux3D 12.0

#M270-50A import @ 60 Hz
# Material(name='Cogent_M270_50A_60Hz : AC Curve 60 Hz - Magsoft 11-27-13', propertyJE=PropertyJeLinear(rho='5.5E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=30.14897145455453, b=0.5583195383544677), BHPoint(h=57.47147683524457, b=0.8014669589602983), BHPoint(h=114.94295367048915, b=1.0554113872521187), BHPoint(h=173.82766354266596, b=1.1828586189728878), BHPoint(h=247.43355088288698, b=1.2726841983189632), BHPoint(h=339.44091005816324, b=1.3385008839945494), BHPoint(h=454.4501090272586, b=1.388316882513333), BHPoint(h=598.2116077386278, b=1.4271905946570458), BHPoint(h=777.9134811278393, b=1.4585163635993679), BHPoint(h=1002.5408228643537, b=1.4847032356509042), BHPoint(h=1283.3250000349967, b=1.5075606100537984), BHPoint(h=1634.3052214983004, b=1.5285329183638185), BHPoint(h=2073.03049832743, b=1.5488529348897677), BHPoint(h=2621.437094363842, b=1.5696502300451567), BHPoint(h=3306.945339409357, b=1.5920352462391996), BHPoint(h=4163.830645716251, b=1.617171360718385), BHPoint(h=5234.937278599868, b=1.646343099980897), BHPoint(h=6573.820569704389, b=1.6810265315423274), BHPoint(h=8247.42468358504, b=1.7229668832636367), BHPoint(h=10339.429825935855, b=1.7742681824379336), BHPoint(h=12954.436253874374, b=1.8340388022204785), BHPoint(h=16223.19428879752, b=1.888024421320848), BHPoint(h=20309.141832451456, b=1.934588181077391), BHPoint(h=25416.576262018876, b=1.9742566116964841), BHPoint(h=31800.86929897815, b=2.00770641431493), BHPoint(h=39781.23559517724, b=2.03568294053627), BHPoint(h=49756.6934654261, b=2.058939298562508), BHPoint(h=62226.015803237184, b=2.078195517643845), BHPoint(h=68448.61738356091, b=2.0860150694082296)], equivalentHarmonicCurve=EquivalentBhUnmodified()), volumicMass='7600')

##M270-50A import @ 50 Hz
Material(name='Cogent_M270_50A_50Hz : AC Curve 50 Hz - Magsoft 11-27-13', propertyJE=PropertyJeLinear(rho='5.5E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=25.335410773000902, b=0.5094095664557834), BHPoint(h=48.29562678603297, b=0.7454092508250769), BHPoint(h=96.59125357206594, b=1.0017970717433387), BHPoint(h=146.07447773808332, b=1.1344364688373194), BHPoint(h=207.92850794560505, b=1.229527244853858), BHPoint(h=285.2460457050072, b=1.300012211798584), BHPoint(h=381.8929679042599, b=1.3537654064900504), BHPoint(h=502.7016206533258, b=1.3958885445691518), BHPoint(h=653.7124365896582, b=1.4298715604430412), BHPoint(h=842.4759565100736, b=1.4582263472240313), BHPoint(h=1078.430356410593, b=1.482856944062607), BHPoint(h=1373.3733562862421, b=1.5052900520340753), BHPoint(h=1742.0521061308036, b=1.5268284928566516), BHPoint(h=2202.9005434365054, b=1.548661354467694), BHPoint(h=2778.9610900686325, b=1.5719502020275844), BHPoint(h=3499.036773358792, b=1.5979033017505093), BHPoint(h=4399.131377471491, b=1.6278458927617978), BHPoint(h=5524.249632612364, b=1.663292525794019), BHPoint(h=6930.647451538455, b=1.7059732977090576), BHPoint(h=8688.644725196069, b=1.753407597419617), BHPoint(h=10886.141317268088, b=1.8024404970229542), BHPoint(h=13633.01205735811, b=1.8516679534963991), BHPoint(h=17066.60048247064, b=1.899527941220615), BHPoint(h=21358.5860138613, b=1.9444152373205), BHPoint(h=26723.567928099623, b=1.9847898884010333), BHPoint(h=33429.79532089753, b=2.0192546990803937), BHPoint(h=41812.57956189491, b=2.046585611555856), BHPoint(h=52291.05986314165, b=2.0657108838057883), BHPoint(h=57520.16584945582, b=2.072281972186367)], equivalentHarmonicCurve=EquivalentBhUnmodified()), volumicMass='7600')


##MUMETAL import
Material(name='Imphy_Mumetal : Annealed at 1170C (4h)', propertyJE=PropertyJeLinear(rho='6.0E-7'), propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=0.07730337052716346, b=0.04602790951232145), BHPoint(h=0.19142247126788856, b=0.10461819800940673), BHPoint(h=0.3828449425357771, b=0.18390674271156043), BHPoint(h=0.6707130314576181, b=0.27256669471182327), BHPoint(h=1.1169085692864718, b=0.36641484021222653), BHPoint(h=1.808511652921195, b=0.4568239710389393), BHPoint(h=2.8804964325550166, b=0.5363431733989547), BHPoint(h=4.54207284098744, b=0.6008591956808994), BHPoint(h=7.117516274057696, b=0.6498302372724394), BHPoint(h=11.109453595316594, b=0.6851048726067008), BHPoint(h=17.296956443267888, b=0.7094828510107992), BHPoint(h=26.887585857592395, b=0.7257160890365061), BHPoint(h=41.75306144979538, b=0.736039703330057), BHPoint(h=64.79454861771002, b=0.74205041483429), BHPoint(h=100.50885372797771, b=0.7447386380251969), BHPoint(h=155.86602664889264, b=0.7450817557495342), BHPoint(h=241.6696446763108, b=0.7452726177975624), BHPoint(h=374.66525261880895, b=0.7455648825875318), BHPoint(h=580.8084449296812, b=0.7460097433508142), BHPoint(h=900.3303930115333, b=0.7466811655891662), BHPoint(h=1395.5894125384038, b=0.7476831419417013), BHPoint(h=2163.2408928050536, b=0.7491578111557223), BHPoint(h=3353.1006872183607, b=0.7512963061089424), BHPoint(h=5197.383368558987, b=0.7543600097338129), BHPoint(h=8056.021524636959, b=0.7587286674261435), BHPoint(h=12486.910666557815, b=0.7649963126697421), BHPoint(h=19354.788836535146, b=0.7741298427653783), BHPoint(h=30000.0, b=0.7876991118430775), BHPoint(h=33000.0, b=0.7914690230273853)], equivalentHarmonicCurve=EquivalentBhUnmodified()))

## ndfeb50 import
#! Preflu2D 10.3
#! Preflu3D 10.3
#! FluxSkewed 10.3

Material(name='BMT_50H : BMT_NdFeB', propertyBH=PropertyBhMagnetOneDirection(br='1.41', mur='1.0447'), volumicMass='7600')	

## ndfeb42uh import
#! Preflu2D 10.3
#! Preflu3D 10.3
#! FluxSkewed 10.3

Material(name='BMT_42UH : BMT_NdFeB', propertyBH=PropertyBhMagnetOneDirection(br='1.31', mur='1.0561'), volumicMass='7600')


##METGLAS http://magweb.us/free-bh-curves/ + extrapolation in DATASHEET folder
lastInstance = Material(name='METGLAS',
         propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    b=0.0),
                                                            BHPoint(h=0.9491626252,
                                                                    b=0.023724686),
                                                            BHPoint(h=1.2126102414,
                                                                    b=0.032310921),
                                                            BHPoint(h=1.4633573684,
                                                                    b=0.042258681),
                                                            BHPoint(h=1.8202602134,
                                                                    b=0.059140911),
                                                            BHPoint(h=2.1645023577,
                                                                    b=0.075660091),
                                                            BHPoint(h=2.3387043684,
                                                                    b=0.084645811),
                                                            BHPoint(h=3.7196995418,
                                                                    b=0.157366666),
                                                            BHPoint(h=5.925144266,
                                                                    b=0.269697236),
                                                            BHPoint(h=8.2028369485,
                                                                    b=0.363638296),
                                                            BHPoint(h=10.3699733049,
                                                                    b=0.441967576),
                                                            BHPoint(h=12.7836153342,
                                                                    b=0.513561616),
                                                            BHPoint(h=15.7496570244,
                                                                    b=0.591127466),
                                                            BHPoint(h=21.3417874608,
                                                                    b=0.708591176),
                                                            BHPoint(h=26.2710176141,
                                                                    b=0.794886336),
                                                            BHPoint(h=31.4127501882,
                                                                    b=0.872267896),
                                                            BHPoint(h=37.2343806926,
                                                                    b=0.947088936),
                                                            BHPoint(h=43.5233589603,
                                                                    b=1.016735676),
                                                            BHPoint(h=59.5434504615,
                                                                    b=1.149),
                                                            BHPoint(h=74.8410942105,
                                                                    b=1.232395221),
                                                            BHPoint(h=91.2860871032,
                                                                    b=1.284148101),
                                                            BHPoint(h=111.5555108274,
                                                                    b=1.319848586),
                                                            BHPoint(h=133.3971373406,
                                                                    b=1.341587081),
                                                            BHPoint(h=155.7487012275,
                                                                    b=1.354974331),
                                                            BHPoint(h=183.9644056522,
                                                                    b=1.365540516),
                                                            BHPoint(h=231.9820348415,
                                                                    b=1.376390326),
                                                            BHPoint(h=279.1497657554,
                                                                    b=1.383211281),
                                                            BHPoint(h=331.8417717978,
                                                                    b=1.388736281),
                                                            BHPoint(h=371.3606808372,
                                                                    b=1.391972381),
                                                            BHPoint(h=447.8489552861,
                                                                    b=1.396941051),
                                                            BHPoint(h=613.9985136522,
                                                                    b=1.404),
                                                            BHPoint(h=792.0462181581,
                                                                    b=1.410014626),
                                                            BHPoint(h=800,
                                                                    b=1.410024621017041)]))

#NO12 https://cogent-power.com/downloads + extrapolation in DATASHEET folder
# lastInstance = Material(name='NO12',
         # propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    # b=0.0),
                                                            # BHPoint(h=25.0,
                                                                    # b=0.1),
                                                            # BHPoint(h=32.0,
                                                                    # b=0.2),
                                                            # BHPoint(h=39.0,
                                                                    # b=0.3),
                                                            # BHPoint(h=45.0,
                                                                    # b=0.4),
                                                            # BHPoint(h=51.0,
                                                                    # b=0.5),
                                                            # BHPoint(h=57.0,
                                                                    # b=0.6),
                                                            # BHPoint(h=65.0,
                                                                    # b=0.7),
                                                            # BHPoint(h=75.0,
                                                                    # b=0.8),
                                                            # BHPoint(h=89.0,
                                                                    # b=0.9),
                                                            # BHPoint(h=105.0,
                                                                    # b=1.0),
                                                            # BHPoint(h=124.0,
                                                                    # b=1.1),
                                                            # BHPoint(h=160.0,
                                                                    # b=1.2),
                                                            # BHPoint(h=248.0,
                                                                    # b=1.3),
                                                            # BHPoint(h=470.0,
                                                                    # b=1.4),
                                                            # BHPoint(h=1290.0,
                                                                    # b=1.5),
                                                            # BHPoint(h=3050.0,
                                                                    # b=1.6),
                                                            # BHPoint(h=5350.0,
                                                                    # b=1.7),
                                                            # BHPoint(h=9420.0,
                                                                    # b=1.8),
                                                            # BHPoint(h=10000.0,
                                                                    # b=1.800728849495633)]))
																	
# NO12 https://cogent-power.com/downloads ONLY DATASHEET INFORMATION, BUT IT STOPS TOO EARLY
# lastInstance = Material(name='NO12',
         # propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    # b=0.0),
                                                            # BHPoint(h=25.0,
                                                                    # b=0.1),
                                                            # BHPoint(h=32.0,
                                                                    # b=0.2),
                                                            # BHPoint(h=39.0,
                                                                    # b=0.3),
                                                            # BHPoint(h=45.0,
                                                                    # b=0.4),
                                                            # BHPoint(h=51.0,
                                                                    # b=0.5),
                                                            # BHPoint(h=57.0,
                                                                    # b=0.6),
                                                            # BHPoint(h=65.0,
                                                                    # b=0.7),
                                                            # BHPoint(h=75.0,
                                                                    # b=0.8),
                                                            # BHPoint(h=89.0,
                                                                    # b=0.9),
                                                            # BHPoint(h=105.0,
                                                                    # b=1.0),
                                                            # BHPoint(h=124.0,
                                                                    # b=1.1),
                                                            # BHPoint(h=160.0,
                                                                    # b=1.2),
                                                            # BHPoint(h=248.0,
                                                                    # b=1.3),
                                                            # BHPoint(h=470.0,
                                                                    # b=1.4),
                                                            # BHPoint(h=1290.0,
                                                                    # b=1.5),
                                                            # BHPoint(h=3050.0,
                                                                    # b=1.6),
                                                            # BHPoint(h=5350.0,
                                                                    # b=1.7),
                                                            # BHPoint(h=9420.0,
                                                                    # b=1.8)]))												

# NO12 https://cogent-power.com/downloads + LOG EXTRAPOLATION WITH EXCEL (SEE DATASHEETS) EARLY																	
lastInstance = Material(name='NO12',
         propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0,
                                                                    b=0.0),
                                                            BHPoint(h=25.0,
                                                                    b=0.1),
                                                            BHPoint(h=32.0,
                                                                    b=0.2),
                                                            BHPoint(h=39.0,
                                                                    b=0.3),
                                                            BHPoint(h=45.0,
                                                                    b=0.4),
                                                            BHPoint(h=51.0,
                                                                    b=0.5),
                                                            BHPoint(h=57.0,
                                                                    b=0.6),
                                                            BHPoint(h=65.0,
                                                                    b=0.7),
                                                            BHPoint(h=75.0,
                                                                    b=0.8),
                                                            BHPoint(h=89.0,
                                                                    b=0.9),
                                                            BHPoint(h=105.0,
                                                                    b=1.0),
                                                            BHPoint(h=124.0,
                                                                    b=1.1),
                                                            BHPoint(h=160.0,
                                                                    b=1.2),
                                                            BHPoint(h=248.0,
                                                                    b=1.3),
                                                            BHPoint(h=470.0,
                                                                    b=1.4),
                                                            BHPoint(h=1290.0,
                                                                    b=1.5),
                                                            BHPoint(h=3050.0,
                                                                    b=1.6),
                                                            BHPoint(h=5350.0,
                                                                    b=1.7),
                                                            BHPoint(h=9420.0,
                                                                    b=1.8),
                                                            BHPoint(h=20000.0,
                                                                    b=1.876631403201),																	
                                                            BHPoint(h=30000.0,
                                                                    b=1.930274437003),		
                                                            BHPoint(h=40000.0,
                                                                    b=1.968334775189),	
                                                            BHPoint(h=50000.0,
                                                                    b=1.997856667027),	
                                                            BHPoint(h=60000.0,
                                                                    b=2.021977808991),	
                                                            BHPoint(h=70000.0,
                                                                    b=2.042371943932),		
                                                            BHPoint(h=80000.0,
                                                                    b=2.060038147177),		
                                                            BHPoint(h=90000.0,
                                                                    b=2.075620842794),																		
                                                            BHPoint(h=100000.0,
                                                                    b=2.089560039016)]))