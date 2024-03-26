# Receive Numbers From User (String)
number1 = input("insert the first number here: ".title())
number2 = input("insert the second number here: ".title())

# Check The Quality Of Input
while number1.isalpha() or number2.isalpha():
    print("please insert just integers!!!".title())
    number1 = input("insert the first number here: ".title())
    number2 = input("insert the second number here: ".title())

# Start The Calculation System --- Infinitive Loop
while True:
    # Change Numbers To Int Form, Which Is Allowed and Standard In This System
    number1 = int(number1)
    number2 = int(number2)

    if number1 == 0:  # Check The Being Zero Of First Number
        print(
            "first number should not be zero in order to have a better calculations".title()
        )
        number1 = int(input("insert the first number here: ".title()))
        number2 = int(input("insert the second number here: ".title()))

    elif number1 < number2:  # Check The Priority Of Numbers For Better Calculations
        print(
            "the number 1 should be more than number 2 in order to have a better calculations"
        )
        number1 = int(input("insert the first number here: ".title()))
        number2 = int(input("insert the second number here: ".title()))

    elif number1 == number2:  # Check The Numbers Equality
        print(
            "the number 1 should not be similar to number 2 in order to have a better calculations"
        )
        number1 = int(input("insert the first number here: ".title()))
        number2 = int(input("insert the second number here: ".title()))

    else:  # Start The Pre-Calculations
        print("number 1 + number 2 = ", number1 + number2)
        print("number 1 - number 2 = ", number1 - number2)
        print("number 1 * number 2 = ", number1 * number2)
        print("number 1 ** number 2 = ", number1**number2)
        print("number 1 / number 2 = ", number1 / number2)
        print("number 1 // number 2 = ", number1 // number2)
        print("number 1 % number 2 = ", number1 % number2)  # End Of Calculations
        number1 = input(
            "insert the first number here: ".title()
        )  # Start By Receiving New Numbers (String)
        number2 = input("insert the second number here: ".title())
        while number1.isalpha() or number1.isalpha():  # Check The Quality Of Inputs
            print("please insert just integers!!!".title())
            number1 = input("insert the first number here: ".title())
            number2 = input("insert the second number here: ".title())
# End Of While Loop And If Conditions
