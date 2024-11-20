clear; close all;

maxIterations = 1000; 
gridDimension = 2000; 
numBlocks = 2;  % number of blocks in each dimension
pointsPerBlock = gridDimension / numBlocks; 
xRange = [-0.748766713922161, -0.748766707771757]; 
yRange = [0.123640844894862, 0.123640851045266]; 

% Generate subintervals for x and y axes
xIntervals = linspace(xRange(1), xRange(2), numBlocks + 1); 
yIntervals = linspace(yRange(1), yRange(2), numBlocks + 1); 

tic();
pixelCount = zeros(gridDimension, gridDimension); 

for blockIndex = 1:(numBlocks * numBlocks)
    rowIndex = ceil(blockIndex / numBlocks); 
    colIndex = mod(blockIndex - 1, numBlocks) + 1; 
    xStartValue = xIntervals(colIndex); 
    xEndValue = xIntervals(colIndex + 1); 
    yStartValue = yIntervals(rowIndex); 
    yEndValue = yIntervals(rowIndex + 1); 
    
    xPoints = linspace(xStartValue, xEndValue, pointsPerBlock); 
    yPoints = linspace(yStartValue, yEndValue, pointsPerBlock); 
    [X, Y] = meshgrid(xPoints, yPoints); 
    initialZ = X + 1i * Y; 
    Z = initialZ; 
    
    for n = 0:maxIterations
        Z = Z .^ 2 + initialZ; 
        insideRegion = abs(Z) <= 2; 
        
        pixelCount(rowIndex * pointsPerBlock - (pointsPerBlock - 1): ...
            rowIndex * pointsPerBlock, colIndex * pointsPerBlock - (pointsPerBlock - 1): ...
            colIndex * pointsPerBlock) = pixelCount(rowIndex * pointsPerBlock - (pointsPerBlock - 1): ...
            rowIndex * pointsPerBlock, colIndex * pointsPerBlock - (pointsPerBlock - 1): ...
            colIndex * pointsPerBlock) + insideRegion; 
    end
end

pixelCount = log(pixelCount); 

% Display results
elapsedTime = toc(); 
set(gcf, 'Position', [200, 200, 600, 600]); 
imagesc(pixelCount); 
axis image; 
axis off; 
colormap([jet(); flipud(jet()); 0 0 0]); 
drawnow; 
title(sprintf('%1.2f seconds (without spmd)', elapsedTime)); 
