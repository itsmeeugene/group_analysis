from math import exp, pi, sqrt
import numpy as np
from random import random
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as ss


def create_disp(real_data):
    data = real_data[:]
    true_percentage = sum(data) / len(data)
    for i in range(len(data)):
        data[i] = (data[i] - true_percentage) ** 2
    return sum(data) / len(data)


def create_hist(people, experiments=5000):
    real_data = []
    for j in range(experiments):
        data = []
        for i in range(people):
            generate_percentage = random()
            if generate_percentage <= very_true_percentage:
                data.append(True)
            else:
                data.append(False)
        real_percentage = sum(data) / len(data)
        real_data.append(real_percentage)
    dispersion = create_disp(real_data)
    return real_data, dispersion


very_true_percentage = 0.05

# ks = []
# selections = []
# disp_list = []
# ppl = 100
#
# for i in range(10):
#     disp_list.append(create_hist(ppl)[1])
#     selections.append(ppl)
#     ppl += 100
#     ks.append(selections[-1] * disp_list[-1])
#
# k = sum(ks) / len(ks)
# y = [k / i for i in range(100, 1001, 50)]
# x = [i for i in range(100, 1001, 50)]
#
# plt.plot(x, y, color='r')
# plt.plot(selections, disp_list, color='b')


real_data, sigma = create_hist(200)
mu = sum(real_data) / len(real_data)
# plt.hist(real_data, density=True, bins=25)

summ = 0
step = 1/12
i = very_true_percentage
# y = [exp((-1 * (i - mu) ** 2) / (2 * sigma)) / sqrt(2 * pi * sigma) for i in np.linspace(0, 0.1)]
# x = [i for i in np.linspace(0, 0.1)]
# plt.plot(x, y)
while summ <= 0.475:
    y1 = exp((-1 * (i - mu) ** 2) / (2 * sigma)) / sqrt(2 * pi * sigma)
    y2 = exp((-1 * (i + step - mu) ** 2) / (2 * sigma)) / sqrt(2 * pi * sigma)
    summ += step * (y1 + y2) / 2
    i += step
print(i)

# plt.show()


