import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner  # góc dưới bên trái

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# khoảng cách
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return all(point_in_circle(circle, p) for p in corners)

def rect_circle_overlap(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return any(point_in_circle(circle, p) for p in corners)


center = Point(150, 100)
circle = Circle(center, 75)

rect = Rectangle(50, 30, Point(140, 90))

print(point_in_circle(circle, Point(150, 100)))  
print(rect_in_circle(circle, rect))             
print(rect_circle_overlap(circle, rect))        