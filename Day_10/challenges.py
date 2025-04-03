## title normalized text to capitalize first letter, lowercase the rest

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"

# print(format_name("BiLl", "Johnson"))


# Echo text func

# def echo(text):
#     return text + text

# def format(text):
#     return text.title()

# print(format(echo("Hello")))

################################################### challenge: is it a leap year?   ################################

# Leap Year
# 💪 This is a difficult challenge! 💪 

# Write a program that returns True or False whether if a given year is a leap year.

# A normal year has 365 days, leap years have 366, with an extra day in February. 


# This is how you work out whether if a particular year is a leap year. 

# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder 

# - unless the year is also divisible by 400 with no remainder   

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(is_leap_year(2024))