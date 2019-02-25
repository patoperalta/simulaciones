%% patricio peralta
%%read hall sensor data for displacements and angles
%%09.05.2018

%%rev B: 16.05.2018, read sensors from rev10

%%rev C: 17.05.2018 shift indexes from first read, load is also compacter
%%see mathematica file calculations_revC in calculations light 14 hall

%%rev D: 21.05.2018 no idea because C does not work, so I redo it

%%rev G: 11.10.2018 analyzing hall sensors from below and above, new
%%structure also

%%revH : 15.10.2018 another adaptation of rev G

%%revI: 15.10.2018 adapt for displacement and rotation

%%revJ: 15.10.2018 works well , now make graphs nicer and do functions
%%sensors

%%revK: 16.10.2018 corrected some bugs with last script... actually, turned
%%around b_diff (its signs)
%%
clc
clear all
close all

fntsize=12;

% set(groot,'DefaultAxesFontSize',fntsize)
% set(groot, 'defaultAxesTickLabelInterpreter','latex'); 
% set(groot, 'defaultLegendInterpreter','latex')
% set(groot, 'defaultTextInterpreter','latex')


%% motor color
scenario='11_DISP_ANGLE';
scenario0='08_DISP0_ANGLE';
folder='fields';
d0=5e-3;    %airgap length 
d0=d0/3;    %scaling for double axial hall sensors    
hs_pos=1;   %there are 24 axial positions we choose the one with highest amplitude
displacements=6;
angle=36;
sensors=6;
b_comp=3;
%% import all values
% [b_top_xy,b_bottom_xy]=import_flux(displacements,angle,sensors,folder,scenario,scenario0); 
% save '02_11_DISP';
% load '02_11_DISP'
%% coordinate system and sums and differences
% [b_top_cyl,b_bottom_cyl,b_sum_cyl,b_diff_cyl]= xy_2_cyl(b_top_xy,b_bottom_xy,hs_pos);
% save '03_11_DISP'
load '03_11_DISP'

%% processing of channels
[X1_diff,X2_diff,X5_diff,X6_diff,theta,alpha,pos_rt,pos_st]=hs_2_x_pos_angle(b_diff_cyl,b_comp,d0); 
% save '04_11_DISP'
load '04_11_DISP'

%% plot of displacement sensibility (dx, dy, dr, etc)
% %%for a continuos displacement with no turning angle, see where the
% %%sensibility is
% close all
% figure;
% j=1; %only one angle
% k=1; %for the first sensor
% stator_border=(10+5-(10+1+0.5));        %%[mm] distance between begin of line and stator
% coil_width= 4;                          %%[mm] coil thickness
% for i = 1 : 5   %all displacements
%     %hall sensor j 
%     if j>3 %otherwise we do not find an opposite
%         j=3;
%     end
%     subplot(2,1,1)
%     h1=plot((0:.5:(length(b_top_xy{k,j,i}(:,3))-1)*.5) -stator_border, ...
%         b_top_xy{k,j,i}(:,3)*1000, ...
%         '-x','Color','red');
%     hold on
%     grid on
%     %hall sensor opposing j
%     h2=plot((0:.5:(length(b_top_xy{k,j,i}(:,3))-1)*.5) -stator_border, ...
%         b_top_xy{k+3,j,i}(:,3)*1000, ...
%         '-x','Color','blue');    
%     %difference from hs
%     b_diff(:,i)=[b_top_xy{k,j,i}(:,3)-b_top_xy{k+3,j,i}(:,3)];    
%     h3=plot((0:.5:(length(b_top_xy{k,j,i}(:,3))-1)*.5) -stator_border, ...
%         1000*(b_top_xy{k,j,i}(:,3)-b_top_xy{k+3,j,i}(:,3)), ...
%         '-x','Color','green');
%     if i~=5
%         clear h1 h2 h3
%     end
% end
% dx=200;             %%[um] simulation movement  
% dbdx=mean(diff(b_diff'))/dx;   %%[delta B / delta x] in [T/um] sensitivity
% dbdx=1e3*dbdx;                 %% now in [mT/um]
% subplot(2,1,2)
% plot((0:.5:(length(b_top_xy{k,j,i}(:,3))-1)*.5) -stator_border, ...
%     dbdx, ...
%     '-x','Color','magenta')  
% grid on 
% hold on
% clear dx b_diff
% %style
% aux=gcf;
% aux.Children(1).XTick=-coil_width:2:8;
% aux.Children(2).XTick=aux.Children(1).XTick;
% aux.Children(2).YTick=-500:250:500;
% % aux.Children(2).YTick=aux.Children(1).YTick;
% 
% subplot(2,1,1)
% plot(0*stator_border*ones(size(aux.Children(2).YLim)), ...
%     aux.Children(2).YLim,'color','k','LineStyle','--' );
% plot(-coil_width*ones(size(aux.Children(2).YLim)), ...
%     aux.Children(2).YLim,'color','k','LineStyle','--' );
% ylabel('Axial Field [mT]')
% legend([h1 h2 h3],{['H' num2str(k) ' top'],['H' num2str(k+3) ' top'],'\DeltaH top'},'Box','off')
% subplot(2,1,2)
% y=aux.Children(1).YLim;
% plot(0*stator_border*ones(size(aux.Children(1).YLim)), ...
%     y,'color','k','LineStyle','--' );
% plot(-coil_width*ones(size(aux.Children(1).YLim)), ...
%     y,'color','k','LineStyle','--' );
% text(   aux.Children(1).XLim(2),...
%         y(2),...
%         '\Delta x_{max} = 500 um', ...
%         'HorizontalAlignment','right', 'VerticalAlignment','top' ...
%     );
% ylabel('Measurement Sensitivity [mT/um]')
% xlabel('Distance from Stator Border Towards Outside [mm]')
% aux.Children(1).YLim=y;
% clear aux y
%% 
close all

%% plot lower and upper channel
% figure;
% colors=linspecer(6);
% i=1;                %first displacement
% coord=3;            %1 for radial, 2 for tangential, 3 for axial
% x=0:10:350;         %abcisse
% %actually, concatenating elements from cell
% for j = 1 : angle      %all displacements
%     for k = 1 : sensors   %for all sensors
%         top(j,k)=b_top_cyl{k,j,i}(:,coord);
%         top_0(j,k)=b_top_cyl{k,j,7}(:,coord);
%         bottom(j,k)=b_bottom_cyl{k,j,i}(:,coord);
%         bottom_0(j,k)=b_bottom_cyl{k,j,7}(:,coord);
%     end
% end
% clear coord j k
% for k= 1 :6 %% print all sensor signals, which were prevoisouly concatenated
%     subplot(2,1,1)
%     h(k)=plot(x,1e3*top_0(:,k),'-x','LineWidth',1,'Color',colors(k,:));
%     str{k}=['H' num2str(k)];
%     hold on
%     grid on
%     subplot(2,1,2)
%     plot(x,1e3*bottom_0(:,k),'--x','LineWidth',1,'Color',colors(k,:))
%     hold on
%     grid on     
% end
% legend(h,str,'Box','off','Location','Best','Orientation','horizontal','Autoupdate','off')
%%
close all
%% plot one displacement with rotating rotor
% figure;
% colors=linspecer(6);
% i=1;                %first displacement
% coord=3;            %1 for radial, 2 for tangential, 3 for axial
% x=0:10:350;         %abcisse
% %actually, concatenating elements from cell
% for j = 1 : angle      %all displacements
%     for k = 1 : sensors   %for all sensors
%         top(j,k)=b_diff_cyl{k,j,i}(:,coord);
%         top_0(j,k)=b_diff_cyl{k,j,7}(:,coord);
%         bottom(j,k)=b_diff_cyl{k,j,i}(:,coord);
%         bottom_0(j,k)=b_diff_cyl{k,j,7}(:,coord);
%     end
% end
% clear coord j k
% for k= 1 :6 %% print all sensor signals, which were prevoisouly concatenated
%     subplot(2,1,1)
%     h(k)=plot(x,1e3*top_0(:,k),'-x','LineWidth',1,'Color',colors(k,:));
%     str{k}=['H' num2str(k)];
%     hold on
%     grid on
%     subplot(2,1,2)
%     plot(x,1e3*top(:,k),'--x','LineWidth',1,'Color',colors(k,:))
%     hold on
%     grid on     
% end
% legend(h,str,'Box','off','Location','Best','Orientation','horizontal','Autoupdate','off')
% [m_max,i_max]=max(top(:,1)-top_0(:,1));
% [m_min,i_min]=min(top(:,4)-top_0(:,4));
% subplot(2,1,1)
% ylabel(['\Delta r=0 um' newline 'B-Field [mT]'])
% plot(x(i_max)*[1 1],1e3*[top(i_max,1) top_0(i_max,1)],'o','MarkerSize',10,'Color',colors(1,:),'LineWidth',2)
% text(x(i_max),...
%     max(1e3*[top(i_max,1) top_0(i_max,1)]), ...
%     ['{\Delta}B=' num2str(round(1e3*m_max,0)) ' mT'],...
%     'VerticalAlignment','bottom','HorizontalAlignment','right')
% text(x(i_min),...
%     max(1e3*[top(i_min,4) top_0(i_min,4)]), ...
%     ['{\Delta}B=' num2str(round(1e3*m_min,0)) ' mT'],...
%     'VerticalAlignment','bottom','HorizontalAlignment','right')
% plot(x(i_min)*[1 1],1e3*[top(i_min,4) top_0(i_min,4)],'o','MarkerSize',10,'Color',colors(4,:),'LineWidth',2)
% subplot(2,1,2)
% % plot(x(i_max),1e3*m_max,'x')
% % plot(x(i_min),1e3*m_min,'x')
% clear i j k colors x
% clear top top_0 bottom bottom_0
% ylabel(['\Delta r=500 um' newline 'B-Field [mT]'])
xlabel('Rotor Angle [°]')
%%
close all
%% plot results
figure;  
colors=linspecer(7);
for i = 1 : 7
    for j = 1: 1
%         subplot(2,1,1)
%         plot(0:10:350,X1_diff(:,i),'Color',colors(i,:));
%         hold on
%         grid on
%         subplot(2,1,2)
%         plot(0:10:350,X2_diff(:,i),'Color',colors(i,:));
%         hold on
%         grid on        
        subplot(2,2,1)
        plot(X1_diff(:,i),X2_diff(:,i),'-x','LineWidth',2,'Color',colors(i,:));
        hold on
        grid on   
        pbaspect([1 1 1])    

        subplot(2,2,2)
        plot(0:10:350,rad2deg(alpha{j}),'-x','LineWidth',2,'Color',colors(i,:));
        hold on
        grid on    

        subplot(2,2,3:4)
        plot(1e3*pos_st{i}(1,:),1e3*pos_st{i}(2,:),'-x','Color',colors(i,:));
        hold on
        grid on
        pbaspect([1 1 1])
    end
end
clear i j k

subplot(2,2,1)
xlabel('X$_1$')
ylabel('X$_2$')
% ylabel(['Calculated Angle [deg]'],'FontSize',fntsize)

subplot(2,2,2)
xlabel('Real Angle [deg]','FontSize',fntsize)
ylabel(['Calculated Angle [deg]'],'FontSize',fntsize)
xlim([0 360])
xticks(0:120:360)
yticks(-180:90:180)

subplot(2,2,3:4)
xlabel(['POS$_{X_{ST}}$ [mm]'],'FontSize',fntsize)
ylabel(['POS$_{Y_{ST}}$ [mm]'],'FontSize',fntsize)
xticks(-.5:.25:.5)
yticks(-.5:.25:.5)
%% function to read table
function [b_top_xy,b_bottom_xy]=import_flux(displacements,angle,sensors,folder,scenario,scenario0)
if ~isempty(scenario)
    c    = 0;
    H    = waitbar(0, 'Please wait...');
    n= displacements*sensors*angle;
    for i = 0 : displacements-1           %check all displacements...
        for j = 0 : angle-1      %check all angles
            for k = 1 : sensors   %check all sensors
                filename_1=[...
                            scenario '_HS_AX_' ...
                            ]; %now comes either 'bottom' or 'top' as string
                filename_2=[...
                            '_' num2str(k) '_ANG_DTHETA_' num2str(j*10) '_ANG_DTHETA_0_' num2str(i*60)...
                            ];                 
                name_bottom=[filename_1 'BOTTOM' filename_2];
                name_top=[filename_1 'TOP' filename_2];   
                % sensor, angle, displacement
                b_top_xy{k,j+1,i+1}=importfile([folder '\' name_top],1,19,42);
                b_bottom_xy{k,j+1,i+1}=importfile([folder '\' name_bottom],1,19,42);

                if ~ishghandle(H)
                    error('User closed waitbar.');
                end
                c = c + 1;
                waitbar(c / n, H, sprintf('%d of %d', c, n));
            end
        end
    end
    close(H)
end
%% add no displacement
if ~isempty(scenario0)
    c    = 0;
    H    = waitbar(0, 'Please wait...');
    n= angle*sensors;
    scenario='08_DISP0_ANGLE';
    for i = 0 : 0           %check all displacements...
        for j = 0 : angle-1      %check all angles
            for k = 1 : sensors   %check all sensors            
                filename_1=[...
                            scenario0 '_HS_AX_' ...
                            ]; %now comes either 'bottom' or 'top' as string
                filename_2=[...
                            '_' num2str(k) '_ANG_DTHETA_' num2str(j*10) '_ANG_DTHETA_0_' num2str(i*60)...
                            ];                 
                name_bottom=[filename_1 'BOTTOM' filename_2];
                name_top=[filename_1 'TOP' filename_2];   
                % sensor, angle, displacement
                b_top_xy{k,j+1,displacement+1}=importfile([folder '\' name_top],1,19,42);
                b_bottom_xy{k,j+1,displacement+1}=importfile([folder '\' name_bottom],1,19,42);

                if ~ishghandle(H)
                    error('User closed waitbar.');
                end
                c = c + 1;
                waitbar(c / n, H, sprintf('%d of %d', c, n));
            end
        end
    end
    close(H)
end
end
%%
function tableout = importfile(workbookFile,sheetName,startRow,endRow)
%IMPORTFILE Import data from a spreadsheet
%   DATA = IMPORTFILE(FILE) reads data from the first worksheet in the
%   Microsoft Excel spreadsheet file named FILE and returns the data as a
%   table.
%
%   DATA = IMPORTFILE(FILE,SHEET) reads from the specified worksheet.
%
%   DATA = IMPORTFILE(FILE,SHEET,STARTROW,ENDROW) reads from the specified
%   worksheet for the specified row interval(s). Specify STARTROW and
%   ENDROW as a pair of scalars or vectors of matching size for
%   dis-contiguous row intervals. To read to the end of the file specify an
%   ENDROW of inf.%
% Example:
%   DXHSAXBOTTOM1DX200um = importfile('01_DX_HS_AX_BOTTOM_1_DX_200um.xls','01_DX_HS_AX_BOTTOM_1_DX_200UM',17,40);
%
%   See also XLSREAD.

% Auto-generated by MATLAB on 2018/10/11 15:41:33

%% Input handling

% If no sheet is specified, read first sheet
if nargin == 1 || isempty(sheetName)
    sheetName = 1;
end

% If row start and end points are not specified, define defaults
if nargin <= 3
    startRow = 17;
    endRow = 40;
end

%% Import the data
data = xlsread(workbookFile, sheetName, sprintf('F%d:H%d',startRow(1),endRow(1)));
for block=2:length(startRow)
    tmpDataBlock = xlsread(workbookFile, sheetName, sprintf('F%d:H%d',startRow(block),endRow(block)));
    data = [data;tmpDataBlock]; %#ok<AGROW>
end

%% Create table
tableout = table;

%% Allocate imported array to column variable names
tableout.Magneticfluxdensityxcomponent = data(:,1);
tableout.Magneticfluxdensityycomponent = data(:,2);
tableout.Magneticfluxdensityzcomponent = data(:,3);

tableout=table2array(tableout);
end
%%
function [b_top_cyl,b_bottom_cyl,b_sum_cyl,b_diff_cyl]= xy_2_cyl(b_top_xy,b_bottom_xy,hs_pos)
% rotate to cylindrical coordinates, only for hs_pos !
b_top_cyl=      cell(size(b_top_xy));
b_bottom_cyl=   b_top_cyl;
b_sum_cyl=      b_top_cyl;
b_diff_cyl=     b_top_cyl;
for i = 1 : size(b_top_xy,3)           %check all displacements...
    for j = 1 : size(b_top_xy,2)%check all angles
        for k = 1 : size(b_top_xy,1)   %check all sensors
            aux=cell2mat(b_top_xy(k,j,i));
            b_top_cyl{k,j,i}=[  aux(hs_pos,1)   *cos(deg2rad((k-1)*60))+aux(hs_pos,2)   *sin(deg2rad((k-1)*60)), ...
                                aux(hs_pos,1)  *-sin(deg2rad((k-1)*60))+aux(hs_pos,2)   *cos(deg2rad((k-1)*60)) ,...
                                aux(hs_pos,3) ];

            aux=cell2mat(b_bottom_xy(k,j,i));
            b_bottom_cyl{k,j,i}=[   aux(hs_pos,1)   *cos(deg2rad((k-1)*60))+aux(hs_pos,2)   *sin(deg2rad((k-1)*60)), ...
                                    aux(hs_pos,1)  *-sin(deg2rad((k-1)*60))+aux(hs_pos,2)   *cos(deg2rad((k-1)*60)) ,...
                                    aux(hs_pos,3) ];                     
            b_sum_cyl{k,j,i}=   b_top_cyl{k,j,i}+b_bottom_cyl{k,j,i};
            b_diff_cyl{k,j,i}=  b_top_cyl{k,j,i}-b_bottom_cyl{k,j,i};
        end
    end
end
% clear i j k aux h1 h2 h3 folder scenario
end

function [X1_diff,X2_diff,X5_diff,X6_diff,theta,alpha,pos_rt,pos_st]=hs_2_x_pos_angle(b_diff_cyl,b_comp,d0)
    for i = 1 : size(b_diff_cyl,3)       %for all displacements
        for j = 1 : size(b_diff_cyl,2)	%for all angles
            %we actually loose the dimension of all sensors, because we add
            %through them
            X1_diff(j,i)=    b_diff_cyl{1,j,i}(:,b_comp)-b_diff_cyl{4,j,i}(:,b_comp)...
                            +1/2*	(...
                                b_diff_cyl{2,j,i}(:,b_comp)+b_diff_cyl{6,j,i}(:,b_comp)-b_diff_cyl{3,j,i}(:,b_comp)-b_diff_cyl{5,j,i}(:,b_comp)...
                                    );
            X2_diff(j,i)=    sqrt(3)/2*  ( ...
                                b_diff_cyl{2,j,i}(:,b_comp)+b_diff_cyl{3,j,i}(:,b_comp)-b_diff_cyl{5,j,i}(:,b_comp)-b_diff_cyl{6,j,i}(:,b_comp)...
                                        );
            X5_diff(j,i)=    2*b_diff_cyl{1,j,i}(:,b_comp)+2*b_diff_cyl{4,j,i}(:,b_comp)...
                            -1*	(...
                                b_diff_cyl{2,j,i}(:,b_comp)+b_diff_cyl{6,j,i}(:,b_comp)+b_diff_cyl{3,j,i}(:,b_comp)+b_diff_cyl{5,j,i}(:,b_comp)...
                                );
            X6_diff(j,i)=    sqrt(3)*	( ...
                                b_diff_cyl{2,j,i}(:,b_comp)-b_diff_cyl{3,j,i}(:,b_comp)+b_diff_cyl{5,j,i}(:,b_comp)-b_diff_cyl{6,j,i}(:,b_comp)...
                                        );  
        end
            %angle vectors are 'celled' for each displacement... they grow to
            %the right with the turning angle j
            theta{i}=       [X1_diff(:,i),X2_diff(:,i)];
            alpha{i}=       atan2(X2_diff(:,i),X1_diff(:,i));
            pos_rt{i}=      [X5_diff(:,i),X6_diff(:,i)];
            %%denominator of position, so that length comes out 
    %         pos_st{i}=      d0./(X1_diff(:,i).^2+X2_diff(:,i).^2);        
            for k = 1 : size(X1_diff,1)
                aux=  d0./(X1_diff(k,i).^2+X2_diff(k,i).^2) ...
                                .*[X1_diff(k,i),X2_diff(k,i); ...
                                -X2_diff(k,i),X1_diff(k,i)] ...
                                *pos_rt{i}(k,:)';  
                pos_st{i}(:,k)=aux';
            end
    end
end