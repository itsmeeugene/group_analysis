import numpy as np
from random import random
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def create_hist(n):
    for j in range(n):
        for i in range(1000):
            generate_percentage = random()
            if generate_percentage <= true_percentage:
                data.append(True)
            else:
                data.append(False)
        real_percentage = sum(data) / len(data)
        real_data.append(real_percentage)
    return real_data


true_percentage = 0.05

data = []
real_data = []

x = np.array(create_hist(100))
y = np.array(create_hist(250))

plt.hist([x, y])
plt.show()

