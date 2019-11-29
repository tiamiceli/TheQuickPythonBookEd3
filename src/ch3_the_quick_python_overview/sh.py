"""sh module. Contains clsses Shape, Square and Circle"""
class Shape:
    """Shape class: has method move"""
    def __init__(self, x, y): # constructor!
        self.x = x # initialize instance variables!
        self.y = y
    def move(self, deltaX, deltaY): # methods / functions
        self.x = self.x + deltaX
        self.y = self.y + deltaY
class Square(Shape): # inherits!
    """Square Class: inherits from Shape"""
    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y) # must call initializer of base class!
        self.side = side
class Circle(Shape): #inherits!
    """Circle Class: inherits from Shape and has method area"""
    pi = 3.14159
    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y) # must call initializer of base class!
        self.radius = r
    def area(self):
        """Circle area method: returns the area of the circle."""
        return self.radius * self.radius * self.pi
    def __str__(self): # used for the print function!
        return "Circle of radius %s at coordinates (%d, %d)"\
            % (self.radius, self.x, self.y)