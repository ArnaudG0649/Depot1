from Complex import Complex
from Cercle import Cercle
import math

z=Complex(1,2)
print(z.x,z.y)


u=z

u.initialise(1,-2)
u.y

v=z.conjugue()
v.y

un_cercle = Cercle()
un_cercle.initRayon(10)
print(un_cercle.circonference())
print(un_cercle.surface())



