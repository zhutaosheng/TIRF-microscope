# -*- coding: utf-8 -*-
#change by main_optimized python file
from pycromanager import Acquisition, multi_d_acquisition_events
import numpy as np
import math

edge_xy_1 = [100,200] #[initial Position X, initial Position Y]
edge_xy_2 = [200,300] #[final Position X, final Position Y]

length_x_move = 20 # distance move to x // in um
length_y_move = 20 # distance move to y // in um

length_x = edge_xy_2[0]-edge_xy_1[0]
length_y = edge_xy_2[1]-edge_xy_1[1]

num_samples_x = length_x/length_x_move
num_samples_y = length_y/length_y_move
num_samples_x = math.floor(abs(num_samples_x)) # with round() function
num_samples_y = math.floor((num_samples_y))

x = np.linspace(edge_xy_1[0],edge_xy_2[0],num =num_samples_x)
y = np.linspace(edge_xy_1[1],edge_xy_2[1],num =num_samples_y)
y_reverse = y[::-1]
x_reverse = y[::-1]

# generate grid2points
xy = []

direction = True
# default: direction move along with the y

if direction:
    for i in range(len(x)):
        for j in range(len(y)):
            if (i % 2) == 0:
                xy.append([x[i],y[j]])
            else:
                xy.append([x[i],y_reverse[j]])
    xy = np.array(xy)
else:
    for j in range(len(x)):
        for i in range(len(y)):
            if (j % 2) == 0:
                xy.append([x[i],y[j]])
            else:
                xy.append([x_reverse[i],y[j]])
    xy = np.array(xy)


print(xy)
print(len(xy)) #toknow how many points we get

directory=r'D:/Zhutao'
name='new-data'
order='tp' # order='pt' # p,t mean position, time
time_interval_s = 10


