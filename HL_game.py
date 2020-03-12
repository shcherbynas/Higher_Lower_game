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
            print(secret)
            #return secret            
            entrance_check(high, low)
    except ValueError:
        print("Please write an integer")
        highest_check(low)

def entrance_check(high, low):
    try:
        user_number = int(input("Try to guess the 'secret' number "))
        while user_number > high or user_number < low:
            print ("Please write number between your highest and lowest numbers")
            user_number = int(input("Try to guess the 'secret' number "))
        else:
            print("ok")
    except:
        print("Please write an integer")
        entrance_check(high,low)
        

lowest_check()



