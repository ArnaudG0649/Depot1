import math

class Fraction:
    def __init__(self,n,d=1):
        self.n=n
        self.d=d
    
    def reduire(self):
        if self.d==0:
          raise ZeroDivisionError(f"problème pour réduire la Fraction({self.n},{self.d}) !")
        pgcd = math.gcd(self.n,self.d)
        self.n //= pgcd
        self.d //= pgcd
        return self
        
    def __str__(self):
        n=self.n
        d=self.d
        if n==0 : return "0"
        if d==1 : return f"{n}"
        elif d==-1 : return f"{-n}"
        if d<0 : return f"{-n}/{-d}"
        else : return f"{n}/{d}"
    
    def inverse(self):
        return Fraction(self.d,self.n)
    

    def __add__(self,b):
        if isinstance(b, Fraction) : 
            na,da,nb,db=self.n,self.d,b.n,b.d
            return Fraction(na*db+nb*da,da*db)
        elif isinstance(b, int) : 
            na,da=self.n,self.d
            return Fraction(na+b*da,da)

    def __radd__(self,b):
        if isinstance(b, int) : 
            na,da=self.n,self.d
            return Fraction(na+b*da,da)    

    def __neg__(self):
        return Fraction(-self.n,self.d)
    
    def __sub__(self,b):
            return self+(-b)
        
    def __rsub__(self,b):
        if isinstance(b, int) : 
            return b+(-self)
        
    def __mul__(self,b):
        if isinstance(b, Fraction) : 
            na,da,nb,db=self.n,self.d,b.n,b.d
            return Fraction(na*nb,da*db)
        elif isinstance(b, int) : 
            na,da=self.n,self.d
            return Fraction(na*b,da)
        
    def __rmul__(self,b):
        if isinstance(b, int) : 
            na,da=self.n,self.d
            return Fraction(na*b,da)  
        
    def __truediv__(self,b):
        if isinstance(b, Fraction) : 
            na,da,nb,db=self.n,self.d,b.n,b.d
            return Fraction(na*db,da*nb)
        elif isinstance(b, int) : 
            na,da=self.n,self.d
            return Fraction(na,da*b)
        
    def __rtruediv__(self,b):
        if isinstance(b, int) : 
            na,da=self.n,self.d
            return Fraction(b*da,na)      
        
    def __iadd__(self,b):
                return self+b

    def __ge__(self,b):
        if isinstance(b, Fraction) : 
            na,da,nb,db=self.n,self.d,b.n,b.d
            return na/da>=nb/db
        elif isinstance(b, int) : 
            na,da=self.n,self.d
            return na/da>=b
        
    def __rge__(self,b):
        if isinstance(b, int) : 
            na,da=self.n,self.d
            return b>=na/da 

"""
f = Fraction(15,27)
print(f)                  # 15/27
f2 = f.inverse()
print(f2)                 # 27/15


print(Fraction(2,3))     # écrit 2/3
print(Fraction(-2,3))    # écrit -2/3
print(Fraction(2,-3))    # écrit -2/3
print(Fraction(-2,-3))   # écrit 2/3
print(Fraction(2,1))    
    

print(Fraction(15,0)) 

b=Fraction(1,4)
a=Fraction(2,3)
#print(a+b)
#print(-(1-a),a-1)
#print(a/b,2/a,a/2,a/3)
#a+=b
#print(a)
#b+=1
#print(b)
#n=3
#n+=b
#print(n)
#print(a*0)
#z=Fraction(0)
#print(z)

a>=b
b>=a
a>=1

p = Fraction(9,15)
q = Fraction(2,3)

print(p+q)
print((p+1)/(p-1))
print(-p)

if p>=q:
  p += 1

p += q
print(2*p)
"""