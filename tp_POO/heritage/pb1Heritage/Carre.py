import turtle
import math 
import Forme

class Carre(Forme.Forme) :

    # def trace(self) : 
    #     self._goto_G()
        
    #     l=self.l
    #     c=self.c
    #     e=self.e
        
    #     turtle.setheading(-135)
    #     turtle.forward(l*(math.sqrt(2)/2))

    #     turtle.pencolor(c)
    #     turtle.pensize(e)
    #     turtle.pendown()
    #     turtle.setheading(0)
    #     turtle.forward(l)
    #     turtle.setheading(90)
    #     turtle.forward(l)
    #     turtle.setheading(180)
    #     turtle.forward(l)
    #     turtle.setheading(270)
    #     turtle.forward(l)
        
    def _goto_edge(self):
        
        l=self.l
        
        turtle.setheading(-135)
        turtle.forward(l*(math.sqrt(2)/2))
    
    def _trace(self):
        
        l=self.l
        c=self.c
        e=self.e
        
        turtle.pencolor(c)
        turtle.pensize(e)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(l)
        turtle.setheading(90)
        turtle.forward(l)
        turtle.setheading(180)
        turtle.forward(l)
        turtle.setheading(270)
        turtle.forward(l)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        