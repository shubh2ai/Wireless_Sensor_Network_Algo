import numpy as np
import matplotlib.pyplot as plt
import time
A=50
N=10
n=np.round(20+(A-20)*np.random.random((N,2)))
plt.ion()
print(n)
plt.plot(n[:,0],n[:,1],"ro")
for i in range(N):
    plt.text(n[i,0],n[i,1],i)
    sleep(0.2)
#plt.show()

plt.ioff()
