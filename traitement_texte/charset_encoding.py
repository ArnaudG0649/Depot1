#!/bin/env python3

import sys, re, collections, encodings

##ch1

print(" ", end="   ")
for i in range(8):
    print(f"{i:1x}", end="   ")
print()

for i in range(16):
    print(f"{i:1x}: ", end=" ")
    for j in range(8):
        code = j*16+i
        car = chr(code)
        if not car.isprintable():
          car=" "
        print(car, end="   ")
    print()


#ch3
s=b"\x41, \x42, \x43, \xE9, \xE8, \xC5"
s.decode(encoding="iso8859-3")


#b'f"\x{i}'.decode(encoding="iso8859-3")

##ch5

def charset(codec):
    print(" ", end="   ")
    for i in range(16):
        print(f"{i:1x}", end="   ")
    print()
    
    for i in range(16):
        print(f"{i:1x}: ", end=" ")
        for j in range(16):
            code = j*16+i
            b = bytes([code])
            car = b.decode(encoding=codec)
            if not car.isprintable():
              car=" "
            print(car, end="   ")
        print()
        
charset("latin1")


##ch6

def charset(codec1,codec2):
    print(" ", end="   ")
    for i in range(16):
        print(f"{i:1x}", end="   ")
    print()
    
    for i in range(16):
        print(f"{i:1x}: ", end=" ")
        for j in range(16):
            code = j*16+i
            b = bytes([code])
            car1 = b.decode(encoding=codec1)
            car2 = b.decode(encoding=codec2)
            if not car2.isprintable() or car1==car2:
              car2=" "
            print(car2, end="   ")
        print()
        
charset("iso8859-1","iso8859-15")

##ch7
fn = input("file name: ")
with open(fn, "r", encoding="iso8859-1") as f:
    char = f.read(1)
    while char:
        print(f"{char}",end=" ")
        char = f.read(1)


import unicodedata
unicodedata.name('/')
unicodedata.lookup('solidus')
unicodedata.lookup('LEFT CURLY BRACKET')
unicodedata.category('A')        # Letter uppercase
unicodedata.category('a')        # Letter lowercase
unicodedata.category('9')        # Numeric decimal
unicodedata.category('€')        # Symbol currency
unicodedata.numeric('9')
unicodedata.numeric('a')


#uc9

unicodedata.name("\u2160")
unicodedata.numeric("\u2160")

print("\u2160")

unicodedata.name("\u0041")
unicodedata.name("\u0391")
















