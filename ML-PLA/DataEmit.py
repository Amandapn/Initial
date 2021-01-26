import numpy as np
import random
import itertools

w = input("w:")  # input vector w to generate data points
w = eval(w)  # convert a string to an array
m = input("m:")  # get the number of points with label +
m = int(m)  # convert a string to an integer
n = input("n:")  # get the number of points with label -
n = int(n)  # convert a string to an integer


# Define the function DataEmit1 to generate data with labels
def DataEmit1(w, m, n):  # Input parameters
    data1 = {}  # Define a dict to store data points and corresponding labels
    data2 = {}
    data3 = {}
    random_S = list(itertools.product(range(-20, 20), range(-20, 20)))  # Generate random data points ranging
    # from -20 to 20 (integer values, range can be changed)
    # random_S_list=random.sample(random_S,3*S)                            # Select S data points from the generated
    # random data points
    for i in random_S:
        []#  Make a judgment and give the corresponding label to the data point
        if w[1] * i[0] + w[2] * i[1] + w[0] < 0:
            data1[i] = '-'
        else:
            data2[i] = '+'  # If the above conditions are not met, the opposite label is give
    data = random.sample(list(data1.items()), n) + random.sample(list(data2.items()), m)  # Randomly select data
    return data  # Return a list of data points and corresponding labels


data = DataEmit1(w, m, n)  # Call the function once after entering the parameters to get the data set and label
data = dict(data)  # Convert a list to a dictionary
print(data)  # Display data set and labels
fw = open("PLAtrain.txt", 'w')  # Open the train.txt file in write mode. If there is no such file, create one
fw.write(str(data))  # Save data points and labels in a file as a string
fw.close()
