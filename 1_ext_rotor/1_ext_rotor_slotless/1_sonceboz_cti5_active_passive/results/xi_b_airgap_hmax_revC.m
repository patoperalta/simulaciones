function [ xi ] = xi_b_airgap_hmax_revC( dir_filename,p,hmax,pos )
% dir_filename='test';
%%patricio peralta
%%07.11.2017
%%evaluation of airgap fields for the calculation of 
%%eddy current copper losses as daniel suggested
%%obtain fields as bx and by
%%output is the vector br, btan, brms,and xi

%%test with revA in the 0ld matlab folder

%%coming from :
%C:\Users\jperalta\switchdrive\4_EPFL_Dropbox\05 Calculations\02_matlab_motor_losses\revB_motor_fields

%%HMAX CONSIDERS THE CALCULATION OF XI UNTIL THE HMAX-TH HARMONIC
%%OTHERWISE, THIS FACTOR IS EXAGERATED
%%FOUND THAT OUT BECAUSE XI SHOULD ALWAYS BE AROUND 1 FOR THE 1 PP MOTOR

%% clear and these things
% clc
% close all
% clear

%% generate theta vector to project to r and theta
% dir_filename='0a_int_rotor_slotless_constant_airgap_bfields_out\airgap_int_rotor_slotless_alpha_11_beta_06_rout_100';
% p=1;
% hmax=15;
data=xlsread(dir_filename,1,pos); %assumming 1024 points

% fetch necesary data
% dairgap=data(:,1);
b_x=data(:,5);
b_y=data(:,6);

%free workspace
clear data 

%% rotate coordinate system to r and theta
%angle
theta=linspace(0,2*pi,size(b_x,1));
theta=theta';

%rotate from data
b_r=b_x.*cos(theta)+b_y.*sin(theta);
b_tan=-b_x.*sin(theta)+b_y.*cos(theta);

% %test
% b_r=sqrt(2)*cos(theta)*0+sqrt(2)*2*cos(2*theta);
% b_tan=b_r*.5;

%plot
% f1=figure;
% f1.Position=[76 908 560 420];
% plot(theta,b_r,'-')
% hold on
% grid on
% plot(theta,b_tan,'-')

%modulus and rms
b_mod=(sqrt(b_r.^2+b_tan.^2));
b_rms=rms(b_mod);

%% fft of components

%fft centered around 0
fs=length(theta)/p;
NFFT=length(theta)/p;
fft_br=fftshift(fft(b_r,NFFT));
fft_btan=fftshift(fft(b_tan,NFFT));
fVals=fs*(-NFFT/2:NFFT/2-1)/NFFT;	

%find center frequency
f0=find(fVals==0);

%the positive harmonics are then accounted for, 
%but then, their amplitude %is double, and then its in peak
%so it is divided by sqrt(2) to have rms. 
fVals=fVals(f0:end);
fft_br=2*fft_br(f0:end)/NFFT/sqrt(2);
fft_btan=2*fft_btan(f0:end)/NFFT/sqrt(2);

%a plot, if you want
% f2=figure;
% f2.Position=[651 908 560 420];
% stem(fVals,abs(fft_br))
% xlim([0 hmax])
% hold on
% grid on
% stem(fVals,abs(fft_btan))

%calculate distortion
xi=1/b_rms...
    *sqrt(...
    fVals(1:hmax).^2*...
    ( abs(fft_br(1:hmax)).^2 + abs(fft_btan(1:hmax)).^2 )...
    );
end