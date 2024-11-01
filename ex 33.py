class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y     
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
        
       
    

p1 = Point(3,4)
p2 = Point(3,4)
print(hash(p1), hash(p2), sep='\n')
print(hash(p1) == hash(p2))
d={}
d[p1]=p1.x
print(d.items())
d[p2] = p2.y
print(d.items())