# Main Function to Calculate our Date
def charCounter(username):
    # Empty Variables
    lowCounter = 0
    upCounter = 0
    spaces = 0

    # Checking Conditions
    for items in username:  # To Iterate each Character
        if items.islower():
            lowCounter += 1
        elif items.isupper():
            upCounter += 1
        elif items == " ":
            spaces += 1
        else:  # Just For Complete Use Of if Condition Options
            pass

    print(
        f"your name has {lowCounter} lower character \nyour in name has {upCounter} upper character\nyour name has {spaces} space".title()
    )


while True:  # Use While Infinity Loop To Run The Code Agin Automatically
    # Receive String From User
    username = input("enter your username here: ".title())

    # Use Of Function With An Argument
    charCounter(username)

    # Ask User If Wants to Continue Or Not
    choice = input(
        "Do you want to enter another username?\t".title() + "(yes/no): ".casefold()
    )

    if choice != "yes":  # Check Exit Condition
        break
