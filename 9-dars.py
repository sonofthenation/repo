# def matnni_qayta_ishlash(matn):
#     def tozalash():
#         return matn.strip().lower()
#     def uzunligi():
#          return len(matn)
#     return tozalash(),uzunligi()

# print(matnni_qayta_ishlash("  Salom DUNYO!  "))
# def hisoblagich():
#     son = 0  # Lokal o'zgaruvchi

#     def qoshish():
#         nonlocal son  # Ichki funksiya tashqi funksiyaning o'zgaruvchisini o'zgartira olishi uchun
#         son += 1
#         if son==5:
#             son=1
#         return son

#     return qoshish  # Ichki funksiyani qaytaramiz

# hisob = hisoblagich()
# print(hisob())  # 1
# print(hisob())  # 2
# print(hisob())  # 3
# print(hisob()) 
# print(hisob()) 
# print(hisob())



def dec1(s):
    def daraja(*args,**kwargs):
        javob=int(s(*args,**kwargs))
        return javob*javob
    return daraja

@dec1
def x(n):
    return n



son=int(input("Son kiriting:\n"))
n=x(son)
print(x(son))


