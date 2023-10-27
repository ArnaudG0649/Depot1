import turtle
import Forme

class Cercle(Forme.Forme) : 

    # def trace(self) : 
    #     self._goto_G()
        
    #     l=self.l
    #     c=self.c
    #     e=self.e
        
    #     turtle.setheading(-90)
    #     turtle.forward(l/2)

    #     turtle.pencolor(c)
    #     turtle.pensize(e)
    #     turtle.pendown()
    #     turtle.setheading(0)
    #     turtle.circle(l/2)
        
    def _goto_edge(self):
        
        l=self.l
        
        turtle.setheading(-90)
        turtle.forward(l/2)
    
    def _trace(self):
        
        l=self.l
        c=self.c
        e=self.e
        
        turtle.pencolor(c)
        turtle.pensize(e)
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(l/2)
        