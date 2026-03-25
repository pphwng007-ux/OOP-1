class NhanVien:
    LUONG_MAX = 50000000  # lương tối đa

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    # ===== Getter =====
    def get_tenNhanVien(self):
        return self.__tenNhanVien

    def get_luongCoBan(self):
        return self.__luongCoBan

    def get_heSoLuong(self):
        return self.__heSoLuong

    def get_LUONG_MAX(self):
        return NhanVien.LUONG_MAX

    # ===== Setter =====
    def set_tenNhanVien(self, tenNhanVien):
        if isinstance(tenNhanVien, str) and tenNhanVien.strip() != "":
            self.__tenNhanVien = tenNhanVien
        else:
            print(" Tên không hợp lệ")

    def set_luongCoBan(self, luongCoBan):
        if luongCoBan > 0:
            self.__luongCoBan = luongCoBan
        else:
            print(" Lương cơ bản phải > 0")

    def set_heSoLuong(self, heSoLuong):
        if heSoLuong > 0:
            self.__heSoLuong = heSoLuong
        else:
            print(" Hệ số lương phải > 0")

    def set_LUONG_MAX(self, luong_max):
        if luong_max > 0:
            NhanVien.LUONG_MAX = luong_max
        else:
            print(" LUONG_MAX phải > 0")

    # ===== Tính lương =====
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    # ===== Tăng lương (boolean) =====
    def tangLuong(self, delta):
        luong_moi = (self.__luongCoBan + delta) * self.__heSoLuong

        if luong_moi > NhanVien.LUONG_MAX:
            print(" Lương vượt quá mức tối đa!")
            return False
        else:
            self.__luongCoBan += delta
            return True

    # ===== In thông tin =====
    def inTTin(self):
        print("Tên:", self.__tenNhanVien)
        print("Lương cơ bản:", self.__luongCoBan)
        print("Hệ số lương:", self.__heSoLuong)
        print("=> Lương:", self.tinhLuong())


# ===== TEST =====
if __name__ == "__main__":
    nv = NhanVien("Phuong", 5000000, 3)

    print("=== Thông tin ban đầu ===")
    nv.inTTin()

    print("\n=== Tăng lương ===")
    if nv.tangLuong(2000000):
        print(" Tăng lương thành công")
    else:
        print(" Tăng lương thất bại")

    print("\n=== Sau khi tăng ===")
    nv.inTTin()