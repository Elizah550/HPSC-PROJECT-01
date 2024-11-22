import time
import random

def timeconsumingfun(arg):
    # Generate a random integer between 1 and 5
    pause_duration = random.randint(1, 5) 
    print(f'Pausing for {pause_duration} seconds...')  # Display the pause duration
    time.sleep(pause_duration)  # Pause for the random duration

# import time
# def timeconsumingfun(arg):
#     time.sleep(5)