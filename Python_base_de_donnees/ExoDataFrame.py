import pandas as pd
import numpy.random as npr


######################### Ex1 #########################

n=10
def simu(n):
    Ind=range(1,n+1)
    Noms=[f'enregistrement {i}' for i in Ind]
    Val1=npr.random(size=n)
    Val2=npr.random(size=n)
    Val3=npr.random(size=n)
    Snoms=pd.Series(Noms,index=Ind)
    SVal1=pd.Series(Val1,index=Ind)
    SVal2=pd.Series(Val2,index=Ind)
    SVal3=pd.Series(Val3,index=Ind)


    D={"nom":Snoms, "val1":SVal1, "val2":SVal2, "val3":SVal3}

    DF=pd.DataFrame(D)
    
    return DF

DF=simu(n) ; DF

DF["moy"]=(DF["val1"]+DF["val2"]+DF["val3"])/3

DF.drop(['val1','val2','val3'],axis=1,inplace=True) #axis=1 pour colonne (!!par défaut axis=0 pour les lignes!!)
#Inplace pour écraser "l'ancien" DF par celui renvoyé par cette méthode



DF2=DF.copy()
DF2[DF2["moy"]>0.5]

def simu2(n):
    Ind=range(1,n+1)
    Noms=[f'enregistrement {i}' for i in Ind]
    M=npr.random(size=(n,3))

    DFnoms=pd.DataFrame(Noms)
    DFM=pd.DataFrame(M)
    DF=pd.concat((DFnoms,DFM),axis=1)
    DF.index=Ind
    DF.columns=["nom","val1",'val2','val3']
    
    return DF

DF3=simu2(n) ; DF3


######################### Ex2 #########################

Titanic=pd.read_csv("/users/2024/ds1/122005148/Bureau/Python_base_de_donnees/titanic.csv",usecols=[0,1,2,3,4,5],index_col=(0))

Titanic

len(Titanic)

GrpSex=Titanic.groupby("Sex")
GrpSex['Sex'].count()


Titanic["Sex"].value_counts()
Titanic["Survived"].value_counts()

GrpSex['Survived'].mean()

GrpSexClass=Titanic.groupby(['Sex','Pclass'])
for R in GrpSexClass : 
    print(R)


GrpSexClass["Survived"].mean().unstack()

Age=pd.cut(Titanic['Age'],[0,18,120],right=False)
GrpAge=Titanic.groupby(Age)
GrpAge['Survived'].mean()
Age.count()


######################### Ex3 #########################

Workers=pd.read_csv("/users/2024/ds1/122005148/Bureau/Python_base_de_donnees/workers.data", usecols=[0,9,12,13,14],
                    names=['Age','Sexe','Heures/Sem','Pays','Salaire'])

DFSample=Workers.sample(10000)
DFSample.head(5)
DFSample.sort_index(inplace=True)
DFSample.head(5)
DFSample.reset_index(drop=True, inplace=True)
DFSample

DFSample

Pays=(Workers['Pays'].unique())
Pays.sort()
Pays


pd.crosstab(Workers['Sexe'], Workers['Salaire'])

Workers.groupby(['Sexe','Salaire'])['Age'].count().unstack()

Inde = Workers[Workers['Pays']==' India']
Inde

Inde2 = Workers[Workers['Pays']==' India'][Workers['Salaire']==' >50K']
Inde2['Heures/Sem'].mean()

Grp=Workers.groupby('Pays')['Heures/Sem']
Grp.mean()
Grp.agg('mean') #permet d'appliquer une fonction perso

Grp.mean().sort_values(ascending=False).head(5)


######################### Ex4 #########################

EtatCivil=pd.read_csv("/users/2024/ds1/122005148/Bureau/Python_base_de_donnees/etatcivil.csv", sep=',' ,index_col=0)

EtatCivil.head(3)
EtatCivil.columns=['Année','Nom','Sexe','Naissances']

EtatCivil[((EtatCivil['Nom'].str)[:4]=='Fran')]
Fran=EtatCivil[(EtatCivil['Nom'].str).startswith("Fran")]

Grp=Fran.groupby('Nom')['Naissances'].sum()
Grp.sort_values(ascending=False).head(5)

Fran5=Grp.sort_values(ascending=False).head(5)

Fran5DF=Fran[Fran['Nom'].isin(Fran5.index)] ; Fran5DF
Fran5DFP=Fran5DF.pivot_table('Naissances',index='Année',columns='Nom', aggfunc=sum) #Effectif M et F à sommer 

Fran5DFP.plot(grid=True,ylabel="Naissances" )

Camille=EtatCivil[EtatCivil["Nom"]=='Camille']

CamilleP=Camille.pivot_table('Naissances',index='Année',columns='Sexe')

CamilleP.plot(grid=True,ylabel="Naissances" )

CamilleP['%F']=100*CamilleP['F']/(CamilleP['F']+CamilleP['M'])
CamilleP['%M']=100-CamilleP['%F']

del CamilleP['F']
del CamilleP['M']

CamilleP.plot(grid=True,ylabel="%Naissances" )


