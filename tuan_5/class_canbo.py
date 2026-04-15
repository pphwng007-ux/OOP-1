class CanBo:
    def __init__(self):
        self.ho_ten = ""
        self.tuoi = 0
        self.gioi_tinh = ""
        self.dia_chi = ""

    def nhap(self):
        self.ho_ten = input("Ho ten: ")
        self.tuoi = int(input("Tuoi: "))
        self.gioi_tinh = input("Gioi tinh: ")
        self.dia_chi = input("Dia chi: ")

    def xuat(self):
        print(f"Ho ten: {self.ho_ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Gioi tinh: {self.gioi_tinh}")
        print(f"Dia chi: {self.dia_chi}")


# ===== Công nhân =====
class CongNhan(CanBo):
    def __init__(self):
        super().__init__()
        self.bac = 0

    def nhap(self):
        super().nhap()
        self.bac = int(input("Bac (1-10): "))

    def xuat(self):
        super().xuat()
        print(f"Bac: {self.bac}")


# ===== Kỹ sư =====
class KySu(CanBo):
    def __init__(self):
        super().__init__()
        self.nganh = ""

    def nhap(self):
        super().nhap()
        self.nganh = input("Nganh dao tao: ")

    def xuat(self):
        super().xuat()
        print(f"Nganh: {self.nganh}")


# ===== Nhân viên =====
class NhanVien(CanBo):
    def __init__(self):
        super().__init__()
        self.cong_viec = ""

    def nhap(self):
        super().nhap()
        self.cong_viec = input("Cong viec: ")

    def xuat(self):
        super().xuat()
        print(f"Cong viec: {self.cong_viec}")


# ===== Quản lý cán bộ =====
class QLCB:
    def __init__(self):
        self.ds = []

    def them(self):
        print("1. Cong nhan | 2. Ky su | 3. Nhan vien")
        loai = int(input("Chon loai: "))

        if loai == 1:
            cb = CongNhan()
        elif loai == 2:
            cb = KySu()
        elif loai == 3:
            cb = NhanVien()
        else:
            print("Lua chon khong hop le")
            return

        cb.nhap()
        self.ds.append(cb)

    def tim_kiem(self):
        ten = input("Nhap ten can tim: ")
        for cb in self.ds:
            if ten.lower() in cb.ho_ten.lower():
                cb.xuat()
                print("----------------")

    def hien_thi(self):
        for cb in self.ds:
            cb.xuat()
            print("----------------")


# ===== Main (menu) =====
if __name__ == "__main__":
    ql = QLCB()

    while True:
        print("\n===== MENU =====")
        print("1. Them can bo")
        print("2. Tim kiem theo ten")
        print("3. Hien thi danh sach")
        print("4. Thoat")

        chon = int(input("Chon: "))

        if chon == 1:
            ql.them()
        elif chon == 2:
            ql.tim_kiem()
        elif chon == 3:
            ql.hien_thi()
        elif chon == 4:
            break
        else:
            print("Chon sai!")