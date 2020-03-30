import random


# setting a function that checks if user wrote an integer
def int_check(question, low=None, high=None):
    global error
    if low is not None and high is not None:
        error = ("Please write an integer between {} and {}"
                "(inclusive)".format(low, high))
    elif low is not None and high is None:
        error = ("Please write an integer more than "
                 + str(low-1))
    elif low is None and high is None:
        error = ("Please write an integer")

    while True:
        try:
            response = int(input(question))
            if low is not None and response < low:
                print(error)
                continue
            elif high is not None and response > high:
                print(error)
                continue
            return response
        except ValueError:
            print(error)
            continue


# setting up winning system that checks user guessed the secret number.
# if user didn't guess secret number then program tells him whether the secret number is higher or lower
def winning_syst(secret_n, user_numb, guesses_allow):
    guesses = 0
    while user_numb != secret_n and guesses < guesses_allowed:
        guesses += 1

        if guesses < guesses_allow:
            if user_numb > secret_n:
                print("Try again, the secret number is lower")
                user_numb = int_check("Try to guess the 'secret' number ", lowest, highest)

            elif user_numb < secret_n:
                print("Try again, the secret number is higher")
                user_numb = int_check("Try to guess the 'secret' number ", lowest, highest)
        else:
            print("Sorry, you ran out of guesses")
            print("The secret number was " + str(secret_n))
    if user_numb == secret_n:
        print("Congratulations! You guessed the secret number")


guesses_allowed = int_check("How many guesses do you want to have? ", 1)
lowest = int_check("What is the lowest number of your list? ")
highest = int_check("What is the highest number of your list? ", lowest+1)

secret = random.randint(lowest, highest)
print(secret)

user_number = int_check("Try to guess the 'secret' number ", lowest, highest)


winning_syst(secret, user_number, guesses_allowed)
