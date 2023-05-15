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


if gender == "M":
    test_list=[1,3,5,7,9]
    gender_random = random.sample(test_list,1)
else:
    test_list=[0,2,4,6,8]
    gender_random = random.sample(test_list,1)


year = '%02d' % (birth_year % 100)
month = '%02d' % birth_month
day = '%02d' % birth_month


three_random = random.randint(100,999)
three_random = str(three_random)

a = year[0]
a = int(a)

b = year[1]
b = int(b)

c = month[0]
c = int(c)

d = month[1]
d = int(d)

e = day[0]
e = int(e)

f = day[1]
f = int(f)

g = three_random[0]
g = int(g)

h = three_random[1]
h = int(h)

i = three_random[2]
i = int(i)

j = gender_random[0]
j = int(j)



check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j
if check % 10 == 0:
    last_digit = 0
else:
    last_digit = 10 - (check % 10)

print('%02d' % (birth_year % 100), end='')
print('%02d' % birth_month, end='')
print('%02d' % birth_day, end='')
print(three_random, end='')
print(j, end='')
print(last_digit)
# PESEL RRMMDDLLLLK
# Losowe cyfry - L
# Cyfra kontrolna - K
