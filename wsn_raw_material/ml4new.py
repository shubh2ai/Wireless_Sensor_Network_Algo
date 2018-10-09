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


#a=int(input("enter ur node:"))

while(1):
    nei=[]
    for i in range(N):
        plt.text(n[i,0],n[i,1],i)
        plt.pause(0.1)
        a=np.random.randint(9)
        c=n[a] #c:cordinates
        #print(c)
        #print("x=",c[0],"y=",c[1])
        d=np.sqrt(np.square(n[i][0]-c[0])+np.square(n[i][1]-c[1]))
        if(d>0 and d<=18):
            print("neibours are",i,"=",n[i],"d=",d)
            nei.append(n[i])
            #plt.plot(n[i][0],n[i][1],"bo")

    #print(nei)      
    for i in range(len(nei)):
        plt.plot((c[0],nei[i][0]),(c[1],nei[i][1]),'b')
    EON=np.full((N,2),1000)
    print("EON=",EON)
    s=[]
    ETX=[]
    ERX=[]
    #SRC=[]
    count=0
    for i in  range(len(nei)):
        s=np.random.randint(0,2,N)
        ETX=np.random.randint(240,260,1)
        ERX=np.random.randint(210,220,1)
        #SRC=np.random.randint(10,20,1)
        print("ETX=",ETX,"ERX=",ERX)
        print (s)
        count+=1
        print("count=",count)
        if s[i] == 0:
            print("node is transmitting",s[i] )
            EON[i]=EON[i]-ETX
            print("EON=",EON[i])
            if (EON[i][0]>=800 and EON[i][0]<1000):
                print("energy is good")
                plt.plot(nei[i][0],nei[i][1],"go")
            elif (EON[i][0]>=500 and EON[i][0]<800):
                print("energy is moderate")
                plt.plot(nei[i][0],nei[i][1],"bo")
            elif (EON[i][0]>=200 and EON[i][0]<500):
                print("energy is low")
                plt.plot(nei[i][0],nei[i][1],"yo")
            elif (EON[i][0]>=10 and EON[i][0]<200):
                print("energy is crfitically low")
                plt.plot(nei[i][0],nei[i][1],"ro")
            plt.pause(0.3)
            time.sleep(0.3)
        elif s[i]==1:
            print("node is receiving",s[i])
            EON[i]=EON[i]-ERX
            print("EON=",EON[i])
            if (EON[i][0]>=800 and EON[i][0]<1000):
                print("energy is good")
                plt.plot(nei[i][0],nei[i][1],"go")
            elif (EON[i][0]>=500 and EON[i][0]<800):
                print("energy is moderate")
                plt.plot(nei[i][0],nei[i][1],"bo")
            elif (EON[i][0]>=200 and EON[i][0]<500):
                print("energy is low")
                plt.plot(nei[i][0],nei[i][1],"yo")
            elif (EON[i][0]>=200 and EON[i][0]<500):
                print("energy is crfitically low")
                plt.plot(nei[i][0],nei[i][1],"ro")
            plt.pause(0.3)
            time.sleep(0.3)
        
print("EON=",EON)
plt.show() 
