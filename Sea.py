import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

IceCreamData = {

"Flavor":["chocolate","vanila","strawberry","mint"],
"votes":[40,20,30,10]
}
IceCreamDF = pd.DataFrame(IceCreamData)

#Barplot


plt.figure(figsize=(8,5))
sb.barplot(x="Flavor", y="votes", data=IceCreamDF, palette="pastel")
plt.xlabel("Flavor")
plt.ylabel("Votes")
plt.title("IceCrean Data")
plt.show()

#Linear Plot

plt.figure(figsize=(8,5))
sb.lineplot(data=IceCreamDF, x="Flavor", y="votes")
plt.xlabel("Flavor")
plt.ylabel("votes")
plt.title("IceCream Data")
plt.show()

#pie plot

plt.figure(figsize=(8,5))
plt.pie(IceCreamDF["votes"], labels =IceCreamDF["Flavor"], autopct="%1.1f%%")
plt.xlabel("Flavor")
plt.ylabel("votes")
plt.title("IceCream Data")
plt.show()