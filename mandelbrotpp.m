clear; close all; pool = gcp('nocreate'); if ~isempty(pool), delete(pool); end
parpool(4);

numWorkers = gcp().NumWorkers; 
maxIterations = 1000; 
gridDimension = 2000; 
numBlocks = 2;  % blocks in both dimensions
pointsPerBlock = gridDimension / numBlocks; 
xRange = [-0.748766713922161, -0.748766707771757]; 
yRange = [0.123640844894862, 0.123640851045266];

% Define subintervals for x and y axes
xIntervals = linspace(xRange(1), xRange(2), numBlocks + 1); 
yIntervals = linspace(yRange(1), yRange(2), numBlocks + 1); 

tic();
spmd
    idx = labindex(); 
    rowIndex = ceil(idx / numBlocks); 
    colIndex = mod(idx - 1, numBlocks) + 1; 
    xStartVal = xIntervals(colIndex); 
    xEndVal = xIntervals(colIndex + 1); 
    yStartVal = yIntervals(rowIndex); 
    yEndVal = yIntervals(rowIndex + 1); 
    xPoints = linspace(xStartVal, xEndVal, pointsPerBlock); 
    yPoints = linspace(yStartVal, yEndVal, pointsPerBlock); 
    [X, Y] = meshgrid(xPoints, yPoints); 
    initialZ = X + 1i * Y; 
    pixelCount = ones(size(initialZ)); 
    
    % Iterative calculation
    Z = initialZ; 
    for iter = 0:maxIterations
        Z = Z .^ 2 + initialZ; 
        isInside = abs(Z) <= 2; 
        pixelCount = pixelCount + isInside; 
    end
    pixelCount = log(pixelCount); 
end

% Display results
elapsedTime = toc(); 
set(gcf, 'Position', [200, 200, 600, 600]); 
imagesc(cat(2, xPoints{:}), cat(2, yPoints{:}), cat(1, pixelCount{:})); 
axis image; 
axis off; 
colormap([jet(); flipud(jet()); 0 0 0]); 
drawnow; 
title(sprintf('%1.2f seconds (using spmd)', elapsedTime)); 
