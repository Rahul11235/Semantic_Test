import pandas as pd

Data1=pd.read_csv("E:\Whole_Data2012.csv",usecols=[0,1,5,24])
print(Data1[:5])


a = Data1['Complaint Type'] !=0
b = Data1['Borough'] == "QUEENS"
Data2=Data1[a & b]
Count=Data2["Complaint Type"].value_counts()
c=(Count[:10])
print(c)
  

X = Data1['Complaint Type'] == "Illegal Parking"
y = Data1[X]
z=y['Borough'].value_counts()
print(z)

import matplotlib
from matplotlib import pyplot

c.plot(kind="bar")
pyplot.show()     

z.plot(kind="bar")
pyplot.show()       
    
        
