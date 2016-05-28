import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open("datasetemaple.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    assert isinstance(plots, object)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('HOLD THE DOOR\nHold the Door')
plt.legend
plt.show()