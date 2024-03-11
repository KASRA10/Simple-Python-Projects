# import vitals
import time
import os

while True:  # Use while For This Specific Code To Restart Again
    # welcome
    print(
        """     ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️    Welcome to our website    ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️     """.title()
    )
    # To Clear The Terminal
    time.sleep(4)
    os.system("cls")
    time.sleep(2)

    # Specify the user's request
    userOperation = input(
        "please select your operation 1 / 2\n1 = create a new account - signup\n2 = login - sign in\n0 = exit\ninsert: ".title()
    )

    # Provide a list of options
    optionList = ["0", "1", "2"]

    # Define Main Mechanism

    # wrong input
    while userOperation not in optionList:
        print("sorry, your input is not correct ☹️".title())
        userOperation = input(
            "please select your operation 1 / 2\n1 = create a new account - sign up\n2 = log in - sign in\n0 = exit\ninsert: ".title()
        )

    # Sing up / sign in / Exit Operation

    # Users Database
    users_database = {
        "user0_username": "admin",
        "user0_email": "domain-mail",
        "user0_pass": "admin",
        "user1_username": "benz",
        "user1_email": "benz-mail",
        "user1_pass": "Benz@1023",
        "user2_username": "chrome",
        "user2_email": "chrome-mail",
        "user2_pass": "Chrome&^6547",
    }

    # Special Characters Essentials For a Safe Password
    specialCharacters = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "=",
        "+",
        "/",
        "\\\\",
        "?",
        ",",
        "|",
        "~",
        "`",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    if userOperation == "1":
        # SingUp Form
        newUser_username = input("Username: ".title())
        newUser_email = input("email: ".title())
        newUser_password = input("password: ".title())

        # Check if the password is secure
        while not any(chr in newUser_password for chr in specialCharacters):
            print(
                "for security reasons you should use special characters and numbers in your password 🔐\n(capital letters are not required.)".title()
            )
            newUser_password = input("password: ".title())
        rePass = input("re-password: ".title())

        # Rapid Check the correction between two input passwords
        while newUser_password != rePass:
            print("your password are not similar, please be careful  🤦‍♂️ ".title())
            newUser_password = input("password: ".title())
            rePass = input("re-password: ".title())
        while newUser_username and newUser_password == "admin":
            print("access denied, this is administrator token pass.  ⛔ ".title())
            newUser_username = input("Username: ".title())
            newUser_email = input("email: ".title())
            newUser_password = input("password: ".title())
            rePass = input("re-password: ".title())
            while newUser_password != rePass:
                print("your passwords are not similar, please be careful  🤦‍♂️ ".title())
                newUser_password = input("password: ".title())
                rePass = input("re-password: ".title())

        # Store Users Information to the Database
        users_database.update({"user1_username": newUser_username})
        users_database.update({"user1_email": newUser_email})
        users_database.update({"user1_password": newUser_password})
        print(
            "thank you for your registration, the login email has been sent. please check your mail box 📧 ".title()
        )
        time.sleep(3)
        os.system("cls")

    # LogIn For Registered Users

    # Get Input From User
    elif userOperation == "2":
        print(" ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️  LogIn ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️")
        registeredUser_usernameOrMail = input("Username or email: ".title())
        registeredUser_password = input("password: ".title())
        while (
            registeredUser_usernameOrMail
            and registeredUser_password
            not in users_database.values()  # Use values() method to check the input with values on our Database(Dictionary)
        ):
            print("your username/email or password is wrong!")
            registeredUser_usernameOrMail = input("Username or email: ".title())
            registeredUser_password = input("password: ".title())
        print("Welcome back 😀 ".title())
        time.sleep(3)
        os.system("cls")

    else:  # 0 == Exit from process
        print("goodbye, thank for your time ❤️".title())
        time.sleep(3)
        os.system("cls")
