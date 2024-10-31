% Clear workspace and command window
clear all;
clc;

% Create a parallel pool if none exists
if isempty(gcp())
   parpool();
end

% Number of workers
nworkers = gcp().NumWorkers;

% Define integration limits
xMin = 0;
xMax = 1; % Match limits with Code 01
yMin = 0;
yMax = 1;

% Discretize the interval for x
xSplit = linspace(xMin, xMax, nworkers + 1); % Split x limits

% Initialize total integral value
totalIntegral = 0;

% Perform the double integral in SPMD
tic
spmd
   % Each worker gets its own subregion for x
   ainit = xSplit(labindex);       % Left limit for x
   bfin = xSplit(labindex + 1);    % Right limit for x

   % Perform the double integral using the external function
   localIntegral = integral2(@myFunction, ainit, bfin, yMin, yMax);
  
   % Combine the results from all workers
   totalIntegral = gplus(localIntegral); % Global sum across all workers
end
toc

disp(['Total integral value: ', num2str(totalIntegral{1})]);

% Function to integrate
function z = myFunction(x, y)
   z = x .* y; % Example function f(x,y) = x * y
end
