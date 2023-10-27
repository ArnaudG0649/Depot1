#class Frigo():
    
    

D={
        "oeufs": 6
        , "beurre": 250
        , "yaourt": 6
        , "fraise": 10
        }

#D["oeufs"]+=2

E={
        "oeufs": 6
        , "beurre": 250
        , "prunes": 6
        }

"prunes" in list(D.keys())
#D["prunes"]!=2

D.items()
list(D.keys())[0]
print([n for n in D.keys()])

L=['a','b','a']
list(set(L))

def Depose(D,E):
    F={}
    for aliments in list(D.keys()) :
        F[aliments]=D[aliments]
    for aliments in list(E.keys()) :
        if aliments in list(D.keys()) :
            F[aliments]=F[aliments]+E[aliments]
        else:
            F[aliments]=E[aliments]
    return F            
            

list({}.keys())+['.']
def Contenu(D):
    print("contenu:")
    for aliments in list(D.keys()):
        print(f"  {aliments}: {D[aliments]}")
    print("  .")


#Q1

class Frigo : 
    def __init__(self):
        self.C={}
        
    def etat(self):
        D=self.C
        print("contenu:")
        for aliments in list(D.keys()):
            print(f"  {aliments}: {D[aliments]}")
        print("  .")
        
    def depose(self,E):
        D=self.C
        F={}
        for aliments in list(D.keys()) :
            F[aliments]=D[aliments]
        for aliments in list(E.keys()) :
            if aliments in list(D.keys()) :
                F[aliments]=F[aliments]+E[aliments]
            else:
                F[aliments]=E[aliments]
        self.C=F 
        
    def extraire(self,recette):
        if not(recette.possible(self)): print("Pas suffisament d'ingrédients")
        else :
            LR=recette.C
            for ingredient in list(LR.keys()):
                self.C[ingredient]=self.C[ingredient]-LR[ingredient]
                if self.C[ingredient]==0 : self.C.pop(ingredient)


F=Frigo()
F.etat()
F.depose(D)
F.etat()
F.depose(E)
F.etat()


#Q2

class Recette : 
    def __init__(self,C):
        self.C=C
        
    def possible(self,frigo):
        flag=True
        Lrecette=self.C
        for ingredient in list(Lrecette.keys()):
            if not(ingredient in list(frigo.C.keys())) : flag=False
            elif Lrecette[ingredient]>frigo.C[ingredient] : flag=False
        return flag
        
tarte_aux_fraises = Recette({
        "oeufs": 2
        , "beurre": 100
        , "fraise": 10
})

# booéeln indiquant si les ingrédients de la recette sont présents dans le frigo
print(tarte_aux_fraises.possible(F))
        
F.extraire(tarte_aux_fraises)
F.etat()
        
        
        
        
        



















