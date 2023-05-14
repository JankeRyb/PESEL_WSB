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


birth_day=input_exceptions.birth_day_input('Input your birthdate - Day (1 - 31): ')


gender = input_exceptions.gender_input('Male/Female - M/F: ')
# PESEL RRMMDDLLLLK
# #Losowe cyfry - L
# Cyfra kontrolna - K
