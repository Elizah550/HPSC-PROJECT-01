function timeconsumingfun
    % Generate a random integer between 1 and 5
    pauseDuration = randi([1, 5]); 
    fprintf('Pausing for %d seconds...\n', pauseDuration); % Display the pause duration
    pause(pauseDuration);           % Pause for the random duration
end
% function timeconsumingfun
%     pause(5)
% end