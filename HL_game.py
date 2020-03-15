import random


# setting up function that checks if user entered an integer as the lowest number of the list
def lowest_check():
    try:
        low = int(input("What is the lowest number of your list? "))
        highest_check(low)
    except:
        print("Please write an integer")
        lowest_check()


# setting up function that checks if user entered an integer as the highest number of the list
def highest_check(low):
    try:
        high = int(input("What is the highest number of your list? "))
        while high < low:
            print("The highest number has to be more than the lowest")
            high = int(input("What is the highest number of your list? "))
        else:
            print("Let's get started")
            secret = random.randint(low, high)
            # return secret
            entrance_check(high, low, secret)
    except ValueError:
        print("Please write an integer")
        highest_check(low)


# setting up function that checks if user wrote an integer as their guess and it's between the highest and the lowest
def entrance_check(high, low, secret):
    try:
        user_number = int(input("Try to guess the 'secret' number "))
        while user_number > high or user_number < low:
            print("Please write number between your highest and lowest numbers")
            user_number = int(input("Try to guess the 'secret' number "))
        else:
            winning_syst(secret, user_number)
    except:
        print("Please write an integer")
        entrance_check(high, low)

def winning_syst(secret, user_numb):
    while user_numb != secret:
        if user_numb > secret:
            print("Try again, the secret number is lower")
            user_numb = int(input("Try to guess the 'secret' number "))
        elif user_numb < secret:
            print("Try again, the secret number is higher")
            user_numb = int(input("Try to guess the 'secret' number "))
    else:
        print("Congratulations! You guessed the secret number")

lowest_check()
