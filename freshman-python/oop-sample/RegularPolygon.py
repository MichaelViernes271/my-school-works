import math

class RegularPolygon:
    """n sided equilateral and equiangular polygon"""

    n = 0
    def __init__(self, n=3, side=1, x=0, y=0):
      self.__n = int(n)
      self.__side = float(side)
      self.__x = float(x)
      self.__y = float(y)
    
    @classmethod
    def polygonN(cls):
        cls.n += 1
        return cls.n
        
    # accessors and mutators for fields
    def getN(self):
        return self.__n

    def getSide(self):
        return float(self.__side)

    def getX(self):
        return self.__x

    def getY(self):
        return float(self.__y)

    def setN(self):
        self.__n = n

    def setSide(self):
        self.__side = float(side)

    def setX(self):
        self.__x = float(x)

    def setY(self):
        self.__y = float(y)

    # solves the perimeter of a polygon
    def getPerimeter(self):
        return str(self.getSide() * self.getN())
        
    def getArea(self):
        formula1 = self.getN() * math.pow(self.getSide(), 2)
        formula2 = 4 * math.tan(math.pi/self.getN())
        return formula1 / formula2
    
    def print_result(self):
        print(f"""\
Polygon: {RegularPolygon.polygonN()}
n-side = {self.getN()}
side length = {self.getSide()}
area = {round(self.getArea(),2)}
perimeter = {self.getPerimeter()}
x-coor = {self.getX()}
y-coor = {self.getY()}
""")    
def main():
    # testing the module
    self = RegularPolygon(3, 4, 0, 0)
    self.print_result()

if __name__ == "__main__":
    main()