import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2*np.pi,2*np.pi,np.pi/10)
y=np.sin(x)
print(x)
print(y)
plt.ion()
for i in range(0,np.size(y)):
    plt.plot(x[i],y[i],"ro")
    plt.text(x[i],y[i],i)
    plt.xlim([-2*np.pi,2*np.pi])
    plt.ylim([-1.5,1.5])
    plt.pause(0.5)
plt.ioff()



"""
x=np.arange(-2*np.pi,2*np.pi,np.pi/10)
y=np.sin(x)
plt.plot(x,y)
plt.show()
"""
