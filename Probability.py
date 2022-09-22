#Program that produces a graph demonstrating the probability of 
#X number of rolls on Y-sided dice or
#Z number of coin flips

import matplotlib.pyplot as plot
import scipy.special

choice = input("Roll dice (D) or flip coins (C) ?") #Input check
while (choice.upper() != 'D' and choice.upper() != 'C'):
    choice = input("Roll dice (D) or flip coins (C) ?")

if (choice.upper() == 'D'):
    sides_input = input("How many sides on the dice?")
    while(sides_input.isnumeric() == False):
        sides_input = input("How many sides on the dice?")
    rolls_input = input("How many rolls of the dice?")
    while(rolls_input.isnumeric() == False):
        rolls_input = input("How many rolls of the dice?")

    sides = int(sides_input)
    rolls = int(rolls_input) #Cast inputs as integers

    probabilites = [] #Holds odds
    outcomes = pow(sides,rolls) #Total number of possible outcomes 

    max_possible = (rolls * sides) #highest possible roll

    for iter,roll in enumerate(range(1,max_possible+1)):

        acceptable = scipy.special.binom(max_possible, iter) #Acceptable number of rolls to equal value iter
        value = acceptable/outcomes #Number of valid rolls over total possible rolls

        probabilites.append(value) #Add to the array and loop
    
    norm = [float(i)/sum(probabilites) for i in probabilites] #Normalize the array inbetween 0 and 1 to get a percentage

    x_values = list(range(1,max_possible+1)) #Add the X-Values (0,1,2,3,etc.)

    plot.bar(x_values, norm) #Graph everything
    plot.title(f"Chances of every possible total outcome when rolling {sides} sided dice {rolls} time(s)")
    plot.show()

elif(choice.upper() == 'C'):
    flips_input = input("How many flips?")
    while(flips_input.isnumeric() == False):
        flips_input = input("How many flips?")
    
    flips = int(flips_input)
    probabilites = []
    outcomes = pow(2,flips) #Possible outcomes is equal to 2 to the number of flips

    for iter,flip in enumerate(range(0,flips)):

        acceptable = scipy.special.binom(flips,iter) #Possible combinations of flips to equal the acceptable number of heads (iter)

        value = acceptable/outcomes #Possible combinations over total combinations = percent chance
        probabilites.append(value) #Add it to the array and loop
    
    x_values = list(range(0,flips)) #Set X Values

    plot.bar(x_values, probabilites) #Graph everything
    plot.title(f"Chances of flipping heads X times")
    plot.show()
    
