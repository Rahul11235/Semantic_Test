
Header=["Complaint Type","Counts"]
m=["Street Light Condition","28738"]
m1=["Damaged Tree","26500"]
m2=["Noise -Residential","25323",]
m3=["HEATING","2543"]
m4=["Blocked Driveway","20839"]
m5=["Street Condition","19401"]
m6=["Sewer","15907"]
m7=["Water System","14999"]
m8=["GENERAL CONSTUCTION","13327"]
m9=["Traffic Signal Condition","13191"]

import csv
with open("R1.csv","w") as fd:
    fd1=csv.writer(fd,delimiter=",")
    fd1.wrierow(Header)
    fd1.writerow(m)
    fd1.writerow(m1)
    fd1.writerow(m2)
    fd1.writerow(m3)
    fd1.writerow(m4)
    fd1.writerow(m5)
    fd1.writerow(m6)
    fd1.writerow(m7)
    fd1.writerow(m8)
    fd1.writerow(m9)


Header1=["Borough","Count"]
n=["BROOKLYN","11480"]
n1=["QUEENS","11480"]
n2=["MANHATTAN","11480"]
n3=["BRONX","11480"]
n4=["STATEN ISLAND","11480"]
import csv
with open("R2.csv","w") as fd2:
    fd3=csv.writer(fd2,delimiter=",")
    fd3.writerow(Header1)
    fd3.writerow(n)
    fd3.writerow(n1)
    fd3.writerow(n2)
    fd3.writerow(n3)
    fd3.writerow(n4)
