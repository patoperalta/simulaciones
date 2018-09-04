%PATO
%exterior rotor construction
%initialize by clearing 
clear all;
clc;
cur_folder=pwd;
rev='9';
mat='_n42_no12';
date='20180419_';
file_name=strcat(date,'slotted_ext_rotor_rev',rev,mat);
%where project will be saved
server_path = strcat(cur_folder,'/sims');
%where commands are
python_path = cur_folder;
%where the project is and how it will be named
% proj_name=strcat(server_path,'/asdf.FLU');
proj_name=strcat(server_path,'/',file_name,'.FLU');


%change slash direction for flux compatibility
server_path = regexprep(server_path, '\','/'); 
python_path = regexprep(python_path, '\','/');
proj_name = regexprep(proj_name, '\','/');


%% Init Flux java path, built in from flux example file
installFlux=getenv('INSTALLFLUX');
if strcmp(installFlux,'') , installFlux='../../' ; end;
installJar=[installFlux,'/Bin/jar/'];
javaaddpath({[installJar,'fluxmp.jar'],[installJar,'cedserver.jar'],[installJar,'coreboot.jar'],[installJar,'corebus.jar'],[installJar,'jutils.jar'],[installJar,'rsicore.jar'],[installJar,'CoreCommon.jar'],[installJar,'CedUtils.jar'],[installJar,'CssUtils.jar'],[installJar,'CssService.jar']})
import rsi.fluxmp.FMP.*

% Server type, here i only do 3D simulations
% FLUX2D_32     ='FLUX2D_12.0_32';
% FLUX2D_64     ='FLUX2D_12.0_64';
% FLUX3D_32     ='FLUX3D_12.0_32';
FLUX3D_64     ='FLUX3D_12.0_64';
% FLUX_SKEWED_32='FLUX_SKEWED_12.0_32';
% FLUX_SKEWED_64='FLUX_SKEWED_12.0_64';
% INCA3D_32     ='INCA3D_3.1_32';
% INCA3D_64     ='INCA3D_3.1_64';

% Server arguments
NUMERICAL_MEMORY_LABEL='MEMSIZN3=';
CHARACTER_MEMORY_LABEL='MEMSIZC3=';
GUI_MEMORY_LABEL      ='JVM_MEMORY=';
LANGUAGE_LABEL        ='CAO_DEFLAN=';
CONSOLE_LABEL         ='CONSOLE_SERVER=';

% Debug Mode
RELEASEMODE=0;
DEBUGMODE  =1;

% Init Flux API
FMP_init(RELEASEMODE);

% Create local Flux server
args={strcat(NUMERICAL_MEMORY_LABEL,'600000000'),strcat(LANGUAGE_LABEL,'2')};
serverUid = FMP_startLocaleServer(FLUX3D_64, '../', args);

%%
disp('batch mode start')
%solve options
options = optimset('disp','on','MaxIter',5000,'MaxFunEvals',5000,'TolFun',1e-7,'TolX',0.01);
disp('main calculation starts')

%% executing python files
try
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/0_main.py")')); 
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/1_param_revB.py")')); %%%for rev 1 of mats
    disp('parameters definition OK')
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/2_app_def.py")'));
    disp('app definition OK')
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/3_mesh_info.py")'));
    disp('mesh info OK')
    %%for old geometry, which was completely vertically extruded
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4a_geom_coord_sys_revA.py")'));
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4b_geom_rotor_revA.py")'));
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4c_geom_stator_revA.py")'));
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4d_geom_build_revA.py")'));
    %%for circular geometry rotor
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4a_geom_coord_sys_revB.py")'));
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4b_geom_stator_revB.py")'));
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4c_geom_rotor_revB.py")'));
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/4d_geom_build_revB.py")'));
    disp('geom OK')
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/5_mat_def.py")'));
    disp('material def ok')
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/6_elec_circuit_concentric_revA.py")'));
%     disp('concentric windings ok')    
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/7_assign_circular.py")'));
    disp('assign ok')
    rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/8_sensors.py")'));
    disp('sensors ok') 
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/9_make_scenarios_passive_revB.py")'));
%     disp('make passive scenario ok')
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('executeBatchSpy("',python_path,'/10_make_scenarios_active_revB.py")'));
%     disp('make active scenario ok')    
    
%     disp('meshing...')
%     tic
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('meshDomain()'));
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('generateSecondOrderElements()'));
%     disp('mesh ok')
%     toc
%     rsi.fluxmp.FMP.FMP_executeJythonCommand (serverUid,strcat('buildMagneticCircuitCut()'));
%     disp('magnetic circuit cut generated ok')
%     tic
    
catch Herror
    Herror.message 
    disp('scheisse!')
end

%% ending messages
rsi.fluxmp.FMP.FMP_executeJythonCommand(serverUid, strcat('saveProjectAs("',proj_name,'")'))
disp('project saved')
rsi.fluxmp.FMP.FMP_executeJythonCommand(serverUid, 'closeProject()');
FMP_stopServer(serverUid)
disp('server closed ok')