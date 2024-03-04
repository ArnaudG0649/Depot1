#!/bin/env python3

import re
import os 
import os.path as osp 
 
os.getcwd()
os.listdir(os.getcwd()) 
#osp.join
#osp.isfile(f)
#osp.basename(os.getcwd())

with open('words.txt','r') as file : 
    for l in file :
        print(l)
        found=re.match(r"t",l) #Match : Occurence AU DEBUT
        found2=re.search(r"t",l) #Search : Occurence n'importe où
        print(bool(found),bool(found2))
        

def Regexligne(regex,ligne) : 
    if bool(re.search(regex,ligne)) : print(ligne)
    
def Regexfichier(regex,fichier) : 
    with open(fichier,'r') as file : 
        for l in file : Regexligne(regex,l)
    
##re2
#1
with open('hosts','r') as file : 
    for l in file : 
        Regexligne(r'::',l)

#2
for fichier in os.listdir(osp.join(os.getcwd(),"profile.d")) :
    print("   ",fichier)
    with open(osp.join("profile.d",fichier),'r') as file :
        for l in file :
            Regexligne(r'\$USER',l)
            
##re3 
#1
Regexfichier(r'ub',"re3_10.txt")
#2
Regexfichier(r'[abcde]{5}',"re3.txt")
#3
Regexfichier(r'b.*b',"re3.txt")


##re4
Regexfichier(r'[^ ]{20}','words.txt')

##re5
Regexfichier(r'[dt]','re3_10.txt')

##re6
Regexfichier(r'[dt]','words.txt')
Regexfichier(r'[dt]','words.txt')
Regexfichier(r'[dt]','words.txt')




