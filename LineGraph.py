import matplotlib.pyplot as plt
import numpy as np
#year = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
#emp_rate =[2.3,4.5,6.7,1.4,4.5,9.0,8.1,0.1,9.9,0.5,9.1]
#plt.plot(year,emp_rate,color='red',marker='o')
#plt.title("Employment Ratie per year")
#plt.xlabel("year")
#plt.ylabel("Employment Ratie")
#plt.show()



year = np.array ([2000,2001,2002,2003,2004,2005])
oil_price = np.array([55,65,75,85,95,105])
year2 = np.array ([2000,2001,2002,2003,2004,2005])
economy =np.array ([2.3,3.4,5.6,1.6,3.4,5.7])

plt.plot(oil_price ,year,color='green')
plt.plot(economy,year2,color='blue')
plt.show()
