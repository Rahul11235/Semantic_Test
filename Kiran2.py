import pandas as pd
import numpy as np
x=pd.read_csv("E:\Kiran_2013.csv",usecols=[0,1,5,24])
x[:5]
Borough = x["Borough"].value_counts()
print(Borough)
import matplotlib
from matplotlib import pyplot
Borough.plot(kind="pie")
#<matplotlib.axes._subplots.AxesSubplot object at 0x000001A42F456A20>
pyplot.show()
