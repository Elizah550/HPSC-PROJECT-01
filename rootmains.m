clear all; close all; % Start fresh

%Organizing Inputs%
f = @(x) sin(3*pi*cos(2*pi*x).*sin(pi*x));
a = -3; b = 5; n = 4^9;
x0 = linspace(a,b,n); % Vector containing initial starting points
q = zeros(size(x0)); % Preallocate a vector for storing roots.
%%%%%%%%%%%%%%%%%%

tic
for i=1:n
    q(i) = fzero(f,x0(i));
end
toc

%Processing Outputs%
q = unique(q); % keep roots with unique values only.

showsavePlot = true; 
switch showsavePlot
    case true
        %Plot the function and roots if possible
        xx = linspace(a,b,1001);
        fig = figure('Position',[100 100 1200 300]);
        plot(xx,f(xx),'-k','linewidth',2);
        hold on
        plot(q,f(q),'o','markerfacecolor','r')
        xlim([a,b]); ylim([-1,1]);
        yticks([-1 0 1])
        xlabel('x'); ylabel('f(x)');
        pbaspect([4 1 1])
        print(fig,'MySavedPlot','-dpng')
end