class S(str) :
    def __init__(self,string) : 
        self.string=string
        
    def __getitem__(self,i) : 
        if type(i)==int : 
            return self.string[i]
        elif type(i)==str : 
            return self.string.find(i)
        
superstring=S("Bonjour")
superstring[0]
superstring["B"]

class Diviseurs(int) :
    def __init__(self,val):
        self.val=val
        self.i=0
        
    def __getitem__(self,i) :
        if i>self.val : 
            raise IndexError("Valeur supérieure à l'entier")
        elif i>0 :
            return self.val%i==0
        else : 
            return False
        
        
    
d15=Diviseurs(15)
d15[3]
d15[7]

for i in d15:
    print(i,end=" ") # False True True True True False True False False False False False True

for i,d in enumerate(Diviseurs(100)):
    if d:
        print(i,end=" ") # 1 2 4 5 10 20 25 50 100
        
class Diviseurs():
    def __init__(self,k):
        self.k = k

    def __iter__(self):
      return self.It(self)

    class It():
      def __init__(self,d):
        self.diviseurs = d
        self.i = 0

      def __next__(self):
        if self.i == self.diviseurs.k:
          raise StopIteration()

        self.i += 1
        while self.diviseurs.k % self.i != 0 :
          self.i += 1
        return self.i

      def __iter__(self):
        return self

  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    