

import random

min_val = 1  #minimun value of dices
max_val = 6  #maximum value of the dices

roll_again = "yes"  # the variable that stores the user’s decision

while roll_again == "yes" or roll_again == "y": # while loop is use for user wants to roll the dices again and again
    print("Dices rolling... " )
    print("The vlues are : " )
    print(random.randint(min_val, max_val))  # Printing the randomly generated variable of the first dice
    print(random.randint(min_val, max_val))  # Printing the randomly generated variable of the second dice
    roll_again = input("Roll the Dices Again?") # Here the user enters yes or y to continue and any other input ends the program

