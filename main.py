import numpy as np
from random import random
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def create_hist(n):
    real_data = []
    for j in range(200):
        data = []
        for i in range(n):
            generate_percentage = random()
            if generate_percentage <= true_percentage:
                data.append(True)
            else:
                data.append(False)
        real_percentage = sum(data) / len(data)
        real_data.append(real_percentage)
    return real_data


true_percentage = 0.05
selec1, selec2, selec3 = 100, 1000, 100000

x = np.array(create_hist(100))
y = np.array(create_hist(1000))
z = np.array(create_hist(10000))
plt.hist([x, y, z], color=['r', 'g', 'b'], label=[selec1, selec2, selec3])
plt.legend(loc='upper right')

plt.show()

