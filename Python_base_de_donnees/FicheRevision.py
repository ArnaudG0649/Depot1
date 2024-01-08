# -*- coding: utf-8 -*-
#!/bin/env python3

import pandas as pd
import numpy.random as npr
import numpy as np

########################Séries########################

#Sans Préciser les indices
prenoms=["Gilbert","Ray","Kevin"]

SerPrenoms=pd.Series(prenoms) ; SerPrenoms

#Pour rajouter les indices 
Ind=["4","Bidule","JaaJ"]

SerPrenoms.index=Ind ; SerPrenoms #Il suffit de changer l'attribut

#En précisant les indices (on par cette fois-çi d'un dictionnaire)
notes = {"maths" : 19,
         "Anglais" : 12,
         "Géo" : 15}

Ser=pd.Series(notes,name="notes") ; Ser

#Pour ajouter un entré
Ser["Français"]=8
print(Ser)
Ser.values

#En précisant les indices avec une liste distincte : 
Gens = pd.Series(np.array([52,47,39,65]),index=["Pierre","Paul","Jacques","Simon"],name="âge")
Gens=Gens.rename("Sous(en euros)")
Gens
Gens["Pierre":"Jacques"] #attention "Jacques" est compris dedans ! 

#Selection par l'indice ou par l'ordre

Pays=pd.Series(["France","Italie","Espagne","Allemagne"], index=[1,2,7,-5])
print(Pays[2]) #Italie : Selection par l'indice
print(Pays.iloc[3]) #Allemagne, selection par l'odre
print(Pays.loc[2]) #Italie : Selection par l'indice
#Enfaite Pays[i]=Pays.loc[i]

#Pour concaténer
Ser3=pd.concat([Gens,Pays]) ; Ser3





########################DataFrame########################

##Importer des DataFrames## 
    
Titanic=pd.read_csv("titanic.csv",usecols=[0,1,2,3,4,5])
Titanic.loc[1] #prend par défaut un range(n) comme liste d'indice
Titanic=pd.read_csv("titanic.csv",usecols=[0,1,2,3,4,5],index_col=(0))
Titanic.iloc[1]

Workers=pd.read_csv("workers.data", usecols=[0,9,12,13,14], names=['Age','Sexe','Heures/Sem','Pays','Salaire'])

Bidule=pd.read_excel("Bidule.xlsx",index_col=(0)) ; Bidule

EtatCivil=pd.read_csv("etatcivil.csv", sep=',' ,index_col=0)
EtatCivil.columns=['Année','Nom','Sexe','Naissances']

##Créer un DataFrame## 

#Avec un dictionnaire de séries : 
Dict={"Age": pd.Series([25,30,35],index=["Sylvie","Gilles","Sylvain"]),
     "Ville" : pd.Series(["Lorient","Angers","Vannes","Le Mans"],index=["Sylvie","Gilles","Sylvain","Thomas"])}
DF=pd.DataFrame(Dict)
DF

#Avec un dictionnaire de listes : 
Dict2={"Prenom" : ["Sylvie","Gilles","Sylvain","Thomas"], "Age" : [25,30,35,40] }
DF2=pd.DataFrame(Dict2)
DF2

#Avec une matrices :
M=npr.random((80,5))
DF3=pd.DataFrame(M) ; DF3
    


##Sélection 

DF2["Prenom"]["Le crack"] #[colonne][indice]
Bidule[(Bidule["Taille"]>160) & (Bidule["Poids"]<80)] #Masque
DF2.head(2) #2 premières lignes
DF2.tail(2) #2 dernières lignes

DFSample=Workers.sample(10000)  #10000 lignes au hasard
len(Workers) #Nombre de ligne

Fran=EtatCivil[EtatCivil['Nom'].str.startswith("Fran")] #Masque pour les caractères



##Changer indices et noms des colonnes##

DF2.index=["La Schtrompfette", "Le démolisseur", "Le crack","Le BG"] #Pour rajouter les indices
DF2
DFSample.sort_index(inplace=True) #Range les indices
DFSample.reset_index(inplace=True) #Rample par le range(..)=[0,1,2,...,max]


DF3.columns=["Arnaud","Guillaume","Charlie","Mia","Kevin"] ; DF3
DF.rename(columns = {"Age" : "Sous"},inplace=True) ; DF



##Concaténation 

DFC1=pd.DataFrame({"Nom":['Gilles','Sylvain'],'Age':[25,28]})
DFC2=pd.DataFrame({"Nom":['Thomas','Alib'],'Age':[19,31]})
pd.concat([DFC1,DFC2]) #Concaténation VERTICAL, attention pensez à rechanger les indices

DFC3=pd.DataFrame({"Profession":['Plombier','Electricien'],'Tel':["05-87-52-10-49","05-14-21-78-91"]})
DFC3

pd.concat([DFC1,DFC3],axis=1) #Concaténation HORIZONTAL



##Enlever une colonne ou ligne 

Bidule.drop(['Prenoms','Poids'],axis=1,inplace=True) #axis=1 pour colonne (!!par défaut axis=0 pour les lignes!!)
Bidule.drop([4],inplace=True) 
print(Bidule)



##GroupBy, découpage par classe et tableaux croisés

GrpSex=Titanic.groupby("Sex")
for r in GrpSex : print(r)
GrpSex['Sex'].count()


Titanic["Sex"].value_counts() #Compte pour chaque modalité
Titanic["Survived"].value_counts()

GrpSex['Survived'].mean() #Moyenne de cette modalité pour chaque groupe

GrpSexClass=Titanic.groupby(['Sex','Pclass']) #Fait les 2*3 tables
for R in GrpSexClass : 
    print(R)

GrpSexClass["Survived"].mean()
GrpSexClass["Survived"].mean().unstack() #Permet de mettre "Pclass" en colonne au lieu de faire un total de 6 lignes.

Age=pd.cut(Titanic['Age'],[0,18,120],right=False) #Découpage en classe par rapport à "Age". Right :Est ce que on ferme à droite chaque classe.
GrpAge=Titanic.groupby(Age)
GrpAge['Survived'].mean()
Age.count() #Ici on remarque qu'il y a moins de données sur l'âge que le total, c'est à dire qu'on ne connait pas l'âge de tout le monde.

pd.crosstab(Workers['Sexe'], Workers['Salaire']) #Tableau de contingence

Workers.groupby(['Sexe','Salaire'])['Age'].count().unstack() #Il faut prendre une des autres données (ici "Age") pour pas qu'il le fasse 3 fois. 

Grp=Workers.groupby("Pays")['Heures/Sem']
Grp.mean()
Grp.agg('mean') #Peut être utilisé avec une fonction perso ->
#Exemple : 
def f(x) : # x est une liste
    return sum(x)**2   
Grp.agg(f)

Grp.mean().sort_values(ascending=False).head(5) #ascending = ordre croissant (de haut en bas)


##Pivotage de tableau : 
    
Camille=EtatCivil[EtatCivil["Nom"]=='Camille'] ; Camille

CamilleP=Camille.pivot_table('Naissances',index='Année',columns='Sexe') #"Naissances" est la donnée qui sera dans les "cases" et 
#les deux modalités de "sexe" seront les nouvelles colonnes
CamilleP


##Un petit peu de plot 

CamilleP.plot(grid=True,ylabel="Naissances" ) #Chaque colonne donne une courbe



