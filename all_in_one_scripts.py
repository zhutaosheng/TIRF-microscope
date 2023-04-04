# -*- coding: utf-8 -*-
#change by main_optimized python file
from pycromanager import Acquisition, multi_d_acquisition_events
import numpy as np

edge_xy_1 = [2362.00,-2476.40] #[initial_x, initial_y]
edge_xy_2 = [2904,-3526.18] #[final_x, final_y]

length_x_move = 200 # how um move for x
length_y_move = 200 # how um move for y

num_samples_x = (edge_xy_2[0]-edge_xy_1[0])/length_x_move
num_samples_y = (edge_xy_2[1]-edge_xy_1[1])/length_y_move
num_samples_x = round(abs(num_samples_x)) # with round() function, approximately, but accurately.
num_samples_y = round(abs(num_samples_y))

#num_samples_x = 3
#num_samples_y = 3

x = np.linspace(edge_xy_1[0],edge_xy_2[0],num =num_samples_x)
y = np.linspace(edge_xy_1[1],edge_xy_2[1],num =num_samples_y)
y_reverse=y[::-1]
xy=[]

for i in range(len(x)):
    for j in range(len(y)):
        if (i % 2) == 0:
            xy.append([x[i],y[j]])
        else:
            xy.append([x[i],y_reverse[j]])
xy = np.array(xy)

print(len(xy)) #for know how many points we get

directory=r'D:/Zhutao'
name='newdata'
order='tp' # order='pt' # p,t mean position, time
time_interval_s = 10
with Acquisition(directory=directory,
                 name=name,
                 ) as acq:
    events = multi_d_acquisition_events(num_time_points=1,time_interval_s=time_interval_s, xy_positions=xy,order=order)
    acq.acquire(events)



'''
# xy generate part

edge_xy_1 = [1000,-4000] #[initial_x, initial_y]
edge_xy_2 = [10000,5000] #[final_x, final_y]

length_x_move = 1000 # how um move for x
length_y_move = 1000 # how um move for y

num_samples_x = (edge_xy_2[0]-edge_xy_1[0])/length_x_move
num_samples_y = (edge_xy_2[1]-edge_xy_1[1])/length_y_move
num_samples_x = round(abs(num_samples_x)) # with round() function, approximately, but accurately.
num_samples_y = round(abs(num_samples_y))

#num_samples_x = 3
#num_samples_y = 3

x = np.linspace(edge_xy_1[0],edge_xy_2[0],num =num_samples_x)
y = np.linspace(edge_xy_1[1],edge_xy_2[1],num =num_samples_y)
y_reverse=y[::-1]
xy=[]


sample data: 9*9 data on the really microscope
x = [4000,4500,5000]
y = [-1000,-500,-0]
y_reverse=y[::-1]
xy=[]    

sample data: 10*10 array data
x = np.linspace(0,10.,10//1+1)
y = np.linspace(0,10.,10//1+1)
y_reverse=y[::-1]
xy=[]

'''



'''
# multi_d_acquisition_events parts

for i in range(len(x)):
    for j in range(len(y)):
        if (i % 2) == 0:
            xy.append([x[i],y[j]])
        else:
            xy.append([x[i],y_reverse[j]])
xy = np.array(xy)


directory=r'D:/Zhutao'
name='acquisition_name1'
order='tp' # order='pt' # p,t mean position, time
with Acquisition(directory=directory,
                 name=name,
                 ) as acq:
    events = multi_d_acquisition_events(num_time_points=1,
                                        time_interval_s=0,
                                        xy_positions=xy,
                                        order=order,
                                        )
    acq.acquire(events)









'''  
'''

https://pycro-manager.readthedocs.io/en/latest/apis.html#acq-event-spec

default papameters
num_time_points=1,
time_interval_s=0,
xy_positions=xy,
order='tp',

  
#default multi_d_acquisition_events parameters

num_time_points: int=None
time_interval_s: float=0
z_start: float=None
z_end: float=None
z_step: float=None
channel_group: str=None
channels: list=None
channel_exposures_ms: list=None
xy_positions=None
xyz_positions=None
order: str="tpcz",
keep_shutter_open_between_channels: bool=False
keep_shutter_open_between_z_steps: bool=False

#default Acquisition parameters

directory: str=None
name: str=None
image_process_fn : callable=None
event_generation_hook_fn: callable=None
pre_hardware_hook_fn: callable=None
post_hardware_hook_fn: callable=None
post_camera_hook_fn: callable=None
show_display: bool or str=True
image_saved_fn: callable=None
process: bool=False
saving_queue_size: int=20
timeout: int=500
debug: int=False
core_log_debug: int=False
'''