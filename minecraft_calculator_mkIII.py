# Kyle Murphy
# This is a basic calculator geared towards Minecraft

import math
import sys

TICKS_IN_ONE_DAY = 24000
ONE_HOUR_IN_TICKS = 1000
ONE_MINUTE_IN_SECONDS = 60


def minecraft_calculator():
    calculator_mode = input("Please input the mode you'd like to use: ")
    if calculator_mode == 'ticks' or 'tick':
        def ticks_calculator():
            ticks_calculator_mode = input("Please input the mode you'd like to use: ")
            if ticks_calculator_mode == 'year':
                def ticks_year():
                    orbital_period = float(input("Please input the number of days in a year: "))
                    ticks_in_one_year = TICKS_IN_ONE_DAY * orbital_period
                    print(f"Your world's year lasts {orbital_period:.0f} days, this number in ticks is"
                          f" {ticks_in_one_year:.0f} ticks")
                ticks_year()
        ticks_calculator()
    else:
        print("Hey, I think you mistyped")

    if calculator_mode == 'time' or 'Time':
        def ticks_calculator_time():
            time_hour = int(input("Please input the hour displayed on the clock: "))
            time_minutes = int(input("Please input the minutes displayed on the clock: "))
            time_seconds = int(input("Please input the seconds displayed on the clock: "))

            hours_in_ticks = time_hour * ONE_HOUR_IN_TICKS
            minutes_and_seconds_in_ticks = (
                        (ONE_HOUR_IN_TICKS * time_minutes) / 60 + ONE_HOUR_IN_TICKS * time_seconds / 60)
            final_time = hours_in_ticks + minutes_and_seconds_in_ticks
            print(f"The time you inputted was {time_hour}:{time_minutes}:{time_seconds}, this time in ticks"
                  f" is {final_time:.0f} ticks")

        ticks_calculator_time()


minecraft_calculator()
