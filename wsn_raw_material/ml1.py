import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-4*np.pi,4*np.pi,np.pi/10)
y=np.sin(x)
z=np.cos(x)
plt.figure(1)
plt.plot(x,y,"g")
plt.plot(y,z,"r")
plt.legend(["sin","cos"])
plt.show()



"""
x=np.arange(-4*np.pi,4*np.pi,np.pi/10)
y=np.sin(x)
z=np.cos(x)
plt.figure(1)
plt.plot(x,y)
plt.figure(2)
plt.plot(y,z)
plt.show()
"""
