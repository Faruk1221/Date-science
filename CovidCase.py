import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
CovidDF = pd.read_csv(url)


country = "India"
CovidDF_India = [CovidDF["location"]==country]

CovidDF_India = CovidDF_India[["date","new_cases","new_deaths","new_recovaries"]]
CovidDF_India["date"] =pd.to_datetime(CovidDF_India["date"])

plt.figure(figsize=(8,6))
plt.plot(CovidDF_India["date"],CovidDF_India["new_cases"],label="New Cases",color="blue")
plt.plot(CovidDF_India["date"],CovidDF_India["new_deaths"],label="New Deaths",color="red")
plt.plot(CovidDF_India["date"],CovidDF_India["new_recovaries"],label="New Recovaries",color="green")

plt.title("Covid Case Analysis")
plt.xlabel("date")
plt.ylabel("Count")
plt.grid(True)
plt.legend()
plt.show()
