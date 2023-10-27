0b1011 
f"{192:b}"
class adressIP : 
    def __init__(self,o1,o2,o3,o4):
        self.o1=o1
        self.o2=o2
        self.o3=o3
        self.o4=o4
        
    def classe(self):
      if self.o1 & 0b10000000 == 0b00000000:
          self.classe = "A"
      elif self.o1 & 0b11000000 == 0b10000000:
          self.classe = "B"
      elif self.o1 & 0b11100000 ==0b11000000:
          self.classe = "C"
    
      return self.classe
    
    def reseau(self):
      pass
    
    def equipement(self):
      pass

if __name__=="__main__":
  ip1 = adressIP(192,168,1,1)
  ip2 = adressIP(172,20,21,19)
  ip3 = adressIP(10,1,1,1)

  print(f"{ip1.classe()=}")
  print(f"{ip2.classe()=}")
  
  