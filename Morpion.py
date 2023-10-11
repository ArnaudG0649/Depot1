#Q1

class TicTacToe:
    def __init__(self):
        self.jeu = {}
        for i in range(1,4):
            for j in range(1,4):
                self.jeu[(i,j)] = "."
                
    def __str__(self):
        M=self.jeu
        C=''
        for i in range(1,4):
            C+=(f"    {M[(i,1)]} {M[(i,2)]} {M[(i,3)]}\n")
        return C
    
    def place(self,i,j,c) :
        self.jeu[(i,j)] = c
        
    def vainqueur(self) :
        def pvainqueur(M,pion):
            v=False
            for i in range(1,4): #Les lignes
                alignement=True
                for j in range(1,4):
                    if M[(i,j)]!=pion : alignement=False
                if alignement : v=True
            for j in range(1,4): #Les colonnes
                alignement=True
                for i in range(1,4):
                    if M[(i,j)]!=pion : alignement=False
                if alignement : v=True
            alignement=True
            for i in range(1,4): #diagonale
                if M[(i,i)]!=pion : alignement=False
            if alignement : v=True
            alignement=True
            for i in range(1,4): #anti-diagonale
                if M[(4-i,i)]!=pion : alignement=False
            if alignement : v=True
            return v
        if pvainqueur(self.jeu,"O") : return "O"
        elif pvainqueur(self.jeu,"X") : return "X"
        else : return None
        
    def vainqueur(self) :
        def pvainqueur(M,pion):
            v=False
            for i in range(1,4): #Les lignes
                alignement=True
                for j in range(1,4):
                    if M[(i,j)]!=pion : alignement=False
                if alignement : v=True
            for j in range(1,4): #Les colonnes
                alignement=True
                for i in range(1,4):
                    if M[(i,j)]!=pion : alignement=False
                if alignement : v=True
            alignement=True
            for i in range(1,4): #diagonale
                if M[(i,i)]!=pion : alignement=False
            if alignement : v=True
            alignement=True
            for i in range(1,4): #anti-diagonale
                if M[(4-i,i)]!=pion : alignement=False
            if alignement : v=True
            return v
        if pvainqueur(self.jeu,"O") : return "O"
        elif pvainqueur(self.jeu,"X") : return "X"
        else : return None
        
        


jeu = TicTacToe()
print(jeu)
 
jeu.place(1,1,'O')
print(jeu)

jeu.place(2,3,'X')
print(jeu)

#Q2

class Joueur:
    def __init__(self,jeu,nom,pion):
        self.nom=nom
        self.pion=pion
        self.jeu=jeu
        
    def joue(self,i,j):
        self.jeu.place(i,j,self.pion)
        
bob = Joueur(jeu,nom='Bob',pion='O')
alice = Joueur(jeu,nom='Alice',pion='X')
print(jeu)
bob.joue(1,1)
print(jeu)
alice.joue(1,3)
print(jeu)
bob.joue(3,3)
alice.joue(2,2)
bob.joue(3,1)
alice.joue(3,2)
bob.joue(2,1)
print(jeu)

jeu.vainqueur()

jeuX= TicTacToe()
for j in range(1,3):
    jeuX.place(2,j,"X")

print(jeuX)

print(jeuX.vainqueur())


