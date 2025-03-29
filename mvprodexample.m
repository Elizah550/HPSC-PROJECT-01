% Matrix-Vector product experiment
clear all; % start fresh

n = 10000;

A = rand(n,n);
x = rand(n,1);
b = zeros(n,1);
bb = zeros(n,1);

tic
for i = 1:n
    for j=1:n
    b(i) = b(i) + A(i,j)*x(j);
    end
end
timeloop = toc

tic
for i = 1:n
    bb(i) = A(i,:)*x;
end
timeloopvec = toc

tic
    bbb = A*x;
timevec = toc

norm(b-bb)
norm(b-bbb)

Speedup = timeloop/timeloopvec
Speedup2 = timeloop/timevec
Speedup3 = timeloopvec/timevec