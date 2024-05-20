%%% Readin CSV %%%

%%readin 
[file, path] = uigetfile('*.csv', ' Please choose file');
filename = [path, file];

%save as table
Data_table = readtable(filename); 

%save as struct
Data_struct = table2struct(Data_table); 

%% rename
% Struct_x.Time = Data_table(:,1);
% Struct_x.Velocity = Data_table(:,2);
% Struct_x.Elevation = Data_table(:,3);


%% replace NAN
% function [Profile] = deletenans (Profile)
%   nanx = isnan(Profile);
%   t    = 1:numel(Profile);
%   Profile(nanx) = interp1(t(~nanx), Profile(~nanx), t(nanx));
% end

% clearvars file filename 

