#!/bin/env python3  

# with open('data', 'w') as mon_fichier: 
#   for i in range(-10,10):
#       print(1/i, file=mon_fichier) 

# mon_fichier = open("data", "w")
# for i in range(-10,10):
#     print(1/i, file=mon_fichier)
# mon_fichier.close()


class Balise : 
    
    def __enter__(self) : 
        print("<balise>")
        
    def __exit__(self,type,value,traceback) : 
        print("<balise>")
        
with Balise():
    print("Hello")
    
class Balise:                                                                                              
    niveau = 0                                                                                                
    def __init__(self,s):                                                                                      
        self.s = s                                                                                               
                                                                                                             
    def __enter__(self):                                                                                    
        Balise.niveau += 1                                                                                     
        print(" "*Balise.niveau,f"<{self.s}>")                                                                   
        return self                                                                                            
                                                                                                            
    def __exit__(self,type,value,traceback):                                                                   
        print(" "*Balise.niveau,f"</{self.s}>")                                                                 
        Balise.niveau -= 1                                                                                     
                                                                                                             
    def print(self,msg):                                                                                       
        print(" "*(Balise.niveau+1),msg)       
        

from time import time 
    

t=time()

class Top:
    def __enter__(self) :
        self.t0=time.time()
        self.cm
    
    def __exit__
    
    
    
    
    
    
    
    
    
    
    
    