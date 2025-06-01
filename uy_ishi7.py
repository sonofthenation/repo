# 1. Toq yoki Juft Son
# Berilgan sonning juft yoki toq ekanligini aniqlaydigan funksiya yozing.


# def tj(s):
#     gg=""
#     if s%2==1:
#         gg=" toq son"
#     elif s&2==0:
#         gg=" juft son"
#     return f"{s}{gg}"
# while True:
#     a=int(input("Son: "))
#     print(tj(a))


# 2. Salom Deyuvchi Funksiya
# Foydalanuvchi ismiga qarab "Salom, ism!" shaklida xabar chiqaradigan funksiya yozing.


# def sal(ism):
#     return f"Salom {ism}!"
#
# a=input("Ism: ")
# print(sal(a))


# 3. Ikki sonni qo'shish
# Berilgan ikkita sonni qo‘shib, natijani chiqaradigan funksiya yozing.


# def plus(a,b):
#     return f"{a} + {b} = {a+b}"
#
# a=int(input("1-son: "))
# b=int(input("2-son: "))
# print(plus(a,b))


# 4. Kvadrat Topish
# Berilgan sonning kvadratini hisoblaydigan funksiya yozing.


# def qua(s):
#     qq=s**2
#     return f"{s} * {s} = {qq}"
#
# x=int(input("Son: "))
# print(qua(x))


# 5. Foydalanuvchi Yoshini Tekshirish
# Foydalanuvchidan yoshini kiritib, 18 yoshdan katta yoki kichikligini tekshiradigan funksiya yozing.


# def check(age):
#     ab="Taqiqlangan!"
#     if age>=18:
#         ab="Kirish mumkin."
#     return ab
#
# a=int(input("Yoshingiz: "))
# print(check(a))


# 6. Uchta sonni ko'paytirish
# Berilgan uchta sonni ko‘paytirib, natijani qaytaruvchi funksiya yozing.


# def triple(s,s2,s3):
#     return f"{s} * {s2} * {s3} = {s*s2*s3}"
#
# a=int(input("1-son: "))
# b=int(input("2-son: "))
# c=int(input("3-son: "))
# print(triple(a,b,c))


# 7. Stringni teskari yozish
# Berilgan matnni teskari yozib beruvchi funksiya yozing.


# def tesk(abc):
#     return abc[::-1]
#
# x=input("Matn: ")
# print(tesk(x))


# 8. Eng katta sonni topish
# Berilgan uchta sonning eng kattasini topadigan funksiya yozing.


# def engk(x,y,z):
#     kk=[x,y,z]
#     s=0
#     for a in kk:
#         if a>s:
#             s=a
#     return s
#
# a=int(input("1-son: "))
# b=int(input("2-son: "))
# c=int(input("3-son: "))
# print(engk(a,b,c))


# 9. Sonlarni ko'paytirish
# Berilgan sonlarni ro'yxatdan ko‘paytirib, natijani qaytaradigan funksiya yozing.


# def kop(aa):
#     c=1
#     for a in aa:
#         c*=int(a)
#     return c
#
# while True:
#     a=input("Sonlar(1,2,3...): ")
#     print(kop(a.split(',')))

# 10. Ikki stringni birlashtirish
# Ikki stringni birlashtirib, bitta matn qilib chiqaradigan funksiya yozing.


# def matnn(matn1,matn2):
#     return f"{matn1} {matn2}"
#
# x=input("1-matn:\n")
# y=input("2-matn:\n")
# print(matnn(x,y))

