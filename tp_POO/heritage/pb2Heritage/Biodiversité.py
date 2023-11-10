class Animal :
    def __init__(self,nom):
        self.nom=nom
        
    def __repr__(self) : 
        SF=''
        for f in self.__class__.__bases__ : 
            SF+=f.__name__+', '        
        return f'je suis {self.nom}, instance de {self.__class__.__name__}, de la famille des {SF}'
    
    def Fuite(self) : 
        self.Bouge()
        self.Crie()
        
class Digitigrade(Animal): 
    def Bouge(self):
        print("Je cours")
        

class Mamifère(Animal): 
    def Bouge(self):
        print("Je cours")
class Souris(Mamifère) : 
    def Crie(self):
        print("Je couine")
class Dauphin(Mamifère): 
    def Bouge(self):
        print("Je nage")
    def Crie(self):
        print("Je siffle")
class Chauve_Souris(Mamifère) : 
    def Bouge(self):
        print("Je vole")
    def Crie(self):
        print("Je grince")
class Ours(Mamifère,Digitigrade) :
    def Crie(self):
        print("Je grogne")        
class Chat(Mamifère,Digitigrade) :
    def Crie(self):
        print("Je miaule")


class Poisson(Animal) : 
    def Bouge(self):
        print("Je nage")
    def Crie(self):
        print("Je reste silencieux")
class Poisson_Crapaud(Poisson) : 
    def Crie(self):
        print("Je grogne")
class Exocoetidae(Poisson) : 
    def Bouge(self):
        print("Je vole")
class Saumon(Poisson) : pass


class Oiseau(Animal) : 
    def Bouge(self):
        print("Je vole")
    def Crie(self):
        print("Je reste silencieux")
class Épervier(Oiseau) : pass
class Rossignol(Oiseau) : pass
class Autruche(Oiseau,Digitigrade) : 
    def Crie(self):
        print("Je claquette")

class Galinacé(Oiseau) : 
    def Crie(self):
        print("Je glousse")
        
class Poule(Galinacé) : pass
class Pintade(Galinacé) : pass


class Territoire:
    def __init__(self):
        self.L=[]
        
    def __iadd__(self,animal):
        self.L.append(animal)
        return self

    def __repr__(self):
        LC=''
        for animal in self.L :
            LC+=str(animal)+'\n'
        return LC
            
    def alerte(self):
        for animal in self.L : 
            animal.Fuite() 













if __name__=="main":
    Lily=Chat()
    Lily.Bouge()
    Lily.Crie()
    Cocotte=Autruche('Cocotte')
    Cocotte.Bouge()
    Cocotte.Crie()
    Cocotte.__class__.__name__
    classe=[(i.__name__) for i in Cocotte.__class__.__bases__]
    print(classe)
    
    print(Cocotte)
