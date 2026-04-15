import math
class MauSoBangKhong(Exception):
    def __init__(self, message="Mẫu số phải khác 0"):
        self.message = message
        super().__init__(self.message)

class PhanSo:
    def __init__(self, tu=0, mau=1):
        if mau == 0:
            raise MauSoBangKhong()
        self.__tu_so = tu
        self.__mau_so = mau

    @property
    def tu_so(self):
        return self.__tu_so

    @tu_so.setter
    def tu_so(self, value):
        self.__tu_so = value

    @property
    def mau_so(self):
        return self.__mau_so

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong()
        self.__mau_so = value

    def toi_gian(self):
        ucln = math.gcd(self.__tu_so, self.__mau_so)
        self.__tu_so //= ucln
        self.__mau_so //= ucln
        if self.__mau_so < 0: # Đảm bảo dấu nằm ở tử số
            self.__tu_so = -self.__tu_so
            self.__mau_so = -self.__mau_so
        return self

    def is_toi_gian(self):
        return math.gcd(self.__tu_so, self.__mau_so) == 1

    def __add__(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        tu = self.tu_so * other.tu_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __truediv__(self, other):
        if other.tu_so == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử bằng 0")
        tu = self.tu_so * other.mau_so
        mau = self.mau_so * other.tu_so
        return PhanSo(tu, mau).toi_gian()

    def __eq__(self, other):
        return self.tu_so * other.mau_so == other.tu_so * self.mau_so

    def __lt__(self, other):
        return self.tu_so * other.mau_so < other.tu_so * self.mau_so

    def __gt__(self, other):
        return self.tu_so * other.mau_so > other.tu_so * self.mau_so

    def __str__(self):
        if self.mau_so == 1:
            return f"{self.tu_so}"
        return f"{self.tu_so}/{self.mau_so}"

    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    def __hash__(self):
        copy_ps = PhanSo(self.tu_so, self.mau_so).toi_gian()
        return hash((copy_ps.tu_so, copy_ps.mau_so))

if __name__ == "__main__":
    try:
        n = int(input("Nhập số lượng phân số: "))
        ds_phanso = []
        
        for i in range(n):
            print(f"Nhập phân số thứ {i+1}:")
            t = int(input("  Tử số: "))
            m = int(input("  Mẫu số: "))
            ds_phanso.append(PhanSo(t, m))

        print("\nCác phân số sau khi tối giản:")
        for ps in ds_phanso:
            print(ps.toi_gian())

        ds_sap_xep = sorted(ds_phanso)
        print("\nDãy phân số sau khi sắp xếp tăng dần:")
        print(", ".join(str(ps) for ps in ds_sap_xep))

    except MauSoBangKhong as e:
        print(f"Lỗi: {e.message}")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
print("\nChương trình kết thúc.")