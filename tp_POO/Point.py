class Point: pass

def examine(Point):
    return f"Point {Point.nom}({Point.x},{Point.y})"
    
def deplace(p,D):
    p.x+=D[0]
    p.y+=D[1]
    return(p)

