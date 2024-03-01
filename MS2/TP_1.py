#!/bin/env python3
 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy.random as npr

## 2.

lamb=2
n=10000000
N=10000
Echantillon=st.geom.rvs(lamb/n,size=N)/n
plt.hist(Echantillon,250,density=True)

X=np.linspace(0,6,200000)
plt.plot(X,st.expon.pdf(X,scale=1/lamb))


## 3.

pas=20
M=np.array([[0.1,0.6,0.3],[0.4,0.2,0.4],[0.5,0,0.5]])
Etat=0
LEtat=[Etat]
for j in range(pas) :
    for i in range(3) :
        if i==Etat : 
            EtatT=npr.choice([0,1,2],p=M[i])
    Etat=EtatT
    LEtat.append(Etat)
print(LEtat)


## 5.

def sigma(x=0) :
    if x not in [0,1,2] : raise ValueError('valeur de x impossible')
    M=np.array([[0.1,0.6,0.3],[0.4,0.2,0.4],[0.5,0,0.5]])
    Etat=x
    LEtat=[Etat]
    pas=0
    while Etat==x and pas<10^3 :
        for i in range(3) :
            if i==Etat :
                print(f'{i=}')
                EtatT=npr.choice([0,1,2],p=M[i])
            print(EtatT)
        Etat=EtatT
        LEtat.append(Etat)
        pas+=1
    return LEtat,pas

sigma()
#Construction d'un échantillon de sigmas 
N=10000
Echantillon=[]
for i in range(N) : 
    Echantillon.append(sigma()[1])

X,Eff=np.unique(Echantillon,return_counts=True)
pEff=Eff/len(Echantillon)

plt.hist(Echantillon,len(X),density=True)
plt.plot(X,st.geom.pmf(X,1-M[0,0]))


L=[]
for i in range(10000) : 
    L.append(npr.choice([0,1,2],p=M[0]))
    
np.unique(L,return_counts=True)





































