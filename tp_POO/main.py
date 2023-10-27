import Point,Cercle

p1 = Point.Point()

p1.nom = "A"
p1.x = 1
p1.y = 2
print(Point.examine(p1))
print(type(p1).__name__)


p2 = Point.Point()
p2.nom = 'B'
p2.x = 0
p2.y = -1
print(Point.examine(p2))
print(type(p2).__name__)


p3=Point.deplace(p1,(1,1))

print(Point.examine(p3))

mon_cercle = Cercle.Cercle()
mon_cercle.nom = "c"
mon_cercle.centre = p1
mon_cercle.rayon = 2.5
print(Cercle.examine(mon_cercle))

Cercle.deplace(mon_cercle,p2)    # déplace mon_cercle en (0,-1)
print(Cercle.examine(mon_cercle))

mon_autre_cercle = Cercle.copie(mon_cercle)
print(Cercle.examine(mon_autre_cercle))


mon_cercle_etendu = Cercle.CercleEtendu()
mon_cercle_etendu.nom = "c"
mon_cercle_etendu.centre = p1
mon_cercle_etendu.rayon = 2.5
mon_cercle_etendu.epaisseur = 1.1