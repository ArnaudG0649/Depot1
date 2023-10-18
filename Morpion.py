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
        def pvainqueur(M,pion): #Cette fonction vérifie que le pion rentré en argument est le pion gagnant.
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
 
    def vainqueurnom(self) : #Similaire à la fonction vainqueur() mais renvoie le nom du joueur gagnant.
        def pvainqueur(M,pion): #Cette fonction vérifie que le pion rentré en argument est le pion gagnant.
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
        if pvainqueur(self.jeu,"O") : 
            for J in ListeJoueurs.items() :
                if J[1].pion=="O" : return J[0] 
        elif pvainqueur(self.jeu,"X") : 
            for J in ListeJoueurs.items() :
                if J[1].pion=="X" : return J[0] 
        else : return None
        

jeu = TicTacToe()
print(jeu)
 
jeu.place(1,1,'O')
print(jeu)

jeu.place(2,3,'X')
print(jeu)


class Joueur:
    global ListeJoueurs
    global ListePion
    ListeJoueurs={} #Pour que les instances des joueurs soient utilisables par la fonction vainqueurnom()
    ListePion=[]
    
    def __init__(self,jeu,nom,pion):
        self.nom=nom
        if pion in ListePion : raise NameError("Pion déjà pris") #Le but de cette ligne est de faire en sorte  
        else :                                                   #que les deux joueurs n'aient pas le même pion.
            self.pion=pion
            ListePion.append(pion)
        self.jeu=jeu
        ListeJoueurs[self.nom]=self
                        
    def joue(self,i,j):
        self.jeu.place(i,j,self.pion)

jeu = TicTacToe()
print(jeu)

ListePion=[] #À réexecuter à chaque nouvelle partie pour permettre l'attribution de pions aux joueurs.
bob = Joueur(jeu,nom='Bob',pion='O')
alice = Joueur(jeu,nom='Alice',pion='X')

bob.joue(1,1)
alice.joue(1,3)
print(jeu)

print(jeu.vainqueur())

bob.joue(3,3)
alice.joue(2,2)
bob.joue(3,1)
alice.joue(3,2)
bob.joue(2,1)
print(jeu)

print(jeu.vainqueur())
print(jeu.vainqueurnom())







