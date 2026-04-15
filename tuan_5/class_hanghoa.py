class HangHoa:
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.__gia = gia
        
    def inTTin(self):
        return f"Mã: {self.__ma_hang} | Tên: {self.__ten_hang} | NSX: {self.__nha_sx} | Giá: {self.__gia:,.0f}"
class HangDienMay(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0, tg_baohanh=0, dien_ap=0, cong_suat=0):
        super().__init__(ma_hang, ten_hang, nha_sx, gia) 
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat
        
    def inTTin1(self):
        return f"{ super().inTTin()} | Bảo hành: {self.__tg_baohanh} tháng | Điện áp: {self.__dien_ap}V | Công suất: {self.__cong_suat}W"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0, loai_nguyenlieu=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu
        
    def inTTin1(self):
        return f"{super().inTTin()} | Nguyên liệu: {self.__loai_nguyenlieu}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang="", ten_hang="", nha_sx="", gia=0.0, ngay_sx="", ngay_hethan=""):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hethan = ngay_hethan
        
    def inTTin1(self):
        return f"{super().inTTin()} | NSX: {self.__ngay_sx} | HSD: {self.__ngay_hethan}"

sp1 = HangDienMay("DM01", "Tủ lạnh", "LG", 12000000, 24, 220, 150)
print(sp1.inTTin1())
sp2=HangSanhSu("DO0012","Bình hoa","Minh béo LTĐ",363.636,"Sứ đè tem")
print(sp2.inTTin1())
sp3=HangThucPham("TP001","Sữa", "Vinamilk", 20000, "2023-01-01", "2023-07-01")
print(sp3.inTTin1())