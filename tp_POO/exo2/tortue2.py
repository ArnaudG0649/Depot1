#1

class Tortue : 
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def localise(self):
        return(self.x,self.y)
    
    def avance(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy

ma_tortue = Tortue(5,0)
print(ma_tortue.localise())
ma_tortue.avance(10,10)
print(ma_tortue.localise()) 

#2
import numpy as np
import numpy.random as npr

class Tortue : 
    def __init__(self,nom,X,vmax=npr.choice(range(2,11))):
        self.X=X
        self.nom=nom
        self.vmax=vmax
    
    def localise(self):
        return(self.nom,self.X)
    
    def avance(self,dX='a'):
        if dX=='a' :
            dX=(npr.choice(np.arange(0,self.vmax+1)),0)
        self.X=list(self.X)    
        self.X[0]=self.X[0]+dX[0]
        self.X[1]=self.X[1]+dX[1]
        self.X=tuple(self.X)

T=Tortue("Jamy",(3,2))
print(T.vmax)
print(T.localise())

T.avance()
print(T.localise())

T.avance((0,30))
print(T.localise())



tortues = []   # tortues au départ

for t in range(5):
  tortues.append(Tortue(f"tortue{t}",(0,0)))

print("1, 2, 3 partez !")
for step in range(100):
  print(f"{step=}")
  for t in tortues:
    t.avance()
    print(t.localise())
    
 #3  
class Course :
    def __init__(self,liste=[]):
        self.liste=liste
    
    def enregistre(self,Tortue):
        self.liste.append(Tortue)
        
    def run(self):
        print("1, 2, 3 partez !")
        for step in range(100) :
            print(f"{step=}")
            for t in self.liste :
                t.avance()
                print(t.localise())
        
la_course = Course()
for t in range(5):
  la_course.enregistre(Tortue(f"tortue{t}",(0,0)))
la_course.run()


























