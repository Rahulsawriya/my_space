from time import time, sleep
start_time = time()

# Replace sleep(75) below with code you want to time
sleep(30)

# Sets end time
end_time = time()

# Computes overall runtime in seconds
tot_time = end_time - start_time

# Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")

# Prints overall runtime in format hh:mm:ss
print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
          str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
          str( int(  ( (tot_time % 3600) % 60 ) ) ) )

"""Note: Instead of rounding to the nearest second, our code using the int() function and will truncate the value of seconds. 
This means if your Total Runtime: 4.519087974567, then it would be formatted to Total Runtime: 0:0:4. If you instead 
want to round to the nearest second, you will want to replace the int() function with the round() function in calculating the number of seconds above."""


