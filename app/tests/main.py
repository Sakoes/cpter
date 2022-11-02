from re import A
from turtle import distance
import numpy as np
import dtw
import matplotlib.pyplot as plt


input_X = [1,2,3,4,5]
input_y = [1,2,3,4,5]

idx = np.linspace(0,6.28,num=100)
query = np.sin(idx) + np.random.uniform(size=100)/10.0

reference = np.cos(idx)

#alignment = dtw.dtw(query,reference)

alignment = dtw.dtw(input_X, input_y)
print(getattr(alignment,"distance"))

print("stop") 

