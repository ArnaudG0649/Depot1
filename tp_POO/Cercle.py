import Point 
import math

class Cercle :
    def initRayon(self,R) :
        self.Rayon=R
        
    def circonference(self) : 
        return 2*math.pi*self.Rayon
    
    def surface(self) : 
        return math.pi*self.Rayon**2

def examine(cercle):
    if type(cercle).__name__==Cercle : 
        cercle.epaisseur=''
    return f"{type(cercle).__name__} {cercle.nom}(centre:{Point.examine(cercle.centre)},rayon:{cercle.rayon},épaisseur={cercle.epaisseur})"

def deplace(cercle,p):
    cercle.centre=p
    return cercle

def copie(cercle):
    copie=cercle
    copie.nom=f"copie_de_{cercle.nom}"
    return copie

class CercleEtendu : pass



"""
correction po2 (suite)

def examine(C):
    if type(C) == Cercle:
        Vrai_rayon = C.rayon
    elif type(C) == CercleEtendu:
        Vrai_rayon = C.rayon + C.epaisseur
    return f"{type(C).__name__} {C.nom}(centre:{Point.examine(C.centre)}),rayon:{Vrai_rayon})"

def deplace(C,P):
    C.centre = P

def copie(C):
    c = C
    c.nom = "copie_de_"+str(C.nom)
    return c
"""