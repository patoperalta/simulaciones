% function [ r_max] = speed( r_out,beta,Sf_sigma,sigma_max,rho_m_mag,nu_mag,n_ob,dn_ob )
%%patricio peralta
%modified from C:\Users\jperalta\switchdrive\4_EPFL_Dropbox\05 Calculations\01_matlab_rotor_space\20170808 revE2 various windows and contours
%%22.09.2017
clear
clc
close all

%inputs below
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%steel parameters out of https://perso.uclouvain.be/ernest.matagne/ELEC2311/T2006/NOFP.pdf
%M235-35A , thin and low losses
r_out=linspace(5/1000,50/1000,100000);
beta = 0.2:0.1:0.9;
beta=beta';
Sf_sigma=.8;
sigma_max = 460e6; %mag war 80e6;
rho_m_mag = (7500+7600)*1/2; %7500 is magnet, 7600 is steel
nu_mag=0.24; %not present, assuming the one from magnet
n_ob = 150*1e3;
dn_ob = 20*1e3;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%gives max speed of rotating ring
%%proper parameters come from rotor_optimization script
%%beta = r_in / r_out
%%see notebook 27.07.2017

n=1./(r_out.*(2*pi/60)).*...
    sqrt(Sf_sigma*sigma_max)./...
    sqrt(1/4*rho_m_mag.*...
    (...
    (1-nu_mag).*beta.^2+(3+nu_mag)*ones(size(beta))...
    )...
    );
n_beta_0=sqrt(Sf_sigma*sigma_max)/...
        sqrt((3+nu_mag)/8*rho_m_mag)*...
        1./(2*pi/60.*r_out);
%%plot results
figure('Name','Maximal Achievable Speed vs Radius')
plot(r_out*1000,n_beta_0*1e-3,'LineWidth',2)
hold on
plot(r_out*1000,n*1e-3,'LineWidth',2)
grid on
%%axis and title
ylabel({'n_{max}','Max. angular speed [krpm]'})
xlabel({'Rotor outer radius  [mm]','r_{r.out}'})
title({'Maximum achievable angular speed', 'with different rotor outer and inner radii'})
%%prepare legend
beta_l(2:length(beta)+1,1)=beta(:);
beta_l(1,1)=0;
legendCell = cellstr(strcat('\beta = ',num2str(beta_l)));
%%plot material data
% text(mean(r_out*1000)-5,max(n_beta_0*1e-3)-20,...
%     strcat(...
%     '\sigma_{TS,mag} = ',...
%     num2str( sigma_max/(1e6) ),...
%     ' MPa'...
%     )...
%     )
% text(mean(r_out*1000)-5,max(n_beta_0*1e-3)-50,...
%     strcat(...
%     '\rho_{mag} = ',...
%     num2str( rho_m_mag ),...
%     ' kg m^{-3}'...
%     )...
%     )
% text(mean(r_out*1000)-5,max(n_beta_0*1e-3)-80,...
%     strcat(...
%     '\nu_{mag} = ',...
%     num2str( nu_mag )...
%     )...
%     )
text(mean(r_out*1000)-20,round(0.8*n_ob*1e-3,0)-80,...
    strcat(...
    '\sigma_{TS,iron} = ',...
    num2str( sigma_max/(1e6) ),...
    ' MPa'...
    )...
    )
text(mean(r_out*1000)-20,round(.8*n_ob*1e-3,0)-90,...
    strcat(...
    '\rho_{iron} = ',...
    num2str( rho_m_mag ),...
    ' kg m^{-3}'...
    )...
    )
text(mean(r_out*1000)-20,round(.8*n_ob*1e-3,0)-100,...
    strcat(...
    '\nu_{iron} = ',...
    num2str( nu_mag )...
    )...
    )
%%plot speed limits
% plot(r_out*1000,n_ob*1e-3*ones(size(r_out)),'--','Color','red','LineWidth',1.5)
%%adjust y scale
ylim([0 round(1.7*n_ob*1e-3,0)])
%%find maximum radius for objective speed, considering only beta > 0
ind=find(n_ob-n(size(n,1),:)<1/100);
r_max = r_out(ind(end));
% plot([r_max r_max]*1000,[0 n_ob]*1e-3,':','Color','magenta','LineWidth',1.5)
%%plot maximum radius
% text((r_max)*1000+0,(n_ob)*1e-3+15,...
%     {...
%     '{r^{*}}_{out.rot.} = ',...
%     strcat(num2str( round(r_max*1000,1) ),...
%     ' mm'...
%     )...
%     }...
%     )
%%show legend
legend(legendCell,'Box','off')
% end