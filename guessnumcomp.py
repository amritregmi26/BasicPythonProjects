import random

def guess(x):
    random_number = random.randint(1,x)
    # It will generate a random number between 1 and 10.

    num = 0
    while num != random_number:
        num = int(input(f"Enter any number between 1 and {x}: "))
        if num < random_number:
            print("The number is too low.")

        elif num > random_number:
            print("The number is too high.")
    # Until the random number is equal to user input, the while loop will keep on executing.

    print(f"Congrats! You guessed the random number {random_number} correctly.")

guess(10)