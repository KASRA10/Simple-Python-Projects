# Define The Number Checker Function
def numberChecker(userNumber=0):
    # Check The String That Consisted Of 0 to 9 Digital Characters
    while not userNumber.isdigit():
        print(
            "please enter just numbers (jut integer, Example = 1000)\n(without spaces)\n* note: it is 0 by default *".title()
        )
        userNumber = input("enter your number here: ".title())
    else:
        pass

    # Turn Input String To Integer Number
    userNumber = int(userNumber)

    # Check Number Zero
    if userNumber == 0:
        print("please insert numbers except zero".title())
    # Calculating If Number Is Odd Or Even
    elif userNumber % 2:
        print(f'your number "{userNumber}" is ODD'.title())
    else:
        print(f'your number "{userNumber}" is Even'.title())


# Using While for Run Program Automatically
while True:
    # Get Number From User
    userNumber = input("enter your number here: ".title())
    numberChecker(userNumber)

    # Ask User to Continue Or Not
    choice = input(
        "Do you want to try other number\t".title() + "(yes/no): ".casefold()
    )
    if choice.lower() != "yes":
        print("thanks for your time".title())
        break  # Exit While Loop
