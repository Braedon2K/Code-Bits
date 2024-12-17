import random

num1 = 11
num2 = 14
num3 = 23
num4 = 27
num5 = 37

attempt = 1

while True:

    lotto1 = random.randint(1, 43)
    lotto2 = random.randint(1, 43)
    if(lotto2 == lotto1):
        lotto2 = random.randint(1,43)
    lotto3 = random.randint(1, 43)
    if(lotto3 == lotto2 or lotto3 == lotto1):
        lotto3 = random.randint(1, 43)
    lotto4 = random.randint(1, 43)
    if(lotto4 == lotto3 or lotto4 == lotto2 or lotto4 == lotto1):
        lotto4 = random.randint(1, 43)
    lotto5 = random.randint(1, 43)
    if(lotto5 == lotto4 or lotto5 == lotto3 or lotto5 == lotto2 or lotto5 == lotto1):
        lotto5 = random.randint(1, 43)

    print("Attempt: ", attempt)
    print("My Numbers: ", num1, num2, num3, num4, num5)
    print("Lotto Numbers: ", lotto1, lotto2, lotto3, lotto4, lotto5)
    print()

    if(num1 == lotto1 or num1 == lotto2 or num1 == lotto3 or num1 == lotto4 or num1 == lotto5):
        if(num2 == lotto1 or num2 == lotto2 or num2 == lotto3 or num2 == lotto4 or num2 == lotto5):
            if(num3 == lotto1 or num3 == lotto2 or num3 == lotto3 or num3 == lotto4 or num3 == lotto5):
                if(num4 == lotto1 or num4 == lotto2 or num4 == lotto3 or num4 == lotto4 or num4 == lotto5):
                   if(num5 == lotto1 or num5 == lotto2 or num5 == lotto3 or num5 == lotto4 or num5 == lotto5):
                      print("You won!")

    attempt = attempt + 1

    
