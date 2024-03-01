#!/bin/env python3

import re

L=[]
with open("file","r") as f : 
    for l in f:
        L.append(l)


def Conditions(s):
    B=False
    if bool(re.search(r".*=.*",s))
    
BL=[False for i in L]
for l in L :
    
    
##########################Correction##########################
#!/bin/env python3                                                                                            
                                                                                                              
import re                                                                                                     
                                                                                                              
nbl=0                                                                                                         
with open("fichier","r") as f:                                                                               
  for line in f:                                                                                             
     nbl += 1                                                                                                 
     if re.search("^[ \t]*$",line):                                                                           
       continue                                                                                               
                                                                                                             
     if re.search("^[ \t]*#",line):                                                                           
       continue                                                                                               
                                                                                                      
     if not re.search("^[a-zA-Z][a-zA-Z0-9_]* *= *",line):                                                    
       print(f"erreur en ligne {nbl} : {line}\n")                                                             
                               