import matplotlib
import matplotlib.pyplot as plt
import numpy as np

names = np.array(["amid","pallab","omor","munmna","faruk"])
marks = np.array([80,86,93,95,33])


plt.plot(names ,marks)
plt.title("student name vs marks")
plt.xlabel("student names")
plt.ylabel("student marks")
plt.show()

