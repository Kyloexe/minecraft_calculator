# Author: Kyle Murphy
# Modified by: Patryk
# Purpose: This is a basic calculator geared towards Minecraft

from re import search

# CONSTANTS
TICKS_IN_ONE_DAY = 24000
ONE_HOUR_IN_TICKS = 1000
ONE_MINUTE_IN_SECONDS = 60

# FUNCTIONS
def calculator(mode, secondaryMode=None):
    if mode == "tick":
        if secondaryMode == "year":
            days = input("Please input the number of days: ")
            if search(r"/[A-Za-z]/g", days):
                raise Exception("You can only have floats or integers for the amount of days") 

            days = float(days)    
            ticks_calculated = TICKS_IN_ONE_DAY * days
            print(f"{days:.2f} days would be equal to {ticks_calculated:.0f} minecraft ticks.")

    elif mode == "time":
        time = input("Please input the time in the 24 hour format: HH:MM:SS*: ")
        if not search(r"^([0-1]?\d|2[0-3])(?::([0-5]?\d))?(?::([0-5]?\d))?$", time):
            raise Exception("Invalid Time format")
        time_split = time.split(":")

        time_hour = int(time_split[0])
        time_minutes = int(time_split[1])
        time_seconds = int(time_split[2])

        hours_in_ticks = time_hour * ONE_HOUR_IN_TICKS
        minutes_and_seconds_in_ticks = (
                    (ONE_HOUR_IN_TICKS * time_minutes) / 60 + ONE_HOUR_IN_TICKS * time_seconds / 60)
        final_time = hours_in_ticks + minutes_and_seconds_in_ticks
        print(f"The time you inputted was {time}, this time in ticks"
                f" is {final_time:.0f} ticks")

    else:
        return print("The only available options for the calculator are: tick; time")



print("AVAILABLE MODES:")
print("=> tick")
print("=> time")
print()

calc_mode = input("Select the mode you'd like to use:")
print()

if calc_mode == "tick":
    print("AVAILABLE MODES:")
    print("=> year")
    print()

    secondary_mode = input("Select the secondary mode you'd like to use:")
    calculator(calc_mode, secondary_mode)

calculator(calc_mode)