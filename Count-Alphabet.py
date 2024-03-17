# Get User Fullname
userName = input("enter your fullname here: ".title())

# change all characters to lower cases
userName = userName.casefold()

# Remove Spaces From The Name
userName = userName.replace(" ", "")

# Main Function (Loop)

iteratedCharacters = []

for items in userName:
    if items not in iteratedCharacters:
        print("Your Name Has {} {}".format(userName.count(items), items))
        iteratedCharacters.append(items)
else:
    print("We counted the characters".title())
