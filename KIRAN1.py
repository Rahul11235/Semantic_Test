import pandas as pd
import numpy as np
x=pd.read_csv("E:\Kiran.csv",usecols=[0,1,5,24])
x[:5]
x[:5]['Complaint Type']
D= x['Complaint Type'] !=0
E=x['Borough']=="QUEENS"
y= x[D & E]
QUEEN=y["Complaint Type"].value_counts()
count=QUEEN[:10]
print(count)
