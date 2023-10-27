import turtle
import math
import Forme

class Triangle(Forme.Forme) :

    # def trace(self) : 
    #     self._goto_G()
        
    #     l=self.l
    #     c=self.c
    #     e=self.e

    #     turtle.setheading(90)
    #     turtle.forward(l*(math.sqrt(3)/2)*2/3)
    
    #     turtle.pencolor(c)
    #     turtle.pensize(e)
    #     turtle.pendown()
    #     turtle.setheading(-120)
    #     turtle.forward(l)
    #     turtle.setheading(0)
    #     turtle.forward(l)
    #     turtle.setheading(120)
    #     turtle.forward(l)
        
    def _goto_edge(self):
        
        l=self.l

        turtle.setheading(90)
        turtle.forward(l*(math.sqrt(3)/2)*2/3)        
        
    def _trace(self):
        
        l=self.l
        c=self.c
        e=self.e
        
        turtle.pencolor(c)
        turtle.pensize(e)
        turtle.pendown()
        turtle.setheading(-120)
        turtle.forward(l)
        turtle.setheading(0)
        turtle.forward(l)
        turtle.setheading(120)
        turtle.forward(l)
        
        
# def main():
#     turtle.Screen()
#     turtle.Screen().setup(640, 480, 100, 100)

#     try:
#         turtle.reset()
#         Triangle(g=[50,50],l=100,debug=True)
#         Triangle(g=[-50,-50],l=100,e=2,c="lime")
#     finally:
#         # turtle.exitonclick()
#         pass

# if __name__ == "__main__":
#     main()
