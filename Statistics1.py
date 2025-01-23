import numpy as np
import pandas as pd

values = np.array((1,2,3,4,5,6,7,8 ))

##
#print(np.mean(values))
#print(np.median(values))

Titanic = pd.read_csv("Titanic Dataset.csv")

MeanAge = np.mean(Titanic["Age"])
print(round (MeanAge))

MeanFare = np.mean(Titanic["Fare"])
print(round (MeanFare))