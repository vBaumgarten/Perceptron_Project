# Program designed as a perceptron for a senior-year (undergraduate) research project.
#
# Description: The system, in training mode, randomly generates a set of weights and adjusts those weights using the set of inputs with various
# training cycles until an ideal tolerance is found. After which, the testing phase is used to test the system
# in a variety of scenarios.
# 
# By: Vincent Baumgarten
# Date of Completion: 
# 

import numpy as np
import sys, os, random
from math import *

bias = random.random()

weights = open("weight.txt", "w+") #opening the weights file for writing purposes
ifile = open("input.txt", "r") #opening the input file for reading purposes

input_data = ifile.readlines()
for line in input_data:
    for i in line.split():
        rnum = str(random.random())
        weights.write(rnum + ' ')
        weights.flush()
        
weights.close()

x = np.array([]) #establishment of the input array
w = np.array([]) #establishment of the weight array

for line in input_data:
    train_input = line.split()
    x = np.append(x, train_input)

weights = open("weight.txt", "r")

weight_data = weights.readlines()
for new_line in weight_data:
    train_weight = new_line.split()
    w = np.append(w, train_weight)

weights.close()              

training_flag = 1 #training mode initialized

print("Welcome to the Perceptron CLI! Please enter the number of the mode you wish to use.")
print()
print("(1) Training Mode: Trains the perceptron using pre-programmed activation function and weight and bias change formulas.")
print("(2) Testing Mode: Runs a forward propogation of the system to provide a predicted value using pre-programmed settings.")
print("(999) Exit: Exits the program.")
print()

while True: #used to control continuous training and testing
    user_input = input(">>> ")

    
    if user_input == '1':
        count = 0
        tol = float(input("Input your tolerance (in decimal form; e.g. 0.01): "))
        actual_val = int(input("Please input the value of the actual answer: "))
        while training_flag == 1: #while in training mode

            count += 1
            
            print("Tol:" + str(tol))
            
            inner_product = 0
            for i in range(x.size):
                inner_product += int(x[i])*float(w[i])
            z = inner_product + bias #value used in calculating the predicted value
            predicted_val = 1/(1+exp(z*-1))

            change_bias_weight = -1*((2/x.size)*(actual_val - predicted_val)*predicted_val*(1 - predicted_val))
            
            print("Predicted value: " + str(round(predicted_val)))

            print("Change in weight/bias: " + str(change_bias_weight))

            learning_rate = 1.01
            w[0] = float(w[0]) - (learning_rate*change_bias_weight)
            w[1] = float(w[1]) - (learning_rate*change_bias_weight)
            bias = float(bias) - (learning_rate*change_bias_weight)

            print()
            
            if actual_val == predicted_val or abs(actual_val - predicted_val) < tol:
                training_flag = 0

            weights = open('weight.txt', 'w+')
        
            for i in range(x.size):
                weights.write(w[i] + ' ')
                weights.flush()

            os.system('cls')

            print("Round " + str(count) + " has been completed.")
            
    elif user_input == '2':
        inner_product = 0
        for i in range(len(x)):
            inner_product += int(x[i])*float(w[i])
        z = inner_product + bias #value used in calculating the predicted value
        predicted_val = 1/(1+exp(z*-1))
        
        print("Predicted value: " + str(round(predicted_val)))
        print()

    elif user_input == "999":
        weights.close()
        ifile.close()
        sys.exit()

    else:
        print("Your input was not recognized. Try again.")
        print()


