from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f"Lỗi: Tuổi {tuoi} không hợp lệ (phải từ 18-65)")

class BacKhongHopLe(Exception):
    def __init__(self, bac):
        super().__init__(f"Lỗi: Bậc công nhân {bac} không hợp lệ (phải từ 1-10)")

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
        self.tuoi = tuoi  # Gọi setter để kiểm tra validation [3]

    @property
    def ho_ten(self):
        return self.__ho_ten

    @property
    def tuoi(self):
        return self.__tuoi

    @tuoi.setter
    def tuoi(self, value):
        # Validation tuổi từ 18-65 [3]
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self.__tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.__ho_ten} | {self.__tuoi}t | {self.__gioi_tinh} | {self.__dia_chi} | {self.mo_ta()}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__ho_ten}', {self.__tuoi}, '{self.__gioi_tinh}', '{self.__dia_chi}', ...)"

    def __eq__(self, other):
        return self.__ho_ten == other.ho_ten and self.__tuoi == other.tuoi

    def __lt__(self, other):
        return self.__ho_ten < other.ho_ten

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac # Gọi setter validation

    @property
    def bac(self):
        return self.__bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self.__bac = value

    def mo_ta(self):
        return f"Công nhân bậc {self.__bac}/10"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dao_tao = nganh_dao_tao

    def mo_ta(self):
        return f"Kỹ sư ngành {self.__nganh_dao_tao}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên: {self.__cong_viec}"

class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, can_bo):
        self.danh_sach.append(can_bo)

    def tim_kiem_ten(self, ten):
        return [cb for cb in self.danh_sach if ten.lower() in cb.ho_ten.lower()]

    def hien_thi(self):
        for cb in sorted(self.danh_sach):
            print(cb)

    def luu_file(self, filename="canbo.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for cb in self.danh_sach:
                f.write(str(cb) + "\n")

if __name__ == "__main__":
    ql = QLCB()
    try:
        ql.them_moi(CongNhan("Nguyen Van A", 30, "Nam", "Ha Noi", 5))
        ql.them_moi(KySu("Tran Thi B", 28, "Nu", "TP HCM", "CNTT"))
        ql.them_moi(NhanVien("Le Van C", 35, "Nam", "Da Nang", "Ke toan"))

        print("--- DANH SÁCH CÁN BỘ (ĐÃ SẮP XẾP TÊN) ---")
        ql.hien_thi()

        print("\n--- TÌM KIẾM TÊN 'TRAN' ---")
        for kq in ql.tim_kiem_ten("Tran"):
            print(kq)
        
        ql.luu_file()
        print("\nĐã lưu danh sách vào file canbo.txt")

    except (TuoiKhongHopLe, BacKhongHopLe) as e:
        print(f"Lỗi nghiệp vụ: {e}")
    except Exception as e:
        print(f"Lỗi hệ thống: {e}")