# OOP Cơ bản
# class Car:
#     # thuộc tính 
#     def __init__(self, name, style, speed, color):
#         self.name = name
#         self.style = style
#         self.speed = speed
#         self.color = color

#     def get_name(self):
#         return self.name
    
#     # phương thức(hành động)
#     def change_speed(self, speed):
#         self.speed = speed
#         return self.speed

#     def change_color(self, color):
#         self.color = color
#         return self.color
    
# obj_car = Car(name="VF7", style="Sport", speed=0, color='White')
# print(obj_car)
# print(obj_car.name)
# print(obj_car.get_name())
# print(obj_car.change_speed(100))
# print(obj_car.change_color("Gray"))

# obj_kia = Car(name="K3", style="Base", speed=0, color="Red")
# print(obj_kia)
# print(obj_kia.name)
# print(obj_kia.change_speed(20))
# print(obj_kia.change_color("Yellow"))

# print()

from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary  # Đóng gói (Private)

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Lỗi: Lương phải là số dương!")

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_info(self):
        print(f"ID: {self.id} | Tên: {self.name} | Lương cơ bản: {self.get_salary():,.0f}")

class Developer(Employee):
    def __init__(self, id, name, salary, programming_language, overtime_hours):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        return self.get_salary() + (self.overtime_hours * 200)

    def display_info(self):
        super().display_info()
        print(f"Ngôn ngữ: {self.programming_language} | OT: {self.overtime_hours}h")
        print(f"==> Tổng lương: {self.calculate_salary():,.0f} VNĐ")
        print("-" * 30)

class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.get_salary() + self.bonus

    def display_info(self):
        super().display_info()
        print(f"Thưởng quản lý: {self.bonus:,.0f} VNĐ")
        print(f"==> Tổng lương: {self.calculate_salary():,.0f} VNĐ")
        print("-" * 30)

# Test 
if __name__ == "__main__":
    dev = Developer("D01", "Hoàng", 15000, "Python", 10)
    mgr = Manager("M01", "Lan", 20000, 5000)

    dev.display_info()
    mgr.display_info()