# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
import random

# My Solution
timezone_indices = random.sample(range(1, len(pytz.all_timezones)), 9)

available_timezones = {}
for i in range(1, len(timezone_indices) + 1):
    available_timezones[i] = pytz.all_timezones[timezone_indices[i-1]]

for zone in sorted(available_timezones):
    print('\t{}: {}'.format(zone, available_timezones[zone]))

while True:
    choice = int(input('Please select a timezone (or 0 to quit): '))

    if choice == 0:
        break

    if choice in available_timezones.keys():
        selected_tz = pytz.timezone(available_timezones[choice])
        selected_tz_time = datetime.datetime.now(selected_tz)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        print('The time in {} is {} {}'.format(
            available_timezones[choice],
            selected_tz_time.strftime('%Y-%m-%d %H:%M:%S %z'),
            selected_tz_time.tzname()
        ))
        print('The local time is {}'.format(
            local_time.strftime('%Y-%m-%d %H:%M:%S')
        ))
        print('The utc time is {}'.format(
            utc_time.strftime('%Y-%m-%d %H:%M:%S')
        ))

# Professor Solution
# available_zones = {'1': "Africa/Tunis",
#                    '2': "Asia/Kolkata",
#                    '3': "Australia/Adelaide",
#                    '4': "Europe/Brussels",
#                    '5': "Europe/London",
#                    '6': "Japan",
#                    '7': "Pacific/Tahiti",
#                    '8': "US/Hawaii",
#                    '9': "Zulu"}

# print("Please choose a time zone (or 0 to quit):")
# for place in sorted(available_zones):
#     print("\t{}. {}".format(place, available_zones[place]))

# while True:
#     choice = input()

#     if choice == '0':
#         break

#     if choice in available_zones.keys():
#         tz_to_display = pytz.timezone(available_zones[choice])
#         world_time = datetime.datetime.now(tz=tz_to_display)
#         print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'),world_time.tzname()))
#         print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
#         print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
#         print()
