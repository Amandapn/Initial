import numpy as np
import matplotlib.pyplot as plt

fr = open("PLAtrain.txt", 'r+')  # Read data points from file
data = eval(fr.read())  # Convert a string to a numeric value
fr.close()  # Close file
w0 = np.random.randint(10, size=3)  # Initialize the value of w in the PLA algorithm randomly
w = w0  # Assign the initialized value to w
flag = 1  # Flag is used to determine if there is a point with a classification error
while flag == 1:  # When the flag is equal to 1, it indicates that there is at least one point with a classification
    # error, and it is necessary to calculate the value of w to reclassify
    plt.figure()  # Create  figure
    for item, value in data.items():  # Traversing data points and labels in the dict
        # print(item,value)              # Output data points and labels
        if value == '+':
            plt.plot(item[0], item[1], marker='o', color='b')  # If the label of the data point is +, draw it as follows
        else:
            plt.plot(item[0], item[1], marker='x', color='r')  # If the label of the data point is -, draw it as follows
    plt.title('data with different labels')  # Display the title of the figure
    plt.xlabel('x1')  # Mark the abscissa of the figure x1
    plt.ylabel('x2')  # Mark the ordinate of the figure x2
    plt.xlim(-25, 25)  # Set the display range of the abscissa
    plt.ylim(-25, 25)  # Set the display range of the ordinate
    for item, value in data.items():  # Traversing data points and labels in the list
        if value == '+':  # In the case where the data point label is +
            if w[1] * item[0] + w[2] * item[1] + w[0] < 0:  # If the point is misclassified
                w = [w[0] + 1, w[1] + item[0], w[2] + item[1]]  # Change the value of w
                flag = 1  # Flag remains at 1
                print(w)
                break  # Jump out of the loop，re-traversing data points and labels
            else:  # If the point is correctly classified, the flag is 0
                flag = 0

        else:  # Similarly，in the case where the data point label is -
            if w[1] * item[0] + w[2] * item[1] + w[0] > 0:  # If the point is misclassified
                w = [w[0] - 1, w[1] - item[0], w[2] - item[1]]  # Change the value of w
                print(w)
                flag = 1  # Flag remains at 1
                break  # Jump out of the loop，re-traversing data points and labels
            else:
                flag = 0  # If the point is correctly classified, the flag is 0
    x = np.arange(-20, 20, 1)  # Define the range of x to draw the classification line
    y1 = (-w[1] / w[2]) * x - (w[0] / w[2])  # Define the ordinate of the classification line as y
    plt.plot(x, y1, 'k')  # Draw the line
    y2 = (-2 / 3) * x - (5 / 3)
    plt.plot(x, y2, 'g')
    plt.show()  # Display figure
