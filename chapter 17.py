class Point:
    """Represents a point in 2D space.
       Has parameters x and y."""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self: "Point") -> str:
        return 'x = %.5f ,y = %.5f' % (self.x, self.y)

    def __add__(self, other: "Point") -> "Point":
        p_add = Point(self.x + other.x, self.y + other.y)
        return p_add
        

p1 = Point(31.2, 5)
print(p1)
p2 = Point(11, -6.77)
print(p2)
print(p1 + p2)