% Matrix-based dot product experiment with profiling
clear all; % Start fresh
% Start the profiler
profile on
n = 10000; % Decide the length of the vectors
a = rand(n, 1); % Create a random column vector a
b = rand(n, 1); % Create a random column vector b
% Dot product using matrix multiplication (vectorized operation)
tic
c = a.' * b; % Transpose a and multiply with b
timevec = toc;
% Display the result
disp('Dot product result:');
disp(c);
disp('Time taken with matrix-based dot product:');
disp(timevec);
% Stop the profiler and display the profile report
profile off
profile viewer

 
