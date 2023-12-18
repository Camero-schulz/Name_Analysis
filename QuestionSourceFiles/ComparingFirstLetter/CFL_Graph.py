#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os
#-get install python3-tk

# Define X and Y variable data
def create(data, charInput, gender):

    names = []
    total = []
    for i in range (7):
      names.append(data[i][0])
      total.append(data[i][1])

    x = np.array(names)
    y = np.array(total)

    plt.clf()  # Clear the current figure and axes
    plt.bar(x, y)

    plt.xlabel("Names") 
    plt.ylabel("Total")
    plt.title("Most popular {0} names starting with {1}".format(gender, charInput))
    plt.savefig('../CFL{0}.png'.format(gender))
    plt.show()
