import pandas as pd
sinhvien={
    "MaSv": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    "HoTen": [ "Võ Minh Hiển", "Trương Thị Ngọc Hậu", "Trần Minh Khâm", "Cao Tấn Đạt", "Võ Minh Duy", "Lê Tấn Duy", "Hồ Tuấn Kiệt", "Võ Hà Thư", "Lê Kiều Thư", "Dương Trân" ],
    "Lop" : ["23ct4", "23ct4", "23ct4", "23ct4", "23ct1", None, "23NH1", "22KT1", "22NN2", "23VT4"],
    "DiemPython": [9, 8.7,8.5, 8.6, 9, None, None, 6, 10, 10],
    "DiemWeb" : [10, 9,8, 7, 10, 5,6,8, 9, 10],
    "DiemDatabase" : [ 9, 8.7,None, None, 9,None, 8, 6, 10, 10 ]
    
}
df = pd.DataFrame(data=sinhvien)
print(df)

#1. Kiểm tra dữ liệu bị null
print("\nKiểm tra giá trị null:")
print(df.isnull())
print ("-----------------------------")
#Dien gia tri null bang 0
print("\nDien gia tri null bang 0:")
print(df.fillna(0))
print ("-----------------------------")
#Tạo cột DTB = DTB 3 môn
print("\n Điểm trung bình 3 môn là:")
df["DTB"] = (df["DiemPython"] + df["DiemWeb"]+df["DiemDatabase"])/3
print(df)
print ("-----------------------------")
#5.Tạo cột XepLoai (Giỏi >= 8, Khá >= 6.5, Trung bình >= 5, Yếu < 5)
print("\n Xếp loại:")
def xeploai(dtb):
    if dtb >= 8:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["XepLoai"] = df["DTB"].apply(xeploai)

print(df[["HoTen", "DTB", "XepLoai"]])

#6.Thống kê dữ liệu theo cột Lop
print ("-----------------------------")
print("Lọc theo tên lớp:")
df_locDK = df[df["Lop"]=="23ct4"]
print(df_locDK)

#7.Tính điểm trung bình DiemTB của mỗi lớp
print ("-----------------------------")
print("Lọc DiemTB theo tên lớp:")
i_groupby = df.groupby("Lop")["DTB"]
for i in i_groupby:
    print (i)
    print()
    
#8.Tạo một bảng Thông Tin Lớp với các cột: Lop, GiaoVien, PhongHoc

thongtinlop = {
    "Lop": ["23ct4", "23ct1", "23NH1", "22KT1", "22NN2", "23VT4"],
    "GiaoVien": ["Thầy An", "Cô Bình", "Thầy Cường", "Cô Dung", "Thầy Hòa", "Cô Lan"],
    "PhongHoc": ["101", "202", "303", "404", "505", "606"]
}

# Tạo DataFrame
df_thongtinlop = pd.DataFrame(thongtinlop)

print("\nBảng Thông Tin Lớp:")
print(df_thongtinlop)
#Ghép 2 bảng lại
print ("-----------------------------")
print("Bảng sau khi được ghép")
df_ghep=df.merge(df_thongtinlop, on="Lop", how="inner")
print(df_ghep)