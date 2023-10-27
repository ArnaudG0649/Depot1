import turtle
import Forme

def main():
    turtle.Screen()
    turtle.Screen().setup(640, 480, 100, 100)

    try:
        turtle.reset()
        T1=Forme.Triangle(g=(50,50),l=100,debug=True)
        T1.trace()
        C1=Forme.Cercle(g=(-50,-50),l=100,debug=True)
        C1.trace()
        C2=Forme.Carre(g=(-50,-50),l=100,c="blue")
        C2.trace()
        T2=Forme.Triangle(g=(-50,-50),l=100,e=2,c="lime")
        T2.trace()
    finally:
        # turtle.exitonclick()
        pass

def main2():
    turtle.Screen()
    turtle.Screen().setup(640, 480, 100, 100)

    try:
        turtle.reset()
        T1=Forme.Triangle(g=(50,50),l=100,debug=True)
        C1=Forme.Cercle(g=(-50,-50),l=100,debug=True)
        C2=Forme.Carre(g=(-50,-50),l=100,c="blue")
        T2=Forme.Triangle(g=(-50,-50),l=100,e=2,c="lime")
        
        gribouilli=Forme.Dessin([T1,C1,C2,T2])
        gribouilli.trace()

    finally:
        # turtle.exitonclick()
        pass



if __name__ == "__main__":
    #main
    main2()



