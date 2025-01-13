import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

Blood_Sugar_Men =[120,110,135, 125, 111, 112, 115, 111,135,125,111,112] #12 Value
Blood_Sugar_Women =[90,95,98, 100, 105,78,88,90,80,99,100,110]

type =[Blood_Sugar_Men, Blood_Sugar_Women]
color=['r','g']
label= ["Men", "Women"]
bins =[70,80,90, 100, 110, 120, 130, 140, 150]

plt.xlabel("Blood Sugar Range")
plt.ylabel("total Number of Patient")
plt.hist(type,bins=bins,color=color,rwidth=0.95,label=label)
plt.title("mone nai")
plt.show()