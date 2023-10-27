import math

def initialise(self,reel,imag):
    self.x = reel
    self.y = imag

class Complex:
    def __init__(self,reel,imag):
        self.x = reel
        self.y = imag
        
    def __str__(self):
        if self.y==0 : 
            return f"{self.x}"
        elif self.x==0:
            return f"{self.y}i"
        else :
            return f"{self.x}+{self.y}i"
        
    def initialise(self,reel,imag):
        self.x = reel
        self.y = imag
        
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def argument(self):
        return math.atan(self.y/self.x)
    
    def conjugue(self):
        conj=Complex()
        initialise(conj,self.x,-self.y)
        return conj
        
if __name__=="__main__":                                                                                      
    pass
           

