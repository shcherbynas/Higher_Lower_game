import random

def lowest_check():
    try:
        low = int(input("What is the lowest number of your list "))
        highest_check(low)
    except:
        print("Please write an integer")
        lowest_check()

def highest_check(low_ch):
    try:
        high = int(input("What is the highest number of your list "))
        while high < low_ch:
            print("The highest number has to be more than the lowest")
            high = int(input("What is the highest number of your list "))
        else:
            print("Let's get started")
    except:
        print("Please write an integer")
        highest_check(low_ch)




lowest_check()

