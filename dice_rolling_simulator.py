"""
This is a program that simulates rolling dice.
When the program runs, it will randomly select a number
between 1 and 6 and print it out.
"""


from random import randint

def dice_simulator ():
    # This function randomly grabs a number between 1 and 6 and prints it.
    number = randint (1,6)
    print (number)

print ("Welcome to 'Dice Rolling Simulator'")

print ("\nLucky number is: ")
dice_simulator()

while True:
    answer = input ("\nDo you wanna try again? (yes/no): ")
    if answer.lower() == "yes":
        dice_simulator()
    elif answer.lower() == "no":
        print ("See you next time")
        break
    else:
        print ("\nWarning! You must select 'yes' or 'no'!")


