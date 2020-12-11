import numpy as np
from random import random
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def create_disp(real_data):
    data = real_data[:]
    true_percentage = sum(data) / len(data)
    for i in range(len(data)):
        data[i] = (data[i] - true_percentage) ** 2
    return sum(data) / len(data)


def create_hist(experiments, people):
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
hist, disp = create_hist(200, 100)


