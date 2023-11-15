from random import randrange

class Carte():
    valeurs = list(range(7,11)) + ['Valet','Dame','Roi','As']
    couleurs = ['Coeur','Carreau','Pique','Trèfle']

    def __init__(self,v=None,c=None):
        if v:
            if not v in Carte.valeurs:
                raise ValueError(f"{v}: valeur incorrecte")
        else:
            v = Carte.valeurs[randrange(0,len(Carte.valeurs))]
    
        if c:
            if not c in Carte.couleurs:
                raise ValueError(f"{c}: couleur incorrecte")
        else:
            c = Carte.couleurs[randrange(0,len(Carte.couleurs))]
    
        self.couleur = c
        self.valeur = v
        
        if isinstance(v,int): self.num=v 
        else : 
            Figures=['Valet','Dame','Roi','As']
            for i in range(1,5):
                if Figures[i-1]==v : self.num=i+10
        #self.num sera utilisée pour les quintes. L'idée est que self.valeur=="Valet" <=> self.num==11, ....=="Dame" <=> ..=12 etc.
        
    def __repr__(self) : 
        return f'{self.valeur} de {self.couleur}'
    
    def __eq__(self, Y):
        return (self.couleur==Y.couleur and self.valeur==Y.valeur)
   
    
class Cartes():
    def __init__(self,C=None):
        self.cartes = []
        if C : self.cartes=C.cartes.copy()
    
    def __repr__(self):
        return ", ".join([str(c) for c in self.cartes])

    def ajoute(self,c):
        self.cartes += [c]
        
    def pioche(self) :
        if self.cartes==[] : raise ValueError("pioche vide !")
        else : 
            i=randrange(0,len(self.cartes))
            carte=self.cartes[i]
            self.cartes.pop(i)
            return carte
        
        
class Jeu(Cartes) : 
    
    def __init__(self) : 
        super().__init__(self)
        for v in Carte.valeurs : 
            for c in Carte.couleurs :
                self.ajoute(Carte(v,c))
        
    def __isub__(self,carte):
        if carte not in self.cartes :
            raise ValueError("Carte non présente dans le jeu !")
        else : 
            self.cartes.remove(carte)
            return self
        
    
class Main(Cartes) : 
    
    def __init__(self,jeu):
        super().__init__(self)
        self.jeu=jeu
    
    def complete(self) : 
        if self.jeu.cartes==[] : raise ValueError(f"plus de carte pour compléter la main [{self}]")
        else :
            carte=self.jeu.cartes[randrange(0,len(self.jeu.cartes))]
            self.jeu -= carte
            self.ajoute(carte)
            
        ## Le but de cette partie est de réorganiser les cartes par couleur puis par valeur à chaque fois qu'on en rajoute une. Elle est n'est pas indispensable.
        L=self.cartes.copy()
        self.cartes=[]
        for c in Carte.couleurs :
            for v in Carte.valeurs : 
                if Carte(v,c) in L : self.ajoute(Carte(v,c))
        ##
        
    def __isub__(self,cartes):
        self.cartes=[carte for carte in self.cartes if carte not in cartes.cartes] 
        #D'un point de vu ensembliste cela correspond à self.cartes/cartes.cartes
        return self 
        

class Carre(Cartes) : 
    
    def __init__(self,main) :
        super().__init__(self)
        p=True # p = "On n'a Pas encore formé de carré"        
        for v in Carte.valeurs : 
            if p :
                LCarre=[Carte(v,c) for c in Carte.couleurs]
                Carre_in_main=all([(carte in main.cartes) for carte in LCarre]) 
                if Carre_in_main : 
                    p=False
                    for carte in LCarre : self.ajoute(carte)
                    self.valeur=v
        if p : raise RuntimeError(f'pas de carré dans [{main}]')
        
    def __repr__(self):
        if self.valeur=="As" : return "carré d'As"
        else : return f"carré de {self.valeur}"
        

class Quinte(Cartes) : 
    
    def __init__(self,main) :
        super().__init__(self)
        p=True # p = "On n'a Pas encore formé de quinte"
        for c in Carte.couleurs : 
            for i in range(7,10) : #Correspond aux premières valeurs de chaque Quinte possible
                if p :
                    Lnum=[carte.num for carte in main.cartes if carte.couleur==c] #Liste des numéros associés aux cartes de couleur c 
                    Quinte_in_main=all([(num in Lnum) for num in range(i,i+5)]) #Une quinte correspond à un alignement comme [8,9,10,11,12] parmi les numéros des cartes d'une même couleur
                    if Quinte_in_main : 
                        p=False
                        for num in range(i,i+5) : self.ajoute(Carte(Carte.valeurs[(num-7)],c))
        if p : raise RuntimeError(f'pas de quinte dans [{main}]')        


print(Carte())                      
print(Carte())                      
print(Carte())                      
carte1 = Carte(7,"Coeur")
print(carte1)                      
# carte2 = Carte("Valet","pic")       
carte3 = Carte("Valet","Pique")
print(carte3)  


#3 cartes
carte1 = Carte("As","Trèfle")
carte2 = Carte(7,"Coeur")
carte3 = Carte("Valet","Pique")

# un ensemble de cartes (vide au départ)
des_cartes = Cartes()

# on y ajoute les 3 cartes
for une_carte in [carte1,carte2,carte3]:
    des_cartes.ajoute(une_carte)

print(f"{des_cartes=}")

les_memes = Cartes(des_cartes)
print(f"{les_memes=}")

j=0
try:
    while True  :
        print(f"{des_cartes.pioche()=}")
        print(f"{des_cartes=}")
        print(f"{les_memes=}")
        j+=1
except ValueError as e:
  # traceback.print_exc(file=sys.stdout)
    print(e)
print("fin de programme")


un_jeu = Jeu()
print(f"{un_jeu=}")
un_jeu -= Carte('Valet','Coeur')
un_jeu -= Carte('As','Pique')
un_jeu -= Carte(10,'Trèfle')
print(f"{un_jeu=}")


le_jeu = Jeu()

# on crée 2 mains vides
ma_main = Main(le_jeu)
ta_main = Main(le_jeu)
print(f"{ma_main=}")
print(f"{ta_main=}")

#on y ajoute 3 cartes
for i in range(3):
    ma_main.complete()
    print(f"{ma_main=}")
    ta_main.complete()
    print(f"{ta_main=}")
print(f"{le_jeu=}")


try:
    for i in range(25):
        ma_main.complete()
except ValueError as e:
    print(e)

try:
  for i in range(25):
    ta_main.complete()
except ValueError as e:
  # traceback.print_exc(file=sys.stdout)
  print(e)

print("fin de programme")


le_jeu = Jeu()

# une main de 25 cartes
une_main = Main(le_jeu)
for i in range(25):
  une_main.complete()
print(f"{une_main=}")

# recheche tous les carrés contenus dans la main
while True:
  try:
    un_carre = Carre(une_main)               # essai de créer un carré
    # si on est là, c'est qu'un carré a été créé
    print(f"{un_carre=},{une_main=}")
    une_main -= un_carre                     # on l'enlève de la main
  except RuntimeError as e:
    # si on est là, c'est qu'un carré n'a pas pu être créé
    print(e)
    break

print("fin de programme")


le_jeu = Jeu()

# une main de 25 cartes
une_main = Main(le_jeu)
for i in range(25):
  une_main.complete()
print(f"{une_main=}\n")

# recheche toutes les quintes contenues dans la main
while True:
  try:
    une_quinte = Quinte(une_main)               # essai de créer une quinte
    # si on est là, c'est que une quinte a été créée
    print(f"{une_quinte=}\n{une_main=}")
    une_main -= une_quinte                     # on l'enlève de la main
  except RuntimeError as e:
    # si on est là, c'est que une quinte n'a pas pu être créée
    print(e)
    break

print("fin de programme")



