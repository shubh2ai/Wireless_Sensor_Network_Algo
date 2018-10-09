
import numpy as np
import matplotlib.pyplot as plt
import time
A=50
N=10
n=np.round(20+(A-20)*np.random.random((N,2)))
print("n=",n)

#plt.ion()
plt.text(25,30,"Wireless Sensor Network Project")
plt.xlabel("area")
plt.ylabel("area")
plt.show()

plt.plot(n[:,0],n[:,1],'ko')
EON=np.full((N,1),1000)

print("EON=",EON)
"""
redflag=[]
RN=[]
egraph=[]
count=0
rncount=0
txcount=0
txlist=[]
rnl=[]
esum=0
def energy_graph():
    plt.figure(2)
    plt.plot(egraph[:],"ro")
    plt.plot(egraph[:],"g")
    plt.text(25,25,"Energy Dissipation Graph")
    plt.xlabel("total energy")
    plt.ylabel("time")
    plt.figure(3)
    plt.plot(rnl[:],"ro")
    plt.plot(rnl[:],"g")
    plt.text(25,25,"Red Node Graph")
    plt.xlabel("time")
    plt.ylabel("red node")
    plt.show()

while(1):
    count=count+1
    nei=[]
    ndx=[]
    a=np.random.randint(10)
    c=n[a] #c:cordinates
    txcount=txcount+1
    txlist.append(c)
    for i in range(N):
        plt.text(n[i,0],n[i,1],i)
        plt.pause(0.1)
        d=np.sqrt(np.square(n[i][0]-c[0])+np.square(n[i][1]-c[1]))
        if(d>0 and d<=18):
            print("neibours are",i,"=",n[i],"d=",d)
            nei.append(n[i])
            ndx.append(i)
            redflag.append(i)
            #plt.plot(n[i][0],n[i][1],"bo")
    print("nei=",nei)
    print("ndx=",ndx)
    for i in range(len(nei)):
        plt.plot((c[0],nei[i][0]),(c[1],nei[i][1]),'k')
    
    ETX=np.random.randint(80,90,1)
    ERX=np.random.randint(50,70,1)
    print("transmitter is:",a,"=",c)
    print("receivers are:",ndx,"=",nei)
    print("ETX=",ETX,"ERX=",ERX)
    EON[a]=EON[a]-ETX
    
    EON[ndx]=EON[ndx]-ERX
    esum=np.sum(EON[:])
    egraph.append(esum)
    
    
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
            RN.append([n[i][0],n[i][1]])
            rncount=rncount+1
            if(i not in rnl):
                rnl.append(i)
            #rnl.append(":")
            #rnl.append(RN)
            
        
    print("EON=",EON)
    EON[np.where(EON<0)]=0
    print("EON=",EON)
    print("sum=",esum)
    print("____________________loop over_____________")
    
    if(EON[i]<100 and esum<0):
        print("energy lost")
        print("EON=",EON)
        print(count,"-->",rncount,":RedNode=",RN,"and",txcount,":TxNode=",txlist)
        print("REDNODE_LIST=",rnl)
        print("total_loopcount=",count,"total_rncount=",rncount,"total_txcount=",txcount)
        print("rnl=",rnl)
        print(RN[0],"node got red first and",RN[N-1],"node got red last")
        
        
        energy_graph()
        
        print("___________break______________________")
        
        break

"""   
   


