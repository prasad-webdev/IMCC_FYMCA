# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#     def __repr__(self):
#         return f"Vector2D({self.x}, {self.y})"
# v1 = Vector2D(3, 4)
# v2 = Vector2D(1, 2)
# print(v1 + v2)

class Rect:
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    def param(self):
        return 2 * self.l * self.b
obj1 = Rect(50, 20)
print(obj1.area())
print(obj1.param())