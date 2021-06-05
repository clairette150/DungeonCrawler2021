class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, Point):
        self.x = self.x + Point.x
        self.y = self.y + Point.y

    def __repr__(self):
        return "({}/{})".format(self.x, self.y)