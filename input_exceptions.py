def CheckLeap(Year):
  # Checking if the given year is leap year
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    #print("Given Year is a leap Year")
    return ("True")
  # Else it is not a leap year
  else:
    #print ("Given Year is not a leap Year")
    return ("False")
# Taking an input year from user

def birth_year_input(message):
    while True:
        try:
            birth_year = int(input(message))
            CheckLeap(birth_year)
            assert 1800 <= birth_year <= 2299
            return birth_year
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Year MUST BE between 1800 and 2299')

def birth_month_input(message):
    while True:
        try:
            birth_month = int(input(message))
            assert 1 <= birth_month <= 12
            return birth_month
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Month MUST BE between 1 and 12')

#czy robimy test na rok przestepny i luty 28/29 dni???


def birth_day_input_28(message):
    while True:
        try:
            birth_day = int(input(message))
            assert 1 <= birth_day <= 28
            return birth_day
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Day MUST BE between 1 and 28')

def birth_day_input_29(message):
    while True:
        try:
            birth_day = int(input(message))
            assert 1 <= birth_day <= 29
            return birth_day
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Day MUST BE between 1 and 29')
def birth_day_input_30(message):
    while True:
        try:
            birth_day = int(input(message))
            assert 1 <= birth_day <= 30
            return birth_day
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Day MUST BE between 1 and 30')
def birth_day_input_31(message):
    while True:
        try:
            birth_day = int(input(message))
            assert 1 <= birth_day <= 31
            return birth_day
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Day MUST BE between 1 and 31')

def gender_input(message):
    while True:
        try:
            gender=input(message).upper()
            if gender == "M":
                return gender
            elif gender=="F":
                return gender
            else:
                print ("Gender invalid")
        except ValueError:
            print ("Gender invalid")

