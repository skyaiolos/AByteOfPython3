#!/usr/bin/python
# Filename: if.py and while, and try - except

number = 23

while True:
    try:
        guess = int(input('Enter an integer : '))  # convert strings to a integer

        if guess == number:
            print('Congratulations, you guessed it.')  # New block starts here
            print('(but you do not win any prizes!)')  # New block ends here

            break
        elif guess < number:
            print('No, it is a little higher than that')  # Another block
            # You can do whatever you want in a block ...
        else:
            print('No, it is a little lower than that')
            # you must have guess > number to reach here
    except ValueError:
        print("pls input integer")

# This last statement is always executed, after the if statement is executed
