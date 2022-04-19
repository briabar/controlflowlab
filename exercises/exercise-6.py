# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

def calculate_season():
    month = input('Enter the month of the year (Jan - Dec): ')
    day = input('Enter the day of the month: ')
    if month.upper() in ('DEC', 'MAR', 'JUN', 'SEP'):
        if month.upper() == 'DEC' and day >= 21:
            season = 'Winter'
        elif month.upper() == 'MAR' and day <= 19:
            season = "Winter"
        elif month.upper() == 'MAR' and day >= 20:
            season = 'Spring'
        elif month.upper() == 'JUN' and day <= 20:
            season = 'Spring'
        elif month.upper() == 'JUN' and day >= 21:
            season = 'Summer'
        elif month.upper() == 'SEP' and day <= 21:
            season = 'Summer'
        elif month.upper() == 'SEP' and day >= 22:
            season = 'Fall'
        elif month.upper() == 'DEC' and day <= 20:
            season = 'Fall'    
    else:
        if month.upper() == 'JAN':
            season = 'Winter'
        elif month.upper() == 'FEB':
            season = 'Winter'
        elif month.upper() == 'APR':
            season = 'Spring'
        elif month.upper() == 'MAY':
            season = 'Spring'
        elif month.upper() == 'JUL':
            season = 'Summer'
        elif month.upper() == 'AUG':
            season = 'Summer'
        elif month.upper() == 'OCT':
            season = 'fall'
        elif month.upper() == 'NOV':
            season = 'fall'

    return f'{month} {day} is in {season} '


print(calculate_season())