class C:
    nb_instances = 0

    def __init__(self,x,y):
      self.x = x
      self.y = y
      print(f"C({x},{y}) créé \t(#{id(self)})", end=" - ")
      C.mod_instance(1)

    def __del__(self):
      print(f"C({self.x},{self.y}) détruit \t(#{id(self)})", end=" - ")
      C.mod_instance(-1)

    @classmethod
    def mod_instance(cls,n):
      cls.nb_instances += n
      print(cls.how_many_instances())

    @classmethod
    def how_many_instances(cls):
      return f"instances vivantes: {cls.nb_instances}"



z1 = C(1,2)
z2 = C(1,-2)
z1 = C(-1,-2)
del z2
z3 = z4 = C(0,0)
z5 = C(1,1)
del z4
print("fin de programme")
