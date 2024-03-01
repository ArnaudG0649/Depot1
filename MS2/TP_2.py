
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy.random as npr
 
##1.
def N(tds,T=np.inf,N=np.inf):
    if T==np.inf and N==np.inf : raise ValueError("Veuillez donner un temps maximal ou un nombre de saut maximal")
    n,t=0,0
    vecT=[t]
    while t<T and n<N: 
        t+=st.expon.rvs(scale=1/tds)
        vecT.append(t)
        n+=1
    return n,vecT

Poisson1=N(0.08,N=50)[1]

def plotN(tds,T=np.inf,N=np.inf): #Avec le graphe
    if T==np.inf and N==np.inf : raise ValueError("Veuillez donner un temps maximal ou un nombre de saut maximal")
    n,t=0,0
    vecT=[t]
    while t<T and n<N:
        t2=t
        t2+=st.expon.rvs(scale=1/tds)
        vecT.append(t2)
        plt.plot([t,t2],[n,n],'k',lw=1)
        plt.plot([t,t2],[0,0],'r',lw=1)
        n+=1
        t=t2
    plt.show()
    return n,vecT

plotN(0.08,N=50)

##2.
def Fortune(tds,x,a,tmax=np.inf,N=np.inf): 
    if tmax==np.inf and N==np.inf : raise ValueError("Veuillez donner un temps maximal ou un nombre de saut maximal")
    n,t,x2=0,0,x
    vecT=[t]
    while t<tmax and n<N :#and x2>0:
        t2,x2=t,x
        t2+=st.expon.rvs(scale=1/tds)
        x2-=a*(t2-t)
        vecT.append(t2)
        plt.plot([t,t2],[x,x2],'k',lw=1)
        plt.plot([t,t2],[0,0],'r',lw=1)
        t,x=t2,x2+1
        n+=1
    plt.show()
    return x,vecT

F=Fortune(0.08,6,0.1,N=50)
print(F[0]/F[1][-1])
S=0
for i in range(1000) : 
    F=Fortune(0.08,6,0.1,N=50)
    S+=F[0]/F[1][-1]
print(S/1000)

##3.
F=Fortune(0.08,6,0.1,N=5000)
print(F[0]/F[1][-1]) #~=0.02


##4.
def Fortunemax(tds,x,a,tmax=np.inf,N=np.inf): 
    if tmax==np.inf and N==np.inf : raise ValueError("Veuillez donner un temps maximal ou un nombre de saut maximal")
    n,t,x2=0,0,x
    vecT=[t]
    while t<tmax and n<N and x2>0:
        t2,x2=t,x
        t2+=st.expon.rvs(scale=1/tds)
        x2-=a*(t2-t)
        vecT.append(t2)
        #plt.plot([t,t2],[x,x2],'k',lw=1)
        #plt.plot([t,t2],[0,0],'r',lw=1)
        if x2<0 : tmort=(x*t2-x2*t)/(x-x2)
        t,x=t2,x2+1
        n+=1
    #plt.scatter([tmort],[0])
    #plt.show()
    if tmort : return tmort,x,vecT
    else : return x,vecT
    

S,Sc,n=0,0,0
LT=[]
for i in range(100000) : 
    F=Fortunemax(0.08, 6, 0.1,tmax=100000)
    if len(F)==3: 
        LT.append(F[0])
        S+=F[0]
        Sc+=F[0]**2
        n+=1
Esp=S/n
Var=(n/(n-1))*(Sc/n-Esp**2)
##6.
plt.hist(LT,density=True)

##7.
Est=6*sum((np.array(LT)==300))/len(LT)/0.1/300 ; print(Est)













