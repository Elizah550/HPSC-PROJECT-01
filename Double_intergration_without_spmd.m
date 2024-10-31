% Clear workspace and command window
clear all;
clc;

% Define the function to integrate
f = @(x, y) x .* y; % Given function

% Define integration limits
xMin = 0;
xMax = 1; % x limits
yMin = 0;
yMax = 1; % y limits

tic
% Perform the double integral using integral2
totalIntegral = integral2(f, xMin, xMax, yMin, yMax);
toc

% Display the total integral value
disp(['Total integral value: ', num2str(totalIntegral)]);
