import numpy as np
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt

employeedata = {
    "ID":[1,2,3,4,5,6,6],
    "Name":["pallab","omor",np.nan,"rahul","nime",np.nan,"lamin"],
    "Age":[20,np.nan,50,24,34,18,90],
    "Salary":["2222","400","NA","2000","3000","3444","444"]

}
empDF = pd.DataFrame(employeedata)
print("orignal dataFrame")

empDF["Name"]= empDF["Name"].fillna("Unknown")

avg_age = empDF['Age'].mean()
empDF['Age'] = empDF["Age"].fillna(avg_age)

empDF('Age') = abs(empDF["Age"])

empDF["salary"] = pd.to_numeric(empDF["salary"])
empDF['salary']=np.nan_to_num(empDF["salary"])
avg_salary =empDF["salary"].mean()
empDF['salary']= empDF["salary"].fillna(avg_salary)
print(empDF)