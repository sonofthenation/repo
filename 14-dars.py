# new_list=['olma','son','kitob','maktab','sinf','algebra']
#
# def ocheck(f):
#     b=[]
#     for a in f:
#         if 'o' in a:
#             b.append(a)
#     return b
# print(ocheck(new_list))


# class Tortburchak:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#
#     def p_get(self):
#         answ1=2*(self.x+self.y)
#         return f"P={answ1}"
#
#     def s_get(self):
#         answ2=self.x*self.y
#         return f"S={answ2}"
#
# x=int(input("1-tomon:\n"))
# y=int(input("2-tomon:\n"))
# obj=Tortburchak(x,y)
# print(obj.s_get(),obj.p_get())




# class Tortburchak:

#     MIN=0
#     MAX=100

#     @classmethod
#     def check_num(cls,n):
#         return cls.MIN<=n<=cls.MAX


#     def __init__(self,x,y):
#         self.x=self.y=0
#         if self.check_num(x) and self.check_num(y):
#             self.x=x
#             self.y=y
#         print(self.rais(self.x))

#     def get_info(self):
#         return self.x,self.y
    
# @staticmethod
# def rais(x):
#     return x**2+Tortburchak.MAX




# class Bugdoy:
#     def __init__(self, sort, kg):
#         self.sort = sort
#         self.kg = kg
#
#     def get_info(self):
#         return self.sort, self.kg
#
#
# obj = Bugdoy('qozoq', 50)
# tosh = Bugdoy('tosh', 150)
# xit=Bugdoy('vodiy',30)
# listing=[obj,tosh,xit]
# print(obj.get_info())
#
#
# class Tegrmon:
#     def __init__(self, name):
#         self.name = name
#         self.bugdoy = []
#
#     def get_name(self):
#         return self.name
#
#     def add_b(self, objs):
#         for obj in objs:
#             if isinstance(obj,Bugdoy):
#                 self.bugdoy.append(obj)
#             else:
#                 print('aldama vodiylik')
#
#     def get_un(self):
#         return [un.get_info() for un in self.bugdoy]
#
#
#
# teg = Tegrmon('davron aka')
# teg.add_b(listing)
#
# print(teg.get_un())



# class Market:
#     def __new__(cls, *args, **kwargs):
#         print('bu new',cls)
#         return super().__init__(cls)
#
#     def __init__(self,name,balance):
#         print("bu init",str(self))
#         self.name=name
#         self.balance=balance
#
#     def full(self):
#         return f"{self.name} {self.balance}"
#
#
# obj=Market("Cola",5000)
# print(obj.full(obj))


# class Tortburchak:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     def per(self):
#         return f"Perimetr: {2*(self.x+self.y)}"
#
#     def s_find(self):
#         return f"Yuzasi: {self.x*self.y}"
#
# a=int(input("1-tomon: "))
# b=int(input("2-tomon: "))
# obj=Tortburchak(a,b)
# print(obj.per())
# print(obj.s_find())



# class Tortburchak:
#     MAX=100
#     MIN=1
#
#     @classmethod
#     def check(cls,n):
#         return cls.MIN<=n<=cls.MAX
#
#     def __init__(self,x,y):
#         self.x=self.y=0
#         if self.check(x) and self.check(y):
#             self.x=x
#             self.y=y
#         print(self.raise_num(self.x),self.raise_num(self.y))
#
#     def get(self):
#         return self.x,self.y
#
#     @staticmethod
#     def raise_num(x):
#         return x**2+Tortburchak.MAX
#
#
# # x=int(input("1-tomon: "))
# # y=int(input("2-tomon: "))
# obj=Tortburchak(2,20)
# # print(obj.get())
# print(obj.x,obj.y)



# class Bugdoy:
#     def __init__(self,sort,kg):
#         self.sort=sort
#         self.kg=kg
#
#     def get(self):
#         return self.sort,self.kg
#
#
# obj=Bugdoy("qozoq",50)
# obj2=Bugdoy("toshkent",150)
# hater=Bugdoy('vodiy',30)
# listing=[obj,obj2,hater]
# print(obj.get())
#
# class Tegirmon:
#     def __init__(self,name):
#         self.name=name
#         self.bugdoy=[]
#
#     def get_name(self):
#         return self.name
#
#     def add(self,obj):
#         for ob in obj:
#             if isinstance(ob,Bugdoy):
#                 self.bugdoy.append(ob)
#             else:
#                 print("Aldama")
#
#     def get_un(self):
#         dic=dict([a.get() for a in self.bugdoy])
#         return dic
#
# teg=Tegirmon('Mirjamol aka')
# teg.add(listing)
# print(teg.get_un())





