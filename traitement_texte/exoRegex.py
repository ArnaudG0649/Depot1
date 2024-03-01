#!/bin/env python3

import re
import os 
 
with open('words.txt','r') as file : 
    for l in file :
        print(l)
        found=re.match(r"t",l) #Match : Occurence AU DEBUT
        found2=re.search(r"t",l) #Search : Occurence n'importe où
        print(bool(found),bool(found2))
        

def Regexligne(regex,ligne) : 
    if bool(re.search(regex,l)) : print(ligne)
    
##re2
#1
with open('hosts','r') as file : 
    for l in file : 
        Regexligne(r'::',l)

#2
