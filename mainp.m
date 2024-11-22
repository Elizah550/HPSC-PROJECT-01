if isempty(gcp())
    parpool();
end

n = 70;
tic
parfor i = 1:n
    timeconsumingfun
end
tp = toc;    