import numpy as np
import matplotlib.pyplot as plt
import time
A=50
N=10
n=np.round(20+(A-20)*np.random.random((N,2)))
print("n=",n)
#plt.ion()
plt.text(10,25,"WSN PROJ")
plt.xlabel("area")
plt.ylabel("area1")
plt.plot(n[:,0],n[:,1],'ko')
EON=np.full((N,1),1000)
print("EON=",EON)
redflag=[]
while(1):
    flag=0
    nei=[]
    ndx=[]
    a=np.random.randint(10)
    c=n[a] #c:cordinates
    for i in range(N):
        plt.text(n[i,0],n[i,1],i)
        plt.pause(0.1)
        d=np.sqrt(np.square(n[i][0]-c[0])+np.square(n[i][1]-c[1]))
        if(d>0 and d<=18):
            print("neibours are",i,"=",n[i],"d=",d)
            nei.append(n[i])
            ndx.append(i)
            redflag.append(i)
           # plt.plot(n[i][0],n[i][1],"bo")
    print("nei=",nei)
    print("ndx=",ndx)
    for i in range(len(nei)):
        plt.plot((c[0],nei[i][0]),(c[1],nei[i][1]))
    ETX=np.random.randint(80,90,1)
    ERX=np.random.randint(50,70,1)
    print("transmitter is:",a,"=",c)
    print("receivers are:",ndx,"=",nei)
    print("ETX=",ETX,"ERX=",ERX)
    EON[a]=EON[a]-ETX
    for i in range(len(ndx)):
        EON[ndx[i]]=EON[ndx[i]]-ERX
    for i in range(N):
        
        if (EON[i]>=800 and EON[i]<1000) and EON[i]>0:
            print("energy is good")
            plt.plot(n[i][0],n[i][1],"go")
        elif (EON[i]>=500 and EON[i]<800) and EON[i]>0:
            print("energy is moderate")
            plt.plot(n[i][0],n[i][1],"yo")
        elif (EON[i]>=0 and EON[i]<500) and EON[i]>0:
            print("energy is low")
            plt.plot(n[i][0],n[i][1],"ro")
            
        elif(EON[i]<0):
            flag=flag+1
        
    print("EON=",EON)
    print("____________________loop over_____________")
    
    if(flag==N):
        print("___________break______________________")
        break

plt.show()
