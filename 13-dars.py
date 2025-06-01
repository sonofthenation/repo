# class Person:
#     pass
#
# new=Person()
# old=Person()
# # print(type(new))
# print(old)
# print(new)
#
# a=5
# b=5
# # print(type(a))
# # print(id(a))
# print(a==5)
# print(a is b)

# class Person:
#     max_age=100
#
# yangi=Person()
# yangi.max_age=120
# eski=Person()
# eski.cours='backend'
# print(eski.__dict__)
# print(eski.max_age)
# yangi.name='ali'
# yangi.age=5
# print(yangi.__dict__)
# mm=Person()


# class Person:
#     CHECK=100
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def get(self):
#         return f"Ismi: {self.name}, yoshi: {self.age}"
#
# ism=input("ismingiz: ")
# age=int(input("Yoshingiz: "))
#
# obj=Person(ism,age)
# print(obj.get())

# obj=Person('ali',18)
# obj2=Person('vali',55)
# print(obj.get())
# print(obj2.get())
# print(obj.__dict__)
# print(obj.CHECK)
# print(obj2.__dict__)


# class Car:
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#
#     def get_info(self):
#         return f"Mashina modeli: {self.model}, narxi: {self.price}"
#
#
# ob=input("Model kiriting: ")
# pr=int(input("Narxini kiriting: "))
# ab=Car(ob,pr)
# print(ab.get_info())

#
# class Person:
#
#     def __init__(self, name, course):
#         self.name = name
#         self.cous = course
#
#     def get(self):
#         return f"Ism:{self.name}\nKursi:{self.cous}"
#
#     def upd(self):
#         self.cous += 1
#
#
# a = input("Ismingiz:\n")
# b = int(input("Kursingiz:\n"))
# obj = Person(a, b)
# obj.upd()
# print(obj.get())








