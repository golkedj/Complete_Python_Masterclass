# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.
import time

# My Solution
# print(time.get_clock_info('time'))
# print(time.get_clock_info('perf_counter'))
# print(time.get_clock_info('monotonic'))
# print(time.get_clock_info('process_time'))

# Professor Solution
print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t\t", time.get_clock_info('perf_counter'))
print("monotonic():\t\t", time.get_clock_info('monotonic'))
print("process_time():\t\t", time.get_clock_info('process_time'))
