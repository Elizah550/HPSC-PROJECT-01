% Matrix-Matrix product experiment
clear all; % start fresh

n = 1000;

A = rand(n,n);
B = rand(n,n);
C = zeros(n,n);
CC = zeros(n,n);

tic
for i = 1:n
    for j=1:n
         for k=1:n
            C(i,j) = C(i,j) + A(i,k)*B(k,j);
         end
    end
end
timeloop = toc

tic
for j = 1:n
    CC(:,j) = A*B(:,j);
end
timeloopvec = toc

tic
    CCC = A*B;
timevec = toc

norm(C-CC)
norm(C-CCC)

Speedup = timeloop/timeloopvec
Speedup2 = timeloop/timevec
Speedup3 = timeloopvec/timevec