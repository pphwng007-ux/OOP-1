class NhanVien:
    LUONG_MAX = 20000000

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    def inTTin(self):
        print("Tên:", self.__tenNhanVien)
        print("Lương:", self.tinhLuong())

    def tangLuong(self, delta):
        heSoMoi = self.__heSoLuong + delta
        luongMoi = self.__luongCoBan * heSoMoi

        if luongMoi > NhanVien.LUONG_MAX:
            print("Vượt max!")
            return False
        else:
            self.__heSoLuong = heSoMoi
            return True


# 🔻 Nhập dữ liệu
ten = input("Nhập tên: ")
luongCoBan = float(input("Nhập lương cơ bản: "))
heSoLuong = float(input("Nhập hệ số lương: "))

nv = NhanVien(ten, luongCoBan, heSoLuong)

nv.inTTin()

# test tăng lương
delta = float(input("Nhập mức tăng: "))
nv.tangLuong(delta)

nv.inTTin()