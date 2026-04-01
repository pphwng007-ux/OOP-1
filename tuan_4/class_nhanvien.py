class NhanVien:
    LUONG_MAX = 50000000   

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self._tenNhanVien = tenNhanVien
        self._luongCoBan = luongCoBan
        self._heSoLuong = heSoLuong

   
    def get_tenNhanVien(self):
        return self._tenNhanVien

    def get_luongCoBan(self):
        return self._luongCoBan

    def get_heSoLuong(self):
        return self._heSoLuong

    
    def set_tenNhanVien(self, ten):
        self._tenNhanVien = ten

    def set_luongCoBan(self, luong):
        self._luongCoBan = luong

    def set_heSoLuong(self, heso):
        self._heSoLuong = heso

   

    # 1. Tính lương
    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong

    # 2. In thông tin
    def inTTin(self):
        print("Tên nhân viên:", self._tenNhanVien)
        print("Lương cơ bản:", self._luongCoBan)
        print("Hệ số lương:", self._heSoLuong)
        print("Lương:", self.tinhLuong())

    # 3. Tăng lương
    def tangLuong(self, delta):
        he_so_moi = self._heSoLuong + delta
        luong_moi = self._luongCoBan * he_so_moi

        if luong_moi > NhanVien.LUONG_MAX:
            print("Lương vượt quá mức tối đa!")
            return False
        else:
            self._heSoLuong = he_so_moi
            return True



nv = NhanVien("Nguyen Van A", 5000000, 2.0)

print("== Thông tin ban đầu ==")
nv.inTTin()

print("\n== Tăng lương ==")
if nv.tangLuong(1.0):
    print("Tăng lương thành công!")
else:
    print("Tăng lương thất bại!")

print("\n== Sau khi tăng ==")
nv.inTTin()