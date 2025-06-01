# class Time:
#     DAY = 86400
import random
from itertools import count


#     def __init__(self, second):
#         self.second = second

#     def verify_time(self):
#         s = self.second % 60
#         m = (self.second // 60) % 60
#         h = (self.second // 3600) % 24
#         return f"{self.formatted(h)}:{self.formatted(m)}:{self.formatted(s)}"

#     @classmethod
#     def formatted(cls, x):
#         return str(x).rjust(2, "0")

#     def __add__(self, x):
#         if isinstance(x,Time):
#             return Time(self.second + x.second)
#         else:
#             return Time(self.second+x)


# t = Time(70)
# m = Time(50)
# t = t + m
# # print(type(t))
# print(t.verify_time())

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)
#
#     def __truediv__(self, scalar):
#         return Vector(self.x / scalar, self.y / scalar)
#
#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
#
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * 2)
# print(v1 / 2)


# HARF="qwertyuiopasdfghjklzxcvbnm"
# UHARF=HARF.upper()
# login=""
# password=""
# id=random.randint(1000000,9999999)
# for a in range(7):
#     login+=random.choice(HARF)
#     password+=random.choice([random.choice(HARF),random.choice(UHARF),str(random.randint(0,9))])
# print(login)
# print(password)
# print(id)


# class Car:
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price
#
#     @staticmethod
#     def add(self):
#         self.price+=self.price*0.1
#
#     def add_p(self):
#         self.price+=self.price*0.2
#
#
#
#
# o=Car('nexia',3000)
# # print(o.add(o))
# print(o.add_p())
# print(o.__dict__)



# class Ustudy:
#     def __init__(self,group,count,price):
#         self.group=group
#         self.count=count
#         self.price=price
#
#
#     # def __len__(self):
#     #     return self.price+self.count
#
#
#
#
#
#
#
#     # def __str__(self):
#     #     return f"{self.group} nomli group studentlar soni {self.count} ta"
#     #
#     #
#     # def __repr__(self):
#     #     return str(self.count)
#
#
#
#
#
# new=Ustudy('back-end',5,100)
# old=Ustudy('front-end',10,150)
# son=-5
# print(abs(son))
# print(len(new))
# print(len(old))


# class Ustudy:
#     def __init__(self, group, count, price):
#         self.group = group
#         self.count = count
#         self.price = price
#
#
#
#
#
#
#
#
# new = Ustudy('back-end', -5, 100)
# old = Ustudy('front-end', 10, 150)




class Time:
    FULL_TIME=86400
    DAY=1
    YEAR=2025

    def __init__(self,second):
        self.second=second
        # dt=self.second//Time.FULL_TIME
        # if dt>=1:
        #     for i in range(dt):
        #         self.day()
        # yt = Time.DAY // 365
        # if yt>=1:
        #     for i in range(yt):
        #         self.year()

    @property
    def verify_time(self):
        h=self.second//3600%24
        m=self.second//60%60
        s=self.second%60
        return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"

    def __add__(self, x):
        if type(x)==Time:
            return Time(self.second+x.second)
        else:
            return Time(self.second+x)

    # @classmethod
    # def day(cls):
    #     cls.DAY+=1
    #     return cls.DAY
    #
    # @classmethod
    # def year(cls):
    #     cls.YEAR+=1
    #     return cls.YEAR



# a=int(input("Necha soniya: "))
t=Time(50)
m=Time(70)
l=t+30
print(l.verify_time)
#
# print(f"""Soat {t.verify_time}
# {t.DAY%365}-kun
# {t.YEAR}-yil""")

















# ll=[]
# lm=''
# a=int(input("Birnima: "))
# while a>0:
#     ll.insert(0,str(a%1000))
#     a//=1000
# for i in ll:
#     lm+=i+" "
# print(lm)












