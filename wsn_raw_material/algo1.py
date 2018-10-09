import numpy as np
import matplotlib.pyplot as plt
n=10
X=np.round(1+(20-1)*np.random.random((2,n))
#siz[]=np.shape(X);
#R=8
#plt.figure(1)
plt.plot(X[0,:],X[1,:],'ro');
for i in range (0, X):
   plt.text(X[0,i],X[1,i], i+1);
#dist=np.zeros((siz[1],siz[1]));
#for i in range (0, siz[1]):
    #for j in range (0, siz[1]):
        #dist[i,j]=np.sqrt((X[0,i]-X[0,j])**2+(X[1,j]-X[1,i])**2);
'''print (dist)

Graph_matrix=np.zeros((siz[1], siz[1]));
for i in range (0, siz[1]):
    for j in range(0,siz[1]):
        if i !=j:
            if dist[i,j]<=R:
                Graph_matrix[i,j]=1;
            else:
                Graph_matrix[i,j]=0;
        else:
            Graph_matrix[i,j]=0;
print (Graph_matrix)

nodes = Graph_matrix[a-1,:];
nei=[];
for i in range(np.size(nodes)):
    if nodes[i]==1:
        nei.append(i);
        print(i+1);
        plt.plot(X[0,i],X[1,i],'go');

plt.plot(X[0,a-1],X[1,a-1],'ko');

for i in range(len(nei)):
    plt.plot([X[0,a-1],X[0,int(nei[i])]],[X[1,a-1],X[1,int(nei[i])]],'b');
 '''   
plt.show();
              
