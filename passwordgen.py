import random
import string


def generatePassword(length):
    password = ""

    randList = [lowerList, upperList, numList, specialList]

    randomList = random.choice(randList)
    randList.remove(randomList)
    password += random.choice(randomList)

    randomList = random.choice(randList)
    randList.remove(randomList)
    password += random.choice(randomList)

    randomList = random.choice(randList)
    randList.remove(randomList)
    password += random.choice(randomList)

    randomList = random.choice(randList)
    randList.remove(randomList)
    password += random.choice(randomList)
    

    for x in range(length - 4):
        randomNum = random.randint(1, 4)
        if (randomNum == 1):
            password += random.choice(lowerList)
        if (randomNum == 2):
            password += random.choice(upperList)
        if (randomNum == 3):
            password += random.choice(numList)
        if (randomNum == 4):
            password += random.choice(specialList)

    return password


lowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

specialList = ['!', '@', '#', '$', '&', '*', '-', '_', '=', '+', '?']

length = int(input("Enter password length (Must be >= 4): "))
while (length < 4):
    print("Please enter a valid length")
    length = int(input("Enter password length (Must be >= 4): "))

    
answer = 'Y'
print()

while (answer == 'Y' or answer == 'y'):
    
    print("Generated password: ", generatePassword(length))
    print("Generated password: ", generatePassword(length))
    print("Generated password: ", generatePassword(length))
    print("Generated password: ", generatePassword(length))
    print()


    answer = input("Would you like to generate more passwords? (Y/N): ")
    print()

