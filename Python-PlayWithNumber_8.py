# very simple code just for training basic materials in python!
print(str("🙋‍♂️ Developed by Kasra10 - https://www.kasra10design.com"))
print(
    ' "In this small game, every chosen number will always result in the number 8." 😁'
)
print(
    """Instructions:
1- a number from 1 to 9
2- chosen number * 2
3- result + 8
4- result + first chosen number
5- result - 2
6- result / 3
7- result - first chosen number
8- result * 4
Final result is always 8 😊"""
)
print(
    "---------------------------------------- ⬇️Lets Play!⬇️ ----------------------------------------"
)
firstNumber = float(input("Step 1: Please choose a number between 1 - 9: "))
firstNumber = int(firstNumber)
earliestNumber = firstNumber
if firstNumber == 0:
    print("Your chosen Number is 0 😱 start again")
elif firstNumber > 9:
    print("Your chosen number is more than Nine 🤦‍♂️ start again")
else:
    firstNumber *= 2
    print("Step 2: chosen number * 2 = ", firstNumber)
    firstNumber += 8
    print("Step 3: result + 8 = ", firstNumber)
    firstNumber += earliestNumber
    print("Step 4: result + first chosen number = ", firstNumber)
    firstNumber -= 2
    print("Step 5: result - 2 = ", firstNumber)
    firstNumber //= 3
    print("step 6: result / 3 = ", firstNumber)
    firstNumber -= earliestNumber
    print("step 7: result - first chosen number = ", firstNumber)
    firstNumber *= 4
    print("step 8: result * 4 = ", firstNumber, "😁")
