class Point():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "[ Point: Name = " + str(self.name) + " x = " + str(self.x) + " y = " + str(self.y) + " ]"

    def __str__(self):
        return "[ Point: Name = " + str(self.name) + " x = " + str(self.x) + " y = " + str(self.y) + " ]"
