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

RNrx=[]
RNtx=[]


EON=np.full((N,1),1000)
print("EON=",EON)
s=[]
ETX=[]
ERX=[]
#SRC=[]
count=0
txcount=0
rxcount=0
rxc=[]
txc=[]
while(1):
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
            plt.plot(n[i][0],n[i][1],"bo")
      
    for i in range(len(nei)):
        plt.plot((c[0],nei[i][0]),(c[1],nei[i][1]),'b')
    print("___________________i=_______________________",i)
    s=np.random.randint(0,2,len(nei))
    ETX=np.random.randint(80,90,1)
    ERX=np.random.randint(50,70,1)
    print (s)
    print("ETX=",ETX,"ERX=",ERX) 
    count=count+1
    for i in range(len(nei)): 
                if s[i] == 0 and EON[i]>0:
                    print(i,"node is transmitting",s[i] )
                    EON[ndx[i]]=EON[ndx[i]]-ETX
                    print("EON=",EON[i])
                    if (EON[i]>=800 and EON[i]<1000) and EON[i]>0:
                        print("energy is good")
                        plt.plot(nei[i][0],nei[i][1],"go")
                    elif (EON[i]>=500 and EON[i]<800) and EON[i]>0:
                        print("energy is moderate")
                        plt.plot(nei[i][0],nei[i][1],"bo")
                    elif (EON[i]>=200 and EON[i]<500) and EON[i]>0:
                        print("energy is low")
                        plt.plot(nei[i][0],nei[i][1],"yo")
                    elif (EON[i]>=10 and EON[i]<200) and EON[i]>0:
                        print("energy is crfitically low")
                        plt.plot(nei[i][0],nei[i][1],"ro")
                        RNtx.append([nei[i][0],nei[i][1]])
                        txcount=txcount+1
                        txc.append(i)
                        txc.append("node & count")
                        txc.append(txcount)
                        rxc.append('//')
                    
                    plt.pause(0.3)
                    #time.sleep(0.3)
                elif s[i]==1 and EON[i]>0:
                    print(i,"node is receiving",s[i])
                    EON[ndx[i]]=EON[ndx[i]]-ERX
                    print("EON=",EON[i])
                    if (EON[i]>=800 and EON[i]<1000) and EON[i]>0:
                        print("energy is good")
                        plt.plot(nei[i][0],nei[i][1],"go")
                    elif (EON[i]>=500 and EON[i]<800) and EON[i]>0:
                        print("energy is moderate")
                        plt.plot(nei[i][0],nei[i][1],"bo")
                    elif (EON[i]>=200 and EON[i]<500) and EON[i]>0:
                        print("energy is low")
                        plt.plot(nei[i][0],nei[i][1],"yo")
                    elif (EON[i]>=10 and EON[i]<200) and EON[i]>0:
                        print("energy is crfitically low")
                        plt.plot(nei[i][0],nei[i][1],"ro")
                        RNrx.append([nei[i][0],nei[i][1]])
                        rxcount=rxcount+1
                        rxc.append(i)
                        rxc.append("node & count")
                        rxc.append(rxcount)
                        rxc.append('//')
                    plt.pause(0.3)
                    #time.sleep(0.3)
                print("sirf EON=",EON)
                
           
plt.show()
"""if EON[i]<=0 :
    print("energy bachi nahi ab jao samosa khao.")
    print(rxcount,"RNrx=",RNrx,txcount,"RNtx=",RNtx)
    print("rxc=",rxc,"txc=",txc)
    print("EON=",EON)
    print("count=",count,"rxcount=",rxcount,"txcount=",txcount)
    break
"""


