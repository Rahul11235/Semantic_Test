
import pandas as pd
import numpy as np
d=pd.read_csv("E:/data_2010.csv",usecols=[0,1,5,24])
x=d["Complaint Type"]!=0
y=d["Borough"]=="QUEENS"
D=d[x & y]
c=D["Complaint Type"].value_counts()
z=c[:10]
print(max(c))
""""
Which borough has most complaints for your given
complaint type

"""
import pandas as pd
import numpy as np
data=pd.read_csv("E:/Ranjeet_2010_Data.csv",usecols=[0,1,5,24])
MM=data["Borough"].value_counts()
print(max(MM))
