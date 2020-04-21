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


# setting up winning system that checks if user guessed the secret number.
# if user didn't guess secret number then program tells him whether the secret number is higher or lower until they run out of guesses
def winning_syst(secret_n, user_numb, guesses_allow):
    guesses = 0
    while user_numb != secret_n and guesses < guesses_allowed:

        if user_numb in already_guessed:
            print("You already guessed this number")
            guesses -= 1

        guesses += 1
        already_guessed.append(user_numb)

        if guesses < guesses_allow:
            if user_numb > secret_n:
                print("Try again, the secret number is lower")
                print("You have {} guesses left".format(guesses_allow - guesses))
                print()
                user_numb = int_check("Try to guess the 'secret' number ", lowest, highest)
                print()

            elif user_numb < secret_n:
                print("Try again, the secret number is higher")
                print("You have {} guesses left".format(guesses_allow - guesses))
                print()
                user_numb = int_check("Try to guess the 'secret' number ", lowest, highest)
                print()
        else:
            print("Sorry, you ran out of guesses")
            print("The secret number was " + str(secret_n))
    if user_numb == secret_n:
        print("Congratulations! You guessed the secret number")
       # keep_going = input("Press <enter> to continue or any other key to quit")
       # return keep_going


keep_goin = ""
while keep_goin == "":
    # creating an empty list to prevent user to guess same number several times
    already_guessed = []
    # initializing variables
    guesses_allowed = int_check("How many guesses do you want to have? ", 1)
    lowest = int_check("What is the lowest number of your list? ")
    highest = int_check("What is the highest number of your list? ", lowest+1)

    # randomly generates secret number
    secret = random.randint(lowest, highest)
    print(secret)
    user_number = int_check("Try to guess the 'secret' number ", lowest, highest)
    print()

    winning_syst(secret, user_number, guesses_allowed)
    keep_goin = input("Press <enter> to continue or ay other key to quit")
else:
    print("Thank you for playing")