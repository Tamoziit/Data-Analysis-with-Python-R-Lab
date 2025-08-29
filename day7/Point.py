import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def cartesian_to_polar(self):
        r = ((self.x * self.x) + (self.y * self.y)) ** 0.5
        if self.x == 0:
            theta = math.pi / 2
        else:
            theta = math.atan(self.y / self.x)
            
        print(f"Cartesian ({self.x}, {self.y}) = Polar ({r}, {theta})")
        
    def distance(self, ob):
        dist = ((self.x - ob.x) ** 2.0 + (self.y - ob.y) ** 2.0) ** 0.5
        print(f"Distance between ({self.x}, {self.y}) & ({ob.x}, {ob.y}) = {dist} units")
        
    def translate(self, del_x, del_y):
        self.x += del_x
        self.y += del_y
        print(f"New Point after translation = ({self.x}, {self.y})")
        
def main():
    x1, y1 = eval(input("Enter coordinates of 1st Point: "))
    x2, y2 = eval(input("Enter coordinates of 2nd Point: "))
    
    ob1 = Point(x1, y1)
    ob2 = Point(x2, y2)
    
    ob1.cartesian_to_polar()
    ob2.cartesian_to_polar()
    ob1.distance(ob2)
    ob1.translate(2, 3)
    ob2.translate(2, 3)
    
main()