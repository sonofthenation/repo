# 1. Listga Element Qo'shish:
# Listda yangi element qo'shing.
# Berilgan list: [1, 2, 3]

# a=[1,2,3]
# a.append(int(input('Son qoshing:\n')))
# print(a)


# 4 sonini list oxiriga qo'shing.
# Yangi list: [1, 2, 3, 4]
# 2. Listdan Elementni O'chirish:
# Berilgan listdan elementni o'chiring.
# Berilgan list: [5, 10, 15, 20]
# 15 sonini listdan o'chiring.

# a=[5,10,15,20]
# # # del a[int(input("O'chirish uchun indeks:\n"))]
# # a.remove(int(input("Son o'chiring:\n")))
# # a.pop(int(input("O'chirish uchun index:\n")))
# print(a)


# Yangi list: [5, 10, 20]
# 3. List Elementini Yangilash:
# Listdagi biror elementni boshqa qiymat bilan yangilang.
# Berilgan list: [8, 9, 10]
# 2-pozitsiyadagi elementni 99 ga o'zgartiring.

# a=[8,9,10]
# a[int(input("Qaysi indexli sonni almashtirish kerak:\n"))]=int(input("Qaysi songa almashsin:\n"))
# print(a)


# Yangi list: [8, 99, 10]
# 4. Listni Boshatish:
# Berilgan listdagi barcha elementlarni olib tashlang.
# Berilgan list: [1, 2, 3, 4, 5]

# a=[1,2,3,4,5]
# a.clear()
# print(a)


# Natija: []
# 5. Listga Bir Nechta Element Qo'shish:
# Listga bir nechta yangi element qo'shing.
# Berilgan list: [3, 6, 9]
# Oxiriga 12 va 15 sonlarini qo'shing.


# a=[3,6,9]
# # a.extend([int(input("Birinchi son:\n")),int(input("Ikkinchi son:\n"))])
# b=[int(input("Birinchi son:\n")),int(input("Ikkinchi son:\n"))]
# print(a+b)


# Yangi list: [3, 6, 9, 12, 15]
# 6. Listdan Elementni Indeks Bo'yicha O'chirish:
# Berilgan listdan indeks bo'yicha elementni o'chiring.
# Berilgan list: [7, 14, 21, 28, 35]
# 3-pozitsiyadagi elementni o'chiring.


# a=[7,14,21,28,35]
# del a[int(input("Indeksini ayting:\n"))]
# print(a)


# Yangi list: [7, 14, 21, 35]
# 7. Listga Element Qo'shish (Ma'lum Pozitsiyaga):
# Ma'lum bir indeksga yangi element qo'shing.
# Berilgan list: [2, 4, 6]
# 1-pozitsiyaga 3 ni qo'shing.


# a=[2,4,6]
# a.insert(int(input("Indeks:\n")),int(input("Son:\n")))
# print(a)


# Yangi list: [2, 3, 4, 6]
# 8. List Elementlarini Almashtirish:
# Listdagi bir qism elementlarni yangi qiymatlar bilan almashtiring.
# Berilgan list: [1, 2, 3, 4, 5]
# 2-4 indekslardagi elementlarni 7 va 8 ga almashtiring.


# a=[1,2,3,4,5]
# a[1:4]=[7,8]
# print(a)


# Yangi list: [1, 7, 8, 5]
# 9. Listni Ko'chirish:
# Listdagi barcha elementlarni boshqa listga ko'chiring.
# Berilgan list: [11, 22, 33]


# a=[11, 22, 33]
# b=[]
# for c in a:
#     b.append(c)
# print(b)


# Natija: [11, 22, 33]
# 10. Listning Oxirgi Elementini O'chirish:
# Listning oxirgi elementini olib tashlang.
# Berilgan list: [4, 5, 6]

# a=[4,5,6]
# a.pop()
# print(a)

# Yangi list: [4, 5]
# 11. Listni Uzunligini Topish:
# Listning nechta elementi borligini aniqlang.
# Berilgan list: [1, 2, 3, 4, 5]

# a=[1,2,3,4,5]
# print(len(a))

# Natija: 5
# 12. Listni Birlashtirish:
# Ikkita listni birlashtirib, yangi list yarating.
# Berilgan listlar: [2, 4, 6] va [8, 10, 12]

# a=[2,4,6]
# b=[8,10,12]
# c=a+b
# print(c)

# Yangi list: [2, 4, 6, 8, 10, 12]
# 13. Elementni Listdan Qidirish:
# Berilgan listda ma'lum bir element bor yoki yo'qligini tekshiring.
# Berilgan list: [5, 10, 15]
# Element 10 bor yoki yo'qligini tekshiring.


# a=[5,10,15]
# b=True
# for c in a:
#     if c==10:
#         b=b
#     else:
#         b=not b
# print(b)


# Natija: True
# 14. Listda Nechta Marta Uchraganini Aniqlash:
# Berilgan listda biror element nechta marta uchraganligini toping.
# Berilgan list: [7, 7, 7, 3, 3]
# Element 7 nechta marta bor?

# a=[7,7,7,3,3]
# b=0
# for b in a:
#     if a==7:
#         b+=1
#     else:
#         b=b
# print(f"{b} martta")


# Natija: 3 marta
# 15. Listni Nusxalash:
# Berilgan listdan yangi nusxa oling.
# Berilgan list: [10, 20, 30]

# a=[10,20,30]
# b=a.copy()
# print(b)

# Yangi list nusxasi: [10, 20, 30]
