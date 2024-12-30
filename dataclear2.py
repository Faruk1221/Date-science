import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


#countryData= pd.read_csv("country_vaccinations.csv")
#VaccineDF = pd.DataFrame(countryData)
#plt.figure(figsize=(8,5))
#sb.heatmap(VaccineDF.isnull(),cbar=False)
#print(VaccineDF.dropna(how="all"))
#VaccineDF.fillna(0)

EmpDS ={
'name': ["Adib", "Adib", "Rahul"],
'ID': [000,000,110]
}

EmpDF = pd.DataFrame (EmpDS)
EmpDF.drop_duplicates()
print (EmpDF)