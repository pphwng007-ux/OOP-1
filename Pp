import math
class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y
    def hien_thi(self):
        print(f"Điểm: ({self.__x}, {self.__y})")
    def doi_diem(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def getX(self):
        print(f"X: {self.__x}")
    def getY(self):
        print(f"Y: {self.__y}")
    def khoang_cach_den_O(self):
        kc1 = math.sqrt(self.__x**2 + self.__y**2)
        print(f"Khoảng cách từ điểm đến gốc tọa độ O: {kc1}")
    def khoang_cach_den_diem(self, other):
        kc2 = math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)
        print(f"Khoảng cách từ điểm đến điểm ({other.__x}, {other.__y}): {kc2}")

A = Point(3, 4)
B = Point(6, 8)
P = Point(4, 5)
A.hien_thi()
A.getX()
A.getY()
A.khoang_cach_den_O()
A.khoang_cach_den_diem(P)
B.hien_thi()
B.getX()
B.getY()
B.khoang_cach_den_O()
B.khoang_cach_den_diem(P)
