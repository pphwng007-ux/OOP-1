from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        super().__init__(f"Lỗi: Giá {gia:,.0f}đ không hợp lệ (phải >= 0)")

class MaHangTrungLap(Exception):
    def __init__(self, ma):
        super().__init__(f"Lỗi: Mã hàng '{ma}' đã tồn tại trong hệ thống")

class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.__ma_hang = ma_hang    # Private [7]
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.gia = gia              # Gọi setter để validate [6, 8]

    @property
    def ma_hang(self):
        return self.__ma_hang

    @property
    def ten_hang(self):
        return self.__ten_hang

    @property
    def gia(self):
        return self.__gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self.__gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    def __str__(self):
        return self.inTTin()

    def __eq__(self, other):
        return self.__ma_hang == other.ma_hang

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.__ma_hang)

class DienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__bao_hanh = bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def loai_hang(self):
        return "Điện máy"

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.ma_hang} | {self.ten_hang} | {self.gia:,.0f}đ | BH: {self.__bao_hanh}T | {self.__dien_ap}V | {self.__cong_suat}W"

class SanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyen_lieu = loai_nguyen_lieu

    def loai_hang(self):
        return "Sành sứ"

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.ma_hang} | {self.ten_hang} | {self.gia:,.0f}đ | Nguyên liệu: {self.__loai_nguyen_lieu}"

class ThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hh):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hh = ngay_hh

    def loai_hang(self):
        return "Thực phẩm"

    def inTTin(self):
        return f"[{self.loai_hang()}] {self.ma_hang} | {self.ten_hang} | {self.gia:,.0f}đ | NSX: {self.__ngay_sx} | HSD: {self.__ngay_hh}"

def luu_file(ds_hang_hoa, filename="kho_hang.txt"):
    with open(filename, "w", encoding="utf-8") as f: # Context Manager [12, 15]
        for hh in ds_hang_hoa:
            f.write(hh.inTTin() + "\n")

if __name__ == "__main__":
    ds_kho = []
    
    def them_hang(hang_moi):
        if any(h.ma_hang == hang_moi.ma_hang for h in ds_kho):
            raise MaHangTrungLap(hang_moi.ma_hang)
        ds_kho.append(hang_moi)

    try:
        them_hang(DienMay("DM01", "Tủ lạnh", "Samsung", 15000000, 24, 220, 150))
        them_hang(SanhSu("SS01", "Bình hoa", "Bát Tràng", 500000, "Gốm"))
        them_hang(ThucPham("TP01", "Sữa tươi", "Vinamilk", 30000, "01/01/2024", "01/01/2025"))

        print("DANH SÁCH HÀNG HÓA:")
        for hh in ds_kho:
            print(hh)

        print("\nDANH SÁCH SAU KHI SẮP XẾP GIÁ:")
        for hh in sorted(ds_kho):
            print(hh)

        luu_file(ds_kho)
        print("\nĐã lưu danh sách vào file kho_hang.txt")

    except (GiaKhongHopLe, MaHangTrungLap) as e:
        print(e)
    except Exception as e:
        print(f"Lỗi hệ thống: {e}")