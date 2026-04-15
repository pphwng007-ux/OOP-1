class NhanVien:
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0.0, he_so_luong=0.0, luong_toi_da=0.0):
        self.__ho_ten = ho_ten
        self.__nam_sinh = nam_sinh
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
        self.__luong_co_ban = luong_co_ban
        self.__he_so_luong = he_so_luong
        self._luong_toi_da = luong_toi_da
        self.Luong = self.__luong_co_ban * self.__he_so_luong

    def inTTin(self):
        print(f'Họ và tên: {self.__ho_ten} | Năm sinh: {self.__nam_sinh} | Giới tính: {self.__gioi_tinh} | Địa chỉ: {self.__dia_chi}')
        print(f'Lương = {self.__luong_co_ban:,.0f} x {self.__he_so_luong} = {self.Luong:,.0f}')

class CongTacVien(NhanVien):
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0.0, he_so_luong=0.0, luong_toi_da=0.0, thoi_han_hop_dong="", phu_cap_CTV=0.0):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi, luong_co_ban, he_so_luong, luong_toi_da)  
        self.__thoi_han_hop_dong = thoi_han_hop_dong
        self.__phu_cap_CTV = phu_cap_CTV
        
        self.LuongThucNhan = self.Luong + self.__phu_cap_CTV

    def inTTin1(self):
        super().inTTin()
        print(f'Cộng tác viên - Thời hạn hợp đồng: {self.__thoi_han_hop_dong}')
        print(f'Lương thực nhận = {self.LuongThucNhan:,.0f}')
        print('-----------------------------------------------------------------')
class NhanVienChinh(NhanVien):
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0.0, he_so_luong=0.0, luong_toi_da=0.0,vi_tri=""):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi, luong_co_ban, he_so_luong, luong_toi_da)
        self.__vi_tri=vi_tri
    def inTTin1(self):
        super().inTTin()
        print(f'{self.__vi_tri}')
        print('-----------------------------------------------------------------')
class TruongPhong(NhanVien):
    def __init__(self, ho_ten="", nam_sinh=0, gioi_tinh="", dia_chi="", luong_co_ban=0, he_so_luong=0, luong_toi_da=0, ngay_bat_dau_QL="",phu_cap_QL=0.0):
        super().__init__(ho_ten, nam_sinh, gioi_tinh, dia_chi, luong_co_ban, he_so_luong, luong_toi_da)
        self.ngay_bat_dau_QL=ngay_bat_dau_QL
        self.phu_cap_QL=phu_cap_QL
        self.Luong_thuc_nhan= self.Luong+ self.phu_cap_QL
    def inTTin1(self):
        super().inTTin()
        print(f'Trưởng phòng- Quản lí từ: {self.ngay_bat_dau_QL}- Phụ cấp quản lí: {self.phu_cap_QL}')
        print(f'Lương thực nhận= {self.Luong_thuc_nhan:,.0f}')
        print('-----------------------------------------------------------------')
nv1 = CongTacVien("Độ Mixi", 1989, "Nam", "120 Yên Lãng, Đống Đa, Hà Nội", 100000, 36.6, 360000000, "12 tháng", 100000)
nv1.inTTin1()
nv2= NhanVienChinh("Thái An",2007,"Nam","Thanh Hóa",10000000,10.72,999999999,"Chuyên viên IT")
nv2.inTTin1()
nv3=TruongPhong("Meow",2007,"Nữ","Bắc Ninh",28000000,12.3,3000000000,"26/03/2026",5000000)
nv3.inTTin1()