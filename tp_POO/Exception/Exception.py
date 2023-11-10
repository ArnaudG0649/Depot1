# l = [1,2,3,4,5,6,7,8]

# def f(i):
#     f(l[i])

# def main():
#     f(0)

# if __name__ == "__main__":
#     main()



# import math

# def g(x):
#     if math.sqrt(x)>2:
#         f(x-10)
#     else:
#         return x

# def f(x):
#     g(x)

# def main():
#     f(45)

# if __name__ == "__main__":
#     main()
    
import Fraction2 as Fr2
import Fraction3 as Fr3

def calc(a,b):
  try:                              
    r1 = Fr2.Fraction(a,b)
    r2 = Fr2.Fraction(b,a)
  except MemoryError:    
    print("une division par 0 a été détectée")
    exit(1)
  return (r1+r2).reduire()

if __name__ == "__main__":
    a = int(input("entrer un premier entier :"))
    b = int(input("entrer un second entier :"))
    print(f"calc({a},{b})={calc(a,b)}")


