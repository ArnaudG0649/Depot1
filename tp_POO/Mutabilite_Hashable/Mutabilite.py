from copy import copy,deepcopy


def is_mutable(x,y):
  print(f'{type(x).__name__} is {"mutable" if x is y else "immutable"}')

D={"A":25, "B":30}
E=D
E["C"]=30
is_mutable(D,E)

class Pomme : pass

p1=Pomme()
p1.col="rouge"
p2=p1
p2.col='jaune'

is_mutable(p1,p2)

a=(1,2)
b=a
b+=(3,4)
is_mutable(a, b)


L=[1,2,[3,4]]
M=copy(L)
