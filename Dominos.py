class Domino: 
    
    def __init__(self,p,f):
        if f-p>1 or p-f>1 : raise RuntimeError("Domino invalide")
        else : 
            self.p=p
            self.f=f
            
    def __str__(self):
        return f"{self.p}:{self.f}"

    def retourne(self):
        self.p,self.f=self.f,self.p
        
    def __add__(self,d):
        c=Chaine()
        c+=self
        c+=d
        return c

        

d1 = Domino(3,4)
print(d1)         # 3:4

d2 = Domino(2,3)
print(d2)         # 0:0

d3 = Domino(6,7)  # Erreur

d1.retourne()
print(d1)         # 4:3

d1.retourne()
print(d1)   


class Chaine:
    
    def __init__(self):
        self.L=[]
        
    def __iadd__(self,d):
        if len(self.L)>1 : 
            if not(self.L[-1].f in [d.p,d.f]) : raise RuntimeError("Nouveau domino invalide")
            elif d.p==self.L[-1].f : self.L.append(d)
            elif d.f==self.L[-1].f : 
                d.retourne()
                self.L.append(d)     
        elif len(self.L)==1 : 
            if not(self.L[0].p in [d.p,d.f]) and not(self.L[0].f in [d.p,d.f]) : 
                raise RuntimeError("Nouveau domino invalide")
            else :
                c1=self.L[0].p==d.p
                c2=self.L[0].p==d.f
                c3=self.L[0].f==d.p
                c4=self.L[0].f==d.f
                if c1 : self.L[0].retourne() ; self.L.append(d) 
                if c2 : self.L[0].retourne() ; d.retourne() ; self.L.append(d) 
                if c3 : self.L.append(d) 
                if c4 : d.retourne() ; self.L.append(d) 
        elif self.L==[]:
            self.L.append(d)
        return self

        
    def __str__(self):
        if self.L!=[] :
            s=f"{self.L[0].p}:{self.L[0].f}"
            for d in self.L[1:] : 
                s+=f"-{d.p}:{d.f}"
            return s
        else : return "" 

c=Chaine()
c+=d1
print(c)
c+=d2
c+=d3
print(c)

print(d1+d2)

d4=Domino(1,2)
c+=d4
c.L[-1].f
[d4.p,d4.f]

e34=Domino(3,4)
e43=Domino(4,3)
e32=Domino(3,2)
e23=Domino(2,3)

print(e34+e32)
print(e34+e23)
print(e43+e32)
print(e43+e23)




