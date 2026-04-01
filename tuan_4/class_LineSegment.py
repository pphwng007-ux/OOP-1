class Point:
    """Lớp đại diện cho một điểm trong không gian 2D"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class LineSegment:
    """Lớp đại diện cho đoạn thẳng nối giữa hai điểm d1 và d2"""

    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
            print("--- Khởi tạo mặc định thành công ---")

        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
            print("--- Khởi tạo từ 2 đối tượng Point thành công ---")

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
            print(f"--- Khởi tạo từ 4 tọa độ ({args[0]},{args[1]}) và ({args[2]},{args[3]}) thành công ---")

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            source = args[0]
            self.__d1 = Point(source.get_d1().x, source.get_d1().y)
            self.__d2 = Point(source.get_d2().x, source.get_d2().y)
            print("--- Sao chép sâu đối tượng thành công ---")
        
        else:
            print("Lỗi: Cách truyền đối số không hợp lệ!")

    def get_d1(self):
        return self.__d1

    def get_d2(self):
        return self.__d2

    def display(self):
        print(f"   => Đoạn thẳng: d1({self.__d1.x}, {self.__d1.y}) - d2({self.__d2.x}, {self.__d2.y})")
        print("-" * 50)


if __name__ == "__main__":
    print("BẮT ĐẦU KIỂM TRA LỚP LINESEGMENT:\n")

    # TH1: Hàm xây dựng mặc định
    line1 = LineSegment()
    line1.display()

    # TH2: Hàm xây dựng với 2 đối tượng Point
    p_start = Point(2, 3)
    p_end = Point(7, 9)
    line2 = LineSegment(p_start, p_end)
    line2.display()

    # TH3: Hàm xây dựng với 4 số nguyên
    line3 = LineSegment(10, 20, 30, 40)
    line3.display()

    # TH4: Hàm xây dựng sao chép 
    line4 = LineSegment(line3)
    line4.display()