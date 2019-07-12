class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.x1, self.y1 = self.point1
        self.x2, self.y2 = self.point2

    def distance(self):
            dis = ((self.y2 - self.y1)**2+(self.x2 - self.x1)**2)**.5
            print(dis)

    def slope(self):
            sl = (self.y2-self.y1)/(self.x2-self.x1)
            print(sl)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
li.distance()
li.slope()
