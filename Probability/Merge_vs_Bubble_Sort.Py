#Sample program to demonstrate how merge sort runtime compares to bubble sort runtime

from ast import main
import time
import random

#Function for merge sort
def mergeSort(numbers):
    if len(numbers) > 1:                #If there is more than 1 number to sort

        midpoint = len(numbers)//2      #The middle of the array of numbers
        left = numbers[:midpoint]       #Left side of the array
        right = numbers[midpoint:]      #Right side of the array

        #Split the array into left and right halves
        mergeSort(left)
        mergeSort(right)

        left_iter = 0
        right_iter = 0
        main_iter = 0

        #After splitting the array, iterate through the values &
        #Place them in order into the numbers / main array

        while left_iter < len(left) and right_iter < len(right):

            if left[left_iter] < right[right_iter]:
                numbers[main_iter] = left[left_iter]
                left_iter += 1
            else:
                numbers[main_iter] = right[right_iter]
                right_iter += 1

            main_iter += 1

        #In case of any extra left or right values due to uneven splits
        while left_iter < len(left):
            numbers[main_iter] = left[left_iter]
            left_iter += 1
            main_iter += 1

        while right_iter < len(right):
            numbers[main_iter] = right[right_iter]
            right_iter += 1
            main_iter += 1

#Function for bubble sort
def bubbleSort(numbers):

    for i in range(len(numbers)):                   #Loop through the array once per value in the array
    
        for j in range(0, len(numbers) - i - 1):    #Loop through every value except the last one

            if numbers[j] > numbers[j + 1]:         #Compare and swap the numbers if the next is greater
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

#Main Program
if __name__ == '__main__':
    print('')
    numbers = input("Enter the values of your array (seperated by spaces) OR enter RANDOM for a random set of integers: ") 

    #Generates a random set of numbers
    if (numbers.upper() == "RANDOM"):
        random_values = input("Enter the number of random variables to sort: ")
        if (random_values.isnumeric() == False):
                print("Please only enter numeric values, Re-Run the program and try again.")
                exit()
        random_values = int(random_values)
        numbers_list = random.sample(range(0, random_values), random_values)

    else:    
        numbers_list = numbers.split()
        
        #Checks through each value to ensure only numbers are entered
        for value in numbers_list: 
            if(value.isnumeric() == False):
                print("Please only enter numeric values, Re-Run the program and try again.")
                exit()

        numbers_list = [int(x) for x in numbers_list] #Cast everything as an integer

    #print("List before the sort: ", numbers_list,'\n') #When using larger sets, you'll want to comment this

    merge_array = numbers_list
    bubble_array = numbers_list

    #Merge Sort call & time
    merge_start = time.time()
    mergeSort(merge_array)
    merge_end = time.time()

    merge_time = merge_end - merge_start

    #print("The merge sorted array: ", merge_array) #When using larger sets, you'll want to comment this
    print("Merge sort took ", merge_time, "seconds" ,'\n')

    #Bubble Sort call & time
    bubble_start = time.time()
    bubbleSort(bubble_array)
    bubble_end = time.time()

    bubble_time = bubble_end - bubble_start

    #print("The bubble sorted array: ", bubble_array) #When using larger sets, you'll want to comment this
    print("Bubble sort took ", bubble_time, "seconds", '\n')
