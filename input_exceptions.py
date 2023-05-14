def birth_year_input(message):
    while True:
        try:
            birth_year = int(input(message))
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
            assert 10 <= birth_month <= 12
            return birth_month
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Year MUST BE between 1800 and 2299')

#czy robimy test na rok przestepny i luty 28/29 dni???

def birth_day_input(message):
    while True:
        try:
            birth_day = int(input(message))
            assert 1 <= birth_day <= 31
            return birth_day
        except ValueError:
            print("Not a valid number, try again")
        except AssertionError:
            print('Year MUST BE between 1 and 31')

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

