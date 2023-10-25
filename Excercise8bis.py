##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random
import matplotlib.pyplot as plt


def roll_two_dice():

    die1= random.randint(1,6)
    die2= random.randint(1,6)
    total = die1+die2
    return total

def main():

    result = []
    num_exec = 100

    for i in range(num_exec):
        result.append(roll_two_dice())


    # Create plot 
    plt.hist(result, bins=range(2, 14), align='left')

    #Add labels and title
    plt.xlabel('Amount of values')
    plt.ylabel('Frecuency')
    plt.tittle('Rolling two dice'+str(num_exec))

    plt.show()
    print('hola')

if __name__ == "__main__":
        main()