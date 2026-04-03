class Account:
    def __init__(self, ten, sodu=0):
        self.ten=ten
        self.sodu=sodu
    def napTien(self,soTien):
        self.sodu+=soTien
        print(f"Đã nạp {soTien} vào tài khoản!")
    def rutTien(self, soTien):
        if soTien>self.sodu:
            print("Không đủ tiền!")
        else:
            self.sodu-=soTien
            print(f"Bạn đã rút {soTien} vnđ")
    def hienThi(self):
        print(f"Tên: {self.ten}")
        print(f"Số dư: {self.sodu} vnđ")
class SavingAccount(Account):
    def __init__(self,ten,sodu=0, laiSuat=0.05):
        super().__init__(ten,sodu)
        self.laiSuat=laiSuat
    def tinhLai(self):
        lai = self.sodu * self.laiSuat
        print (f"Tiền lãi: {lai} vnđ")
tk1=Account("Võ Minh Hiển", 20000000)
tk1.napTien(10000000)
tk1.rutTien(29000000) 
tk1.hienThi()
print("----------------------------------")
tk2=SavingAccount("Võ Minh Duy", 40000000)
tk2.napTien(10000000)
tk2.rutTien(45000000)
tk2.hienThi()   