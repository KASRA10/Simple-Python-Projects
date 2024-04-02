# Describe A Function To Check The Year Number
def yearChecker(usrBirthYear=0):
    while (
        not usrBirthYear.isdigit()
        or len(usrBirthYear) < 4
        or usrBirthYear == 0
        or int(usrBirthYear) > 2024
    ):
        print(
            "⚠️  please enter just an applicable integer numbers (from 1899 to 2024)\n⚠️  example = 1994\n⚠️  0 is not accepted!".title()
        )
        usrBirthYear = input("enter your birth year here: ".title())
    else:
        pass


# Describe A Function To Check The Month Number
def monthChecker(usrBirthMonth=0):
    while (
        not usrBirthMonth.isdigit()
        or len(usrBirthMonth) > 2
        or usrBirthMonth == 0
        or int(usrBirthMonth) > 12
    ):
        print(
            "⚠️  please enter just an applicable integer numbers (from 1 to 12)\n⚠️  example = 10\n⚠️  0 is not accepted!".title()
        )
        usrBirthMonth = input("enter your birth month here: ".title())
    else:
        pass


# Describe A Function To Check The Day Number
def dayChecker(usrBirthDay=0):
    while (
        not usrBirthDay.isdigit()
        or len(usrBirthDay) > 2
        or usrBirthDay == 0
        or int(usrBirthDay) > 31
    ):
        print(
            "⚠️  please enter just an applicable integer numbers (from 1 to 31)\n⚠️  example = 7\n⚠️  0 is not accepted!".title()
        )
        usrBirthDay = input("enter your day year here: ".title())
    else:
        pass


# Describe A Function For Converting Year
def convertor(usrBirthYear, usrBirthMonth, usrBirthDay):
    usrBirthYear = int(usrBirthYear)
    usrBirthMonth = int(usrBirthMonth)
    usrBirthDay = int(usrBirthDay)
    if usrBirthMonth > 10 or usrBirthDay > 10 and usrBirthMonth == 10:
        calculatedYear = usrBirthYear + 622
    else:
        calculatedYear = usrBirthYear + 621
        print(f"your birthday a.c year is {calculatedYear}".title())


# Get User Birth Date Distinctively
# Receive Birth Year
usrBirthYear = input("enter your birth year here: ".title())
yearChecker(usrBirthYear)

# Receive Birth Month
usrBirthMonth = input("enter your birth Month here: ".title())
monthChecker(usrBirthMonth)

# Receive Birth Day
usrBirthDay = input("enter your birth day here: ".title())
dayChecker(usrBirthDay)

# Run Convertor
convertor(usrBirthYear, usrBirthMonth, usrBirthDay)
