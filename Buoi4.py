# 1. Viết chương trình giải phương trình bậc 2
# import math
# a = float(input("Nhập vào số a: "))
# b = float(input("Nhập vào số b: "))
# c = float(input("Nhập vào số c: "))
# delta = b*b - (4 * a * c)
# if delta > 0:
#     x1 = (-b+math.sqrt(delta))/ (2*a)
#     x2 = (-b-math.sqrt(delta))/ (2*a)
#     print (f"Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}")
# elif delta == 0 :
#     x = -b/(2*a)
#     print (f"Phương trình có 1 nghiệm kép: x= {x}")
# else:
#     print ("Phương trình vô nghiệm")
    
#2. Viết chương trình in ra bảng cửu chương từ 2 - 9 
# for i in range ( 1, 10):
#     print (f"Bảng cửu chương {i}")
#     for j in range (1,11):
#         print (f"{i} x {j} = {i*j}")
#     print ("-"*20)
    #in bảng Cửu chương
    
# 3. Tính tổng các số chẵn từ 1 đến 100
# t = 0 
# for i in range(0, 100):
#     if i % 2 == 0:
#         t = t + i

# print ("Tổng từ 1 - 100 là: ",t )

# 4. Viết chương trình kiểm tra số nguyên tố    
# import math
# def isPrime(n):
#     if n<2:
#         return False
#     for i in range (2, int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#         return True
# n = int(input("Nhập một số: "))

# if isPrime(n):
#     print (f"{n} là 1 số nguyên tố")
# else:
#     print (f"{n} 0 là 1 số nguyên tố")

#5. In ra hình tam giác với chiều cao n
# n = int(input("Nhập chiều cao tam giác: "))

# for i in range(1, n+1):
#     print("*" * i)

#6. Viết chương trình tìm UCLN và BCNN của 2 số
# import math

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))

# ucln = math.gcd(a, b)
# bcnn = abs(a * b) // ucln

# print("UCLN =", ucln)
# print("BCNN =", bcnn)

#7. Viết chương trình đếm số lượng chữ số của một số nguyên
# n = int(input("Nhập số: "))
# n = abs(n)

# if n == 0:
#     dem = 1
# else:
#     dem = 0
#     while n > 0:
#         dem += 1
#         n //= 10
# print("Số chữ số =", dem)