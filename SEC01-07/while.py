# !/usr/bin/python
# Filename while.py

number = 23
# running = True
# while running:
while True:
    try:
        guess = int(input("Enter an integer:"))
        if guess == number:
            print("Congratulation, you guessed it.")
            # running = False  # this causes the while loop to stop
            break
        elif guess < number:
            print("It is greater than your input ,please guess again !")
        else:
            print("It is less than your input, please guess again !")
    except ValueError:
        print("pls input integer")
else:
    print("the while is over.")
print("Game Over !")
