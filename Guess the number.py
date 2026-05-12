


import random

secret = random.randint(1, 100)
secret=85

guess = 0

while guess != secret:

    try:
        guess = int(input("Guess the number (1-100): "))

        if guess == secret:
            print("You won!")

        elif guess < secret:
            print("Too low!")

        else:
            print("Too high!")

    except:
        print("Please enter a valid number!")
