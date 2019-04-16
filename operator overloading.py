"""

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):

        x = self.x + other.x
        y = self.y + other.y

        return point(x,y)

    def __str__(self):

        return (" {0},{1}").format(self.x,self.y)

point1 = point(9,4)
point2 = point(1,3)
print(point1 + point2)

"""

#### ASSIGNMENT CODE CHALLENGE 13

class mult:
    def __init(self,x):
        self.x=x

    def __add__(self, other):

        x=self.x+other.x
        return x
abd = mult()
mult1=6
mult2=3
# print(mult1-mult2)