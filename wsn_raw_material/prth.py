import numpy as np
import matplotlib.pyplot as plt
A=50
N=30

n=np.round(1+(A-1)*np.random.random((N,2)))
print(n)
#siz=np.shape(n)
#print(siz)
#plt.ion()
plt.text(10,25,"WSN PROJ")
plt.xlabel("area")
plt.ylabel("area1")
plt.plot(n[:,0],n[:,1],'ro')


a=int(input("enter ur node:"))
c=n[a] #c:cordinates
print(c)
print("x=",c[0],"y=",c[1])
m=[]
for i in range(N):
    plt.text(n[i,0],n[i,1],i)
    plt.pause(0.2)
    d=np.sqrt(np.square(n[i][0]-c[0])+np.square(n[i][1]-c[1]))
    if(d>0 and d<=18):
        print("neibours are",i,"=",n[i])
        m.append(n[i])
        plt.plot(n[i][0],n[i][1],"go")
for i in range(len(m)):
    plt.plot((c[0],m[i][0]),(c[1],m[i][1]),'k-')
    #plt.plot((x[0],l[i]),(y[1],m[i]),"k-")
"""
for i in range(0,siz[0]):
    for j in range(0,siz[1]):
        if i!=j:
            if d[i,j]<=R:
                GM[i,j]=1
            else:
                d[i,j]=0
"""

        
#for i in range(N):
    #plt.plot([n[0,i-1],n[0,int(c[i])]],[n[1,i-1],n[1,int(c[i])]],"g")
       #x=plt.plot(n[i][0],n[i][1],"go")
#plt.show(g)   
plt.show()
#plt.ioff()



"""
import matplotlib.pyplot as plt
import numpy as np
N=10
nodes=np.round(1+(50-1))*np.random.random((N,2))
plt.plot(nodes[:,0],nodes[:,1],'ro')
for i in range(N):
    plt.text(nodes[i,0],nodes[i,1],i)
plt.text(25,25,'GRAPH ANALYSIS')
plt.xlabel('x axis ')
plt.ylabel('y,axis')
plt.show()
print("nodes",nodes)
def energy():
    a=np.full((10,2),1000)
    print("energy",a)

energy()

m=plt.plot(nodes[:,0],nodes[:,1],'ro')
a=int(input("enter the node=="))
print(nodes[a])
c=nodes[a]
print("x axis value",c[0])
print("y axis value",c[1])
for i in range(N):
    new=np.sqrt(np.square(nodes[i][0]-c[0])+np.square(nodes[i][1]-c[1]))
    print("new",new)
    if (new<=15 and new>0):
        print("final value=",new)
        
        g=plt.plot(nodes[i][0],nodes[i][1],'bo')
        plt.text(nodes[i,0],nodes[i,1],i)
plt.show(g)    
"""
