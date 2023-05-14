import random
import input_exceptions
#birth_year=input('Input your birthdate - Year (1800 - 2299): ')


birth_year=input_exceptions.birth_year_input('Input your birthdate - Year (1800 - 2299): ')
print(birth_year)
# if input_exceptions.CheckLeap(True):
#     print("True")
# else:
#     print("False")
birth_month=input_exceptions.birth_month_input('Input your birthdate - Month (1 - 12): ')

if birth_month==2:
    if input_exceptions.CheckLeap(birth_year)=="True":
        birth_day=input_exceptions.birth_day_input_29('Input your birthdate - Day (1 - 29): ')
    else:
        birth_day=input_exceptions.birth_day_input_28('Input your birthdate - Day (1 - 28): ')
elif birth_month in (4, 6, 9, 11):
    birth_day=input_exceptions.birth_day_input_30('Input your birthdate - Day (1 - 30): ')
else:
    birth_day=input_exceptions.birth_day_input_31('Input your birthdate - Day (1 - 31): ')




gender = input_exceptions.gender_input('Male/Female - M/F: ')
# PESEL RRMMDDLLLLK
# #Losowe cyfry - L
# Cyfra kontrolna - K
