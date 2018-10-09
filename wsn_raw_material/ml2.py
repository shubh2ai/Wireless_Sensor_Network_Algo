import numpy as np
import matplotlib.pyplot as plt
A=50
N=10
n=np.round(1+(A-1)*np.random.random((N,2)))
print(n)
plt.ion()
plt.text(10,25,"WSN PROJ")
plt.xlabel("area")
plt.ylabel("area1")
for i in range(0,N):
    plt.plot(n[i,0],n[i,1],'--ro')
    plt.text(n[i,0],n[i,1],i)
    plt.pause(0.5)

plt.ioff()





"""
static nodes
A=50
N=10
n=np.round(1+(A-1)*np.random.random((N,2)))
print(n)
plt.plot(n[:,0],n[:,1],'--ro')
plt.show()
"""
