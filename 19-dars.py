# class Parent1:
#     def method1(self):
#         print("Parent1 metodi")
#
# class Parent2:
#     def method2(self):
#         print("Parent2 metodi")
#
# class Child(Parent1,Parent2):
#     pass
#
# obj=Child()
# obj.method1()
# obj.method2()


# class Odamato:
#     def nomsiz(self):
#         return "odam"
# class Buvi(Odamato):
#     pass
#     # def nomsiz(self):
#     #     return "buvi"
#
# class Bobo(Odamato):
#     pass
#     # def nomsiz(self):
#     #     return "Bobo"
#
# class Ota(Bobo):
#     pass
#     # def nomsiz(self):
#     #     return "ota"
#
# class Ona(Buvi):
#     pass
#     # def nomsiz(self):
#     #     return "ona"
#
# class Bola(Ona,Ota):
#     pass
#
# b=Bola()
# print(b.nomsiz())



# class Mahsulotlar:
#     def __init__(self,mahsulot,narx):
#         self.mahsulot=mahsulot
#         self.narx=narx
#
#     def info(self):
#         return f"{self.mahsulot}ning narxi {self.narx} so'm"
#
# menu={'Osh':25000,'Mastava':30000,'Norin':50000,'Beshbarmoq':35000,'Choy':15000,'Kola':20000,'Salat':32000}
#
# class Jami:
#     def __init__(self):
#         self.jami=[]



# class Menu:
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price
#
#     def info(self):
#         return f"{self.title}ning narxi {self.price} so'm"
#
#
# class Order:
#     def __init__(self):
#         self.menu=[]
#
#     def add_menu(self,menu):
#         self.menu.append(menu)
#
#     # def choice_m(self,nums):
# products = []
# while True:
#
#
#     print('1 menu')
#     print(('2 zakaz'))
#     user=input('tanlang:\n')
#     if user=='3':
#         break
#     if user=='1':
#         title=input('taom nomi:\n')
#         price=input(f'{title}ning narxi:\n')
#         products.append(Menu(title,price))
#         # j=[javob.info() for javob in products]
#
#     elif user=='2':
#         for n,a in enumerate(products,1):
#             print(n,a.info())
#
#         tanlov=input("Raqam bo'yicha tanlang(1,2,3..):\n")
#         tanlov_list=tanlov.split(',')
# print(products)
# print(j)










