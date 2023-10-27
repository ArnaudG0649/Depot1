import math

class Instant:
    def __init__(self,h=0,m=0,s=0):
        self.hh = h + m//60 + s//3600
        self.mm = m%60 + (s%3600)//60
        self.ss = s%60

    def __str__(self):
        if self.hh == 0:
            if self.mm == 0:
                return f"{self.ss}s"
            if self.ss == 0:
                return f"{self.mm}mn"
            return f"{self.mm}mn {self.ss}s"
        if self.mm == 0:
            if self.ss == 0:
                return f"{self.hh}h"
            return f"{self.hh}h {self.ss}s"
        if self.ss == 0:
            return f"{self.hh}h {self.mm}mn"
        return f"{self.hh}h {self.mm}mn {self.ss}s"


if __name__=="__main__":
    instant1 = Instant(h=1,m=10,s=30)
    print(instant1)      # 1h 10mn 30s

    instant2 = Instant(m=10,s=30)
    print(instant2)      # 10mn 30s

    instant3 = Instant(m=10)
    print(instant3)      # 10mn

    instant4 = Instant(h=1,m=90)
    print(instant4)      # 2h 30mn

 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    