class Point:
    """Represents a point in 2D space.
       Has parameters x and y."""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self: "Point") -> str:
        return 'x = %.5f ,y = %.5f' % (self.x, self.y)

    def __add__(self, other: "Point") -> "Point":
        if isinstance(other, Point):
            return(Point(self.x + other.x, self.y + other.y))
        elif isinstance(other, tuple):
            return(Point(self.x + other[0], self.y + other[1]))
        else:
            raise TypeError('Invalid object in Point __add__')
        
    def __radd__(self, other):
        return self.__add__(other)
        

p1 = Point(31.2, 5.0)
print(p1)
p2 = Point(11.0, -6.2)
print(p2)
print(p1 + p2)
p3 = Point(-4.0, 33.0)
print(p1+p2+p3)
#total = sum([p1, p2, p3])