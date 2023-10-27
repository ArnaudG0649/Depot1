import turtle
import math
#import Triangle
#import Carre
#import Cercle

class Forme : 
    def __init__(self,g,l,c="black",e=1,debug=False):
        self.g=g
        self.l=l
        self.c=c
        self.e=e
        self.debug=debug

    def _goto_G(self) :
        g=self.g
        debug=self.debug
        
        turtle.penup()
        turtle.goto(g)

        if debug: 
            turtle.pencolor("red")
            turtle.pensize(1)
            turtle.pendown()
            
    def trace(self):
        
        c=self.c
        e=self.e
        
        self._goto_G()
        self._goto_edge()
        turtle.pencolor(c)
        turtle.pensize(e)
        turtle.pendown()
        self._trace()
        
        
class Triangle(Forme) :

    def _goto_edge(self):
        
        l=self.l

        turtle.setheading(90)
        turtle.forward(l*(math.sqrt(3)/2)*2/3)        
        
    def _trace(self):
        
        l=self.l
        
        turtle.setheading(-120)
        turtle.forward(l)
        turtle.setheading(0)
        turtle.forward(l)
        turtle.setheading(120)
        turtle.forward(l)
        
        
class Carre(Forme) :

    def _goto_edge(self):
        
        l=self.l
        
        turtle.setheading(-135)
        turtle.forward(l*(math.sqrt(2)/2))
    
    def _trace(self):
        
        l=self.l
        
        turtle.setheading(0)
        turtle.forward(l)
        turtle.setheading(90)
        turtle.forward(l)
        turtle.setheading(180)
        turtle.forward(l)
        turtle.setheading(270)
        turtle.forward(l)
             

class Cercle(Forme) : 

    def _goto_edge(self):
        
        l=self.l
        
        turtle.setheading(-90)
        turtle.forward(l/2)
    
    def _trace(self):
        
        l=self.l
        
        turtle.setheading(0)
        turtle.circle(l/2)
        
        
class Dessin():
    
    def __init__(self,L=[]):
        self.L=L
        
    def add(self,F):
        self.L.append(F)
        
    def trace(self):
        for F in self.L : 
            F.trace()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        