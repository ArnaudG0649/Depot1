class Stylo:
    def __init__(self):
        self.Encre=100
        
    def print(self,c) :
        if self.Encre>0 : 
            if self.Encre>=len(c) : 
                print(c)
                self.Encre-=len(c)
            else :
                print(c[:self.Encre])
                self.Encre=0


class StyloCouleur(Stylo):
    
        def __init__(self,couleur):
            super().__init__()
            CouleursPossibles={"vert":"\x1b[32m"
                               ,"bleu":"\x1b[34m"
                               ,"noir":"\x1b[30m"
                               ,"rouge":"\x1b[31m"}
            if couleur in CouleursPossibles.keys() : 
                self.couleur=couleur
                print(CouleursPossibles[couleur])
            else : raise Exception("Couleur impossible")
            
        def print(self,c) :
            CouleursPossibles={"vert":"\x1b[32m"
                               ,"bleu":"\x1b[34m"
                               ,"noir":"\x1b[30m"
                               ,"rouge":"\x1b[31m"}
            
            if self.Encre>0 : 
                if self.Encre>=len(c) : 
                    print(f"{CouleursPossibles[self.couleur]}{c}\x1b[0m")
                    self.Encre-=len(c)
                else :
                    print(f"{CouleursPossibles[self.couleur]}{c[:self.Encre]}\x1b[0m")
                    self.Encre=0
            
            
            

un_stylo_vert = StyloCouleur("vert")
un_stylo_vert.print("vert émeraude")

un_stylo_rouge = StyloCouleur("rouge")
un_stylo_rouge.print("rouge cerise")

un_stylo_jaune = StyloCouleur("jaune") 
            

S=Stylo()
for i in range(19):
    S.print("10000")

print(S.Encre)

S.print("ArnaudLe")
print(S.Encre)


un_stylo = StyloCouleur("vert")
for i in range(5):
  un_stylo.print("seize caractères")
  
  
#SC=StyloCouleur()
#SC.Encre
