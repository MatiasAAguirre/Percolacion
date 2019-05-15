import matplotlib.pyplot as plt
import csv
import numpy as np


x1=[] #Probabilidad dim = 4
y1=[] #Intensidad cluster percolante dim = 4

fit=[]
fit_fn=[]

with open("masa", "r") as f:
    plots = csv.reader(f, delimiter=" ")
    for row in plots:
        if len(row)==0 :
            pass
        else:
            x1.append(float(row[0]))
            y1.append(float(row[1]))
            

fit.append(np.polyfit(np.log(x1), np.log(y1), 1))
fit_fn.append(np.poly1d(fit[0]))
plt.plot(np.log(x1), fit_fn[0](np.log(x1)), '--k')


plt.plot(np.log(x1),np.log(y1),"o")

    
plt.xlabel("Dimensión")
plt.ylabel("Masa Cluster Percolante")

plt.title("Masa de Cluster Percolante vs Dimensión")
plt.legend()
plt.show()
