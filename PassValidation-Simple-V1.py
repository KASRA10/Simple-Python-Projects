def passwordValidate(UserPassword):
    if len(UserPassword) < 8:
        print("your password must be more than 8 characters".title())
    elif UserPassword.isnumeric():  # it checks if all characters are umber or not
        print("your password must have at least one letter".title())
    elif UserPassword.isalpha():  # it checks if all characters are letter or not
        print("your password must have at least one number".title())
    else:
        print("Your password is perfect".title())


while True:
    UserPassword = input("enter your password here: ".title())
    passwordValidate(UserPassword)
