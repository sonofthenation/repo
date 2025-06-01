#
# class Person:
#     HARF="qwertyuiopasdfghjklzxcvbnm"
#     U_HARF=HARF.upper()
#
#     def __init__(self,full_name,age,weight,ps):
#         self.verify_fullname(full_name)
#         self.verify_age(age)
#         self.verify_weight(weight)
#         self.full_name=full_name
#         self.age=age
#         self.weight=weight
#         self.ps=ps
#
#     @classmethod
#     def verify_fullname(cls,full_name):
#         if type(full_name)!=str:
#             raise TypeError("malumotni str korinishida yozing")
#         name_soni=full_name.split(' ')
#         if len(name_soni)!=3:
#             raise ValueError("ism fam ochistva 3 qismdan oshmasni kam ham bolmasin ")
#
#         check_name=cls.HARF+cls.U_HARF
#         for name_s in name_soni:
#             # print(name_s)
#             for name in name_s:
#                 # print(name)
#                 if  not name in check_name:
#                     raise TypeError("faqat lotin harflaridan iborat bo'lsin")
#
#     @classmethod
#     def verify_age(cls,age):
#         if type(age)!=int:
#             raise TypeError(" siz yoshizni sonda kiriting")
#         if not 18<=age<=120:
#             raise ValueError("18 ca 120 oraligida bolsin")
#
#
#     @classmethod
#     def verify_weight(cls,weight):
#         if type(weight)!=float:
#             raise TypeError(" faqat float type kiriting")
#         if not 20<weight<=150:
#             raise ValueError(" sizning vesingiz togri kelmadi")
#
#
#     @classmethod
#     def verify_ps(cls,ps):
#         if type(ps)!=str:
#             raise TypeError("str type yozing")
        
        


# 4 ta concept
# encapsulation, polymorphism, inheritance, abstraction
# public, _protected, __private


# class Ustudy:
#     def __init__(self,name,group_name,id):
#         self.name=name
#         self._group_name=group_name
#         self.__id=id
#
#     def getgr(self):
#         return self._group_name
#
#     def getid(self):
#         return self.__id
#
#
# obj=Ustudy('Mirjamol','back-end',20)
# # print(obj.group_name)
# # print(obj.getid())
# # print(obj.getgr())
# # print(obj.getid())
# obj.name='Ali'
# print(obj.name)



# class User:
#     def __init__(self,name,password):
#         self.name=name
#         self.__password=password
#
#     def get_name(self):
#         return self.name
#
#     def check(self,p):
#         return p==self.__password
#
# a=input("Your name: ")
# b=input("What is password: ")
# obj=User(a,'ppwd6267')
# print(obj.check(b))



# class Karzinka:
#     def __init__(self,name,address,balance):
#         self.__name=name
#         self.__address=address
#         self.balance=balance
#
#     def get(self):
#         return self.balance
#
#     @property
#     def address(self):
#         return self.__address
#
#     @address.setter
#     def address(self,a):
#         self.__address=a
#
# obj=Karzinka('mirzo ulugbek','it park',100000)
# # print(obj.get())
# # print(obj.__dict__)
# obj.address='chorsu'
# print(obj.address)



# class Person:
#     HARF="qwertyuiopasdfghjklzxcvbnm"
#     U_HARF=HARF.upper()
#     def __init__(self,full_name,age,weight,ps):
#         self.fullname(full_name)
#         self.agecheck(age)
#         self.checkwe(weight)
#         self.pscheck(ps)
#         self.__full_name=full_name
#         self.__age=age
#         self.__weight=weight
#         self.__ps=ps
#
#     @classmethod
#     def fullname(cls,full_name):
#         if type(full_name)!=str:
#             raise TypeError("Malumotni str ko'rinishida yozing")
#         namco=full_name.split(" ")
#         if len(namco)!=3:
#             raise ValueError("Faqat 3 ta element")
#         chck=cls.HARF+cls.U_HARF
#         for a in namco:
#             for x in a:
#                 if not x in chck:
#                     raise ValueError("Faqat lotin harflar yozing")
#         return full_name
#
#     @classmethod
#     def agecheck(cls,age):
#         if type(age)!=int:
#             raise TypeError("Faqat son kiriting yoshga")
#         if not 18<=age<=120:
#             raise ValueError("18 dan kichkina 120 dan katta bo'lmasin")
#         return age
#
#     @classmethod
#     def checkwe(cls,weight):
#         if type(weight) not in (int,float):
#             raise TypeError("Faqat son ko'rinishida bo'lsin")
#         if not 20<=weight<=150:
#             raise ValueError("Vesingiz to'g'ri kelmadi")
#         return weight
#
#     @classmethod
#     def pscheck(cls,ps):
#         pss=ps.split(' ')
#         if len(pss)!=2:
#             raise ValueError("2 ta elementdan iborat bo'lsin")
#         for pp in pss[0]:
#             if pp not in cls.U_HARF or len(pss[0])!=2:
#                 raise ValueError("Pasport seriyasi xato")
#         if not pss[1].isdigit() or len(pss[1])!=7:
#             raise ValueError("Pasport raqami xato")
#         return ps
#
#     @property
#     def full_name(self):
#         return self.__full_name
#
#     @full_name.setter
#     def full_name(self,full_name):
#         self.fullname(full_name)
#         self.__full_name=full_name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,age1):
#         self.agecheck(age1)
#         self.__age=age1
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weigh):
#         self.checkwe(weigh)
#         self.__weight = weigh
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, psid):
#         self.pscheck(psid)
#         self.__ps = psid
#
#
# obj=Person('Mirjamol Mirzajonov Baxromovich',18,55,"AD 1234567")
# print(obj.__dict__)








