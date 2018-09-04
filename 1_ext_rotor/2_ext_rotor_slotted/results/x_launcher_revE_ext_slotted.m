%%patricio peralta
%%03.04.2018
%%launching evaluation functions

%rev J has all the excel -- > matlab inside
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% clean
clc 
clear
close all

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% type of motor and name
mot='2';                            %topology
rev='8';                            %revision, that is, material type
material=3;                              %choose type of material
typ='ext_rotor_slotted_n42_no12';   %name
p=2;                                %pole pairs
vtan = 100; %maximum tangential velocity from rotor
Jrms=10;        %current density for torque and force generation
exp = 1;    %if 1, convert .xls to .mat
dx_startup = .5;    %dx startup
jmax = 400;         %max J bng for startup
fz_vent=.5;         %N of axial force due to ventilator op
dz_max=3;           %%max axial displacement

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% materials
if material==1   %m270
    rho_fe=7.650;
    c_h=0.025654156;
    beta_h=0.87480276;
    c_ed=0.0000894290082649805;
    beta_ed=2.8586117381767;
elseif material==2 %metglas
    rho_fe=7.180;
    c_h=8.77357855312521E-10;
    beta_h=1.57146911005535;
    c_ed=1.79126607423198E-10;
    beta_ed=2.76689096383283;    
else    %no12
    rho_fe=7.650;
    c_h=0.0329856688071909;
    beta_h=1.24844961191923;
    c_ed=9.10402E-06;
    beta_ed=2.56583298480801;    
end
density=[rho_fe,7.500,8.960]/1000; %steel, pm, cu weight, in g / cm^3 --> g / mm^3 for revision 1

%%input for loss calculation
z08_in=[...
    .3/1000,...                  %w_d_cu
    .4,...                      %w_kcu
    15,...                      %harm_order_max
    p,...                       %w_p
    c_h,...             %c_h
    beta_h,...              %beta_h
    c_ed,...   %c_ed
    beta_ed,...         %beta_ed
    rho_fe];                       %rho_fe

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% start extracting data from excel files, with scripts inside !!!
if exp==1
z01_dz_auswertung(mot,rev,typ)

z02_dalpha_auswertung(mot,rev,typ)

z03_dbeta_auswertung(mot,rev,typ)

z04_dx_auswertung(mot,rev,typ)

z05_dy_auswertung(mot,rev,typ)

z06_jt_auswertung(mot,rev,typ,vtan,Jrms)

z07_jf_auswertung(mot,rev,typ,Jrms)

z08_losses(mot,rev,typ,z08_in);
end

%% start plotting and blahblah
%%already ran the previous parts
name={'LOSSES',...
    'DZ',...
    'DALPHA',...
    'DBETA',...
    'DX',...
    'DY',...
    'JT',...
    'JF'};
for i = 0:7
    name{i+1}=strcat('rev',rev,'\',mot,'_',num2str(i),'_',name{i+1},'_rev',num2str(rev),'_out');
end
clear i
%% rate motors
%%torque and efficiency
load(name{7})

%%copy characteristics of motors
xi_torque{2} = out(:,1:4);
xi_torque{1}=cols(:,1:4);

%%copy torque
xi_torque{2} = [xi_torque{2} out(:,9:12)];
xi_torque{1}=[xi_torque{1} "it_hat" "p_cu_tot" "a_cu" "tz" ];

%%maximal velocity as krpm in a column
%omega_mec=v/r=2*pi*fmec=2*pi*n/60 with rrot in mm
%n = v/r * 60/(2pi) 
n_max=vtan./((out(:,4))*1e-3) * 60/(2*pi);  

xi_torque{2}=[xi_torque{2} n_max];
xi_torque{1}=[xi_torque{1} "n_max"];

p_loss=out(:,10);   %save copper losses, will add on top the pcu_ed and p_fe
%%calculate weight of motor, volume is in mm^3
%steel st, steel rot, pm, cu vol
weight=((out(:,5)+out(:,6))*density(1)+out(:,7)*density(2)+out(:,8)*density(3)); %%mm^3 x g / mm^3

%%now start considering losses
load(name{1})

%%losses at n_max
p_loss_nmax=[p_loss ...                         %classic joule losses
            out(:,5)  .*(p*(n_max/60)).^2 ...   %edd_cu
            out(:,6)  .*(p*(n_max/60)).^1 ...   %hyst_fe
            out(:,7)  .*(p*(n_max/60)).^2 ...   %edd_fe
            ];   
%clean workspace
clear p_loss out cols

%calculate power at maximum speed
p_mec_nmax=xi_torque{2}(:,8).*(xi_torque{2}(:,9)/60*2*pi);

%%finish the vector
xi_torque{2}=[xi_torque{2} p_mec_nmax p_loss_nmax];
xi_torque{1}=[xi_torque{1} "p_mec_max" "p_cu" "p_cu_edd" "p_fe_hyst" " p_fe_edd"];
%clean
clear p_mec_nmax p_loss_nmax vtan n_max p

%calculate efficiency at a fraction of maximal velocity
n_percent = 100;
eff=100*...
    xi_torque{2}(:,10).*(n_percent/100) ./... % scale mec calculated power
    (...
    xi_torque{2}(:,10).*(n_percent/100)...       % scaled mec power
    +xi_torque{2}(:,11)...                                              %copper losses
    +xi_torque{2}(:,12).*(n_percent/100).^2 ... %eddy currents in copper
    +xi_torque{2}(:,13).*(n_percent/100).^1 ... %hysteresis in iron
    +xi_torque{2}(:,14).*(n_percent/100).^2);   %eddy currents in iron
eff=eff.*(eff>=0).*(eff<100);
xi_torque{2}=[xi_torque{2} eff];
xi_torque{1}=[xi_torque{1} strcat("eff at ",num2str(n_percent),"% from n_max")];
clear eff n_percent
%%add weight column
xi_torque{2}=[xi_torque{2} weight];
xi_torque{1}=[xi_torque{1} strcat("weight of fe+pm+cu")];
clear weight
%% calculate stability indicator
for i = 2 : 6
    load(name{i})
    if i==2
        xi_stability{2}=out;
        xi_stability{1}=cols;
    else
        xi_stability{2}=[xi_stability{2} out(:,end)];
        xi_stability{1}=[xi_stability{1} cols(:,end)];
    end
end
%%clean
clear cols out i
%calculate stability indicator
xi_stb_opt= xi_stability{2}(:,5) .* ... %kz
            xi_stability{2}(:,6) .* ... %kalpha
            xi_stability{2}(:,7) ./ ... %kbeta
            (...
            xi_stability{2}(:,8) .* ... %kx
            xi_stability{2}(:,9) ...    %ky
            );
xi_stb_opt=-xi_stb_opt;             %change its size, so that positive larger values become better
%calculate if configurations are feasible ie if kz kalpha and kbeta are negative        
feasible =(xi_stability{2}(:,5)<0).*(xi_stability{2}(:,6)<0).*(xi_stability{2}(:,7)<0).*(abs(fz_vent./xi_stability{2}(:,5))<dz_max);
feasible(feasible==0)=nan;
%add to stability vector
xi_stability{2}=[xi_stability{2} feasible xi_stb_opt];
xi_stability{1}=[xi_stability{1} "feasibility" "stability merit"];
%%clean
clear xi_stb_opt

%% force
load(name{8})
j_bng_startup=dx_startup*max(xi_stability{2}(:,8),xi_stability{2}(:,9))./out(:,end)*Jrms;
out=[out j_bng_startup]; %assuming dx_startup = .5 mm
cols=[cols "startup J_F"];
feasible = feasible .* (j_bng_startup < jmax); %erase unfeasible startups over jmax
feasible(feasible==0)=nan;
xi_stability{2}(:,10)=feasible;
xi_force{2}=out;
xi_force{1}=cols;

%% plots
fig1=figure(1);
fig2=figure(2);
fig3=figure(3);
% %%amounf of shades and colors
N = 4; 
N_off=3;
C{1} = linspecer(N,'blue'); 
C{2} = linspecer(N,'red');
C{3} = linspecer(N,'green');
C{4} = linspecer(N,'purple');
%%markers for torque and for power
mrkr=['x','o','d','*'];
load(name{7});
for i = 1 : 5       %length(beta)           %%changes marker size
    for j = 1 : 4   %length(dairgap)        %%different color
        for k = 1 : 1   %length(rout)       %%before, it was size, but it is now constant
            for l = 1 : 4 %length(alpha)    %%changes face color
                %% define criteria to filter points
                %        alpha   beta    dagap      r out is not analyzed
                crit = [1.2+l*.2  i/10  .5*j+1.0 ];
                %% filters
                aux_torque = filter_equal(xi_torque{2},crit);
                aux_force  = filter_equal(xi_force{2},crit);                
                v_pm= filter_equal(out,crit);
                v_pm=v_pm(:,7);
                aux_stability = filter_equal(xi_stability{2},crit);   
                fs=aux_stability(:,end-1);
                %% style
                mrkr_size=(7+i^2.0)/1.6*1+0*7;      %I varies with i, that is, with beta
                line_width=(1.2*i^1.1)/1.6*0+2;     %constant 
                line_style='none';                  %no line between the points
                clr=C{j}(N_off,:);                  %J color of edge, varies only with airgap (blue --> red --> green --> orange)
                fc_clr=C{j}(l,:);                   %J and l color of face, shades of the previous color                
                mrk=mrkr(2);                        %marker type
                %% torque vs mech power
                figure(1)
                plot(...
                    1e6*(aux_torque(:,8)).*fs,...
                    (aux_torque(:,10)).*fs,...
                    'Marker',mrk,'MarkerSize',mrkr_size,'LineWidth',line_width,'LineStyle',line_style,'color',clr,'MarkerFaceColor',fc_clr);
                hold on
                grid on
                %% stability vs mech power
                figure(2)
                semilogx(...
                    aux_stability(:,end).*fs,...
                    (aux_torque(:,10)).*fs,...
                    'Marker',mrk,'MarkerSize',mrkr_size,'LineWidth',line_width,'LineStyle',line_style,'color',clr,'MarkerFaceColor',fc_clr);
                hold on
                grid on     
                %% axial displacement vs maximal power
                figure(3)
                plot(...
                    fz_vent/aux_stability(:,5).*fs,...
                    aux_torque(:,10).*fs,...
                    'Marker',mrk,'MarkerSize',mrkr_size,'LineWidth',line_width,'LineStyle',line_style,'color',clr,'MarkerFaceColor',fc_clr);
                hold on
                grid on    
                %% startup current density vs maximal power
                figure(4)
                plot(...
                    aux_force(:,end).*fs,...
                    aux_torque(:,10).*fs,...
                    'Marker',mrk,'MarkerSize',mrkr_size,'LineWidth',line_width,'LineStyle',line_style,'color',clr,'MarkerFaceColor',fc_clr);
                hold on
                grid on               
            end
        end
    end
end
% cols
xi_pm_utilization{1}=["stability_utilization","power_utilization"];
xi_pm_utilization{2}=[(aux_stability(:,end)./out(:,7)).*feasible*(180/pi)^2/1000,...
                    out(:,13)./out(:,7).*feasible];
clear i j k l aux N C aux_jt aux_stability aux_torque crit mrkr_size line_width line_style clr cols out v_pm mrkr 
%%format and axes
typ=strrep(typ,'_',' ');

figure(1)
xlabel(strcat({'Torque at J='},{num2str(Jrms)},{' A_{RMS}/mm^2 [{\mu}Nm]'}))
ylabel('Mechanical Power [W]')
title(typ)

figure(2)
ylabel('Mechanical Output Power [W]')
xlabel('Stability Indicator \tau [Nm^3/rad^2]')
xlim([0 inf])
title(typ)

figure(3)
ylabel('Mechanical Power [W]')
xlabel(strcat({'Axial Displacement @ '},num2str(fz_vent),{' N force [mm]'}))
title(typ)
% xlim([-4 0])

figure(4)
ylabel('Mechanical Power [W]')
xlabel(strcat({'Current Density @ '},num2str(dx_startup),{' mm BNG. startup [A_{RMS}/mm^2]'}))
title(typ)


%% arrange figures
autoArrangeFigures(3,2,2);
%% export plots
savefig(fig1,strcat('rev',rev,'\',mot,'_rev',rev,'_fig1'));
savefig(fig2,strcat('rev',rev,'\',mot,'_rev',rev,'_fig2'));
savefig(fig3,strcat('rev',rev,'\',mot,'_rev',rev,'_fig3'));

%% export matrixes
save(strcat('rev',rev,'\',mot,'_rev',rev,'_xi'),'xi_force','xi_stability','xi_torque','typ','xi_pm_utilization');

clear z00_in typ rev mot name feasible
clear typ rev mot name feasible z00_in

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%FUNCTIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z01_dz_auswertung(mot,rev,typ)
%% name and directory
sim='1_DZ';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% define output format
cols=["alpha","beta","dgap","rmot","kz"];

%% define numerical output
out=raw(:,1:4); %alpha,beta,dgap,rmot
out(:,5)=-raw(:,11)./raw(:,5); %f_st_z / dx 

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z02_dalpha_auswertung(mot,rev,typ)
%% name and directory
sim='2_DALPHA';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% define output format
cols=["alpha","beta","dgap","rmot","kalpha"];

%% define numerical output
out=raw(:,1:4); %alpha,beta,dgap,rmot
out(:,5)=-1/5.*...
    sqrt(raw(:,6).^2+raw(:,8).^2)...
    .*sign(...
    max(...
    raw(:,6),raw(:,8)...
    )...
    ); % - 1 / dalpha  * sqrt(tx_st^2+ty_st^2) * sign(max(tx,ty))

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z03_dbeta_auswertung(mot,rev,typ)
%% name and directory
sim='3_DBETA';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% define output format
cols=["alpha","beta","dgap","rmot","kbeta"];

%% define numerical output
out=raw(:,1:4); %alpha,beta,dgap,rmot
out(:,5)=-1/5.*...
    sqrt(raw(:,6).^2+raw(:,8).^2)...
    .*sign(...
    max(...
    raw(:,6),raw(:,8)...
    )...
    ); % - 1 / dalpha  * sqrt(tx_st^2+ty_st^2) * sign(max(tx,ty))

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z04_dx_auswertung(mot,rev,typ)
%% name and directory
sim='4_DX';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% define output format
cols=["alpha","beta","dgap","rmot","krx"];

%% define numerical output
out=raw(:,1:4); %alpha,beta,dgap,rmot
out(:,5)=sqrt(raw(:,9).^2+raw(:,10).^2)./raw(:,5); %sqrt(fx_rot^2+fy_rot^2)/dx

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z05_dy_auswertung(mot,rev,typ)
%% name and directory
sim='5_DY';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% define output format
cols=["alpha","beta","dgap","rmot","kry"];

%% define numerical output
out=raw(:,1:4); %alpha,beta,dgap,rmot
out(:,5)=sqrt(raw(:,10).^2+raw(:,11).^2)./raw(:,5); %sqrt(fx_rot^2+fy_rot^2)/dx

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z06_jt_auswertung(mot,rev,typ,vtan,J)
%% name and directory
sim='6_JT';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% read headers
fid = fopen(filename);
headers=textscan(fid, '%s', 15, 'delimiter',';');
fclose(fid);
clear ans fid
%% aconditionate headers so that they are a string matrix
headers=headers{1};
headers=headers';

%% define numerical output
%extend imported vector with mech_power
raw = [raw  vtan./(raw(:,4)*1e-3).*raw(:,end-1)];  
headers=[headers "P_MEC"]; 

%erase column with JT_RMS and R_ROT_OUT
raw(:,5:6)=[]; 
headers(:,5:6)=[]; 

% %erase column with TZ_ST
raw(:,end-1)=[]; 
headers(:,end-1)=[]; 

%define output
out=raw;
cols=headers;

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [name]=z07_jf_auswertung(mot,rev,typ,J)
%% name and directory
sim='7_JF';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%% read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

%% prepare headers
cols=["alpha","beta","dgap","rmot","if_hat","p_cu","fr_mod"];

%% define numerical output
out=raw(:,1:4); %alpha,beta,dgap,rmot
out(:,5)=raw(:,6); %if
out(:,6)=raw(:,8); %pcu
out(:,7)=sqrt(...
            raw(:,9).^2....
            +raw(:,10).^2....
            ); %sqrt(fx_rot^2+fy_rot^2)

%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

function [name]=export_as_xls(rev,mot,sim,out,cols,typ)
%% define name of .xls file and export
name=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'_out');
save(name,'out','cols','typ')
end

function [name] = z08_losses(mot,rev,nom,ins)
%from z00 revB
%%rename imput
w_d_cu=ins(1);
w_kcu=ins(2);
harm_order_max=ins(3);
w_p=ins(4);
c_h=ins(5);
beta_h=ins(6);
c_ed=ins(7);
beta_ed=ins(8);
rho_fe=ins(9);

%% brms file
%%import flux output
sim='0_brms_a_wholecoil_mid';
filename=strcat('rev',rev,'\',mot,'_',sim,'_rev',rev,'.csv');

%%read headers of brms file
fid = fopen(filename);
headers=textscan(fid, '%s', 5, 'delimiter',';');
fclose(fid);
clear ans fid
%%aconditionate them so that they are a string matrix
headers=headers{1};
headers=headers';
%%read numerical data
raw=xlsread(filename); %raw results, xlsread magically discards first row

% headers=[headers 'B_RMS_A'];
%%obtain copper area for each motor, using results from z_06
load(strcat('rev',rev,'\',mot,'_6_JT_rev',rev,'_out'))
a_cu = out(:,11); %copper area in mm^2
p_joule=out(:,10);
fmec_max=(out(:,13)./out(:,12))*1/(2*pi); % Pmec_max / T_JT4 = omega_max = 2 pi f_max
raw=[raw a_cu];     %% (:,6)
headers=[headers 'A_CU'];

%%calculate height of stator and therefore length where losses occur
    %2*rrotout *  beta     /    alpha_h
h_st=2*raw(:,4).*raw(:,2)./raw(:,1);
raw=[raw h_st]; %% (:,7)
headers=[headers 'H_ST'];

%% input parameters for losses
w_rho_cu=1.68e-8; %%ohm m
w_N=6;        %%number of coils
% w_d_cu=.3/1000; %%diameter of winding in m fn
% w_kcu=.4;     %%when you make turns, you make them with the coil and not
% copper area fn
w_w=floor(a_cu*1e-6/(pi*w_d_cu.^2/4)*1/w_kcu); %number of turns of each coil
raw=[raw w_w]; %% (:,8)
headers=[headers 'W'];

%% calculate pcu_ed for each motor
%%define directory
dir = strcat('rev',rev,'\',mot,'_b_fields_out_rev',rev);
%%define maximum harmonic to be considered
% harm_order_max = 15; fn
%%define pole pair number
% w_p=2;
%%create zero vector to put distortion in
% xi=zeros(size(out,1),1);
% %%counter
% n=1;
% 
% %%calculate xi, that is, base distortion
% %%make a for, so that all files (all motors) are read
% for l = 1 : 3 %rstout
%     for k = 1 : 3 % d_agap
%         for j = 1 : 2 % beta
%             for i = 1 : 6 %alpha
%                 %%name of file to be loaded
%                 filename=strcat(...
%                     'b_airgap_alpha',num2str(2*i+8),...
%                     '_beta_0',num2str(j),...
%                     '_dgap_',num2str(10*k+10),...
%                     '_rout_',num2str(50*l+50));
%                 %%execute calculation of xi
% %                 xi(n)=xi_b_airgap_hmax_revD(strcat(dir,'\',filename),w_p,harm_order_max,'B20:H1043');
%                 %%increase counter
% %                 n=n+1;
%             end
%         end
%     end
% end
xi=ones(size(out,1),1); %assume slotted motors have sinusoidal field passing through its coils
clear n filename dir h_max i j k l harm_order_max
raw=[raw xi]; %% (:,9)
headers=[headers 'xi'];

lbar=xlsread(strcat('rev',rev,'\',mot,'_0_DIMENSIONS_rev',rev,'.csv'));%,'E2:E109');
lbar=lbar(:,5);
%mow we actually read kwslot
w_slot=xlsread(strcat('rev',rev,'\',mot,'_0_DIMENSIONS_rev',rev,'.csv'));%,'H2:H2');
w_slot=w_slot(1,8)*raw(:,4); %now we have wslot
%thesis daniel pg 114
%still have to multiply by f_el^2 = (p*f_mec)^2
pcu_fel2=(1/32)*...
    1/w_rho_cu*...
    pi^3*...
    w_N*...
    w_d_cu^4*...
    w_w.*... %W, number of parallel conductors in each coil
    lbar/1000.*... %H_ST in m
    (raw(:,5).*xi).^2; %%(brms*xi)^2
    
raw=[raw pcu_fel2]; %% (:,10)
headers=[headers 'p_ed_cu_f2'];
clear xi w_w 

%% calculate p_fe for each motor 
%C:\Users\jperalta\switchdrive\4_EPFL_Dropbox\05 Calculations\08_steinmetzt_parameters
%%M270-50A Least Squares HY+ED
fe_props=[c_h beta_h c_ed beta_ed rho_fe];
clear c_h beta_h c_ed beta_ed rho_fe

%%calculate integral of b(h)^beta_i 
%%load excels
dir = strcat('rev',rev,'\',mot,'_b_fields_out_rev',rev);
%counter
n=1;
%define variable where everything is put
b_mod_beta_hy_ring=zeros(size(out,1),1);
b_mod_beta_hy_slot=zeros(size(out,1),1);
b_mod_beta_ed_ring=zeros(size(out,1),1);
b_mod_beta_ed_slot=zeros(size(out,1),1);
for l = 1 : 1 %rstout
    for k = 1 : 4 % d_agap
        for j = 1 : 5 % beta
            for i = 1 : 4 %alpha
                %first do slot
                %%define name
                filename=strcat(...
                    '_alpha',num2str(2*i+12),...
                    '_beta_0',num2str(j),...
                    '_dgap_',num2str(50*k+100),...
                    '_rout_',num2str(25*l+50));    
                %%import
                b_slot=xlsread(strcat(dir,'\slot',filename),'B17:F1040');
                % integrate along the slot line, then we only have to
                % multiply by width and height
                b_mod_beta_hy_slot(n)=trapz(b_slot(:,1),b_slot(:,5).^fe_props(2));
                b_mod_beta_ed_slot(n)=trapz(b_slot(:,1),b_slot(:,5).^fe_props(4));
                %%import what happens in central circle
                b_rsc=xlsread(strcat(dir,'\center_rsc',filename),'B17:F1040');
                %we are now inside a circle of the middle
                %radial integral, int(b(r) * r dr), then multiply my height
                %and 2pi                        r           r      * b ^c_e
                b_mod_beta_hy_ring(n)=trapz(b_rsc(:,1),b_rsc(:,1).*b_rsc(:,5).^fe_props(2));
                b_mod_beta_ed_ring(n)=trapz(b_rsc(:,1),b_rsc(:,1).*b_rsc(:,5).^fe_props(4));
                n=n+1;
            end
        end
    end
end
clear h b n i j k l b_h dir filename 
%%calculate, see notebook from 25.01.2018
% p / f^i = c^i * rho_fe *  h_st   ( n_slots * l(b)*w
ph_f=fe_props(1)*fe_props(5)*h_st*1e-3.*(w_N*b_mod_beta_hy_slot.*w_slot*1e-3...
    +b_mod_beta_hy_ring*2*pi); %h_st and w_slot are in mm, but integral is already in m
ped_f2=fe_props(3)*fe_props(5)*h_st*1e-3.*(w_N*b_mod_beta_ed_slot.*w_slot*1e-3...
    +b_mod_beta_ed_ring*2*pi); %h_st and w_slot are in mm, but integral is already in m
% ped_f2=fe_props(3)*fe_props(5)*vfe_st./h_st.*int_bh_bed(:,2)*1e-6; %volume is in mm^3 and heigh in mm
% clear int_bh_bed vfe_st

%%write in out vector
raw=[raw ph_f ped_f2]; %% (:,11) (:,12)
headers=[headers 'ph_f' 'ped_f2'];
% clear ph_f ped_f2

%% calculate losses at maximum mechanical speed
p_speed_n_max=p_joule+pcu_fel2.*(w_p*fmec_max).^2+ph_f.*(w_p*fmec_max)+ped_f2.*(w_p*fmec_max).^2;
raw=[raw p_speed_n_max]; %% (:,13)
headers=[headers 'p_speed_n_max'];
clear p_speed_n_max fmec_max

%% export
%%now, important columns will be eliminated !!! so beware
%keeps it
old_out=out; 
%%new out to conserve name export purposes
out = raw;
cols = headers;
typ = nom;
%erase useless stuff
% p_loss_nmax         brms_a, acu, hst, w, xi
out(:,end)=[]; out(:,5:9)=[];
cols(:,end)=[]; cols(:,5:9)=[];

sim='0_LOSSES';
%% define name of .xls file and export
export_as_xls(rev,mot,sim,out,cols,typ)
end

%% functions
function [ aux ] = filter_equal( data,criteria )
aux=data;    %%so that various criteria can be searched into another
for i = 1 : length(criteria) %%search all criteria
    if criteria(i)==-1      %%put -1 as criteria 
        %%do nothing
    else
        k = abs(aux(:,i)-criteria(i))<.05; %%see where criteria is met with certain numerical tolerance
        aux=aux(k,:);   %%save vector
    end
end
end