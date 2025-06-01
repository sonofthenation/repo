# class Kiyim:
#     def clothe(self):
#         return "Mavjud emas"
#
# class Erkaklar(Kiyim):
#     def __init__(self,color,material):
#         self.color=color
#         self.material=material
#
#     def clothe(self):
#         return f"{self.color} rangli {self.material} shim"
#
# class Ayollar(Kiyim):
#     def __init__(self,color,material):
#         self.color=color
#         self.material=material
#
#     def clothe(self):
#         return f"{self.color} rangli {self.material} ko'ylak"
#
#
# cloth=[Erkaklar('Qora','jensi'),Ayollar('Yashil','paxta')]
# for c in cloth:
#     print(c.clothe())



# class Person:
#     def __init__(self,name,adres,age):
#         self.name=name
#         self._adres=adres
#         self.__age=age
#
#     @property
#     def get(self):
#         return self.__age
#
#
# class Employee(Person):
#     def info(self):
#         return self.name,self.get,self._adres
#
#
#
# l=Employee('ali','chorsu',12)
# print(l.info())



# class User:
#     def __init__(self,name):
#         self.__name=name
#
#     def __namee(self):
#         return self.__name[::-1]
#
#     def __private(self):
#         return self.__namee()
#
#     def get_name(self):
#         return self.__private()
#
# us=User('mirjamol')
# # print(us.__namee())
# # print(us.__private)
# print(us.get_name())



