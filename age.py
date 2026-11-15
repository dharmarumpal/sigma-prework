# CALCULATE AGE USING BIRTHDATE INPUT

from datetime import date

date_now = date.today()


def convert_inputted_age_to_date():
    print("Please enter your birthday: ")
    print("Example (01/01/2001)")
    day = int(input("birth day: "))
    month = int(input("birth month: "))
    year = int(input("birth year: "))
    birth_date = date(year, month, day)
    return birth_date


def calculate_age(birth_date):
    age = date_now.year - birth_date.year

    if (date_now.month, date_now.day) < (birth_date.month, birth_date.day):
        age -= 1

    if age > 1:
        print("You are " + str(age) + " years old!")
    else:
        print("You are " + str(age) + " year old!")


calculate_age(convert_inputted_age_to_date())
