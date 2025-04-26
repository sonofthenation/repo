# 1.Talabalar ro'yxati: Talabalar ro'yxatini (list) yarating. Har bir talabaning ismi va bahosi bo‘lsin. Agar talabaning bahosi 90 dan yuqori bo‘lsa, "Ajoyib" deb chiqaring.

# Ma'lumot turi: list, dict, if, for

# stud=[]
# b=int(input("Studentlar soni:\n"))
# for a in range(b):
#     x=input(f"{a+1}- student ismi:\n")
#     y=int(input(f"{a+1}- student bahosi:\n"))
#     if y >=90:
#         y="Ajoyib"
#     stud.append({x:y})
# print(stud)

# 2.Mevalarni filtrlash: Mevalar ro'yxati bor. Faqat "olma" bo‘lgan elementlarni chiqarib oling.

# Ma'lumot turi: list, if, for

# soni=int(input("Mevalar soni:\n"))
# mevalar=[]
# for a in range(soni):
#     b=input(f"{a+1}- meva:\n")
#     if b=="olma":
#         mevalar.append(b)
# print(mevalar)


# 3.Do'kon mahsulotlari: Mahsulotlar va ularning narxlari saqlangan dictionary yarating. Foydalanuvchidan mahsulot nomini kiriting va narxini qaytaring.

# Ma'lumot turi: dict, if

# mahs={'olma':5000,'cola':14000,'choy':10000,'non':3000,'sosiska':13000,'shokolad':7000}
# b=list(mahs.keys())
# a=input(f"Qaysi mahsulot kerak {b}:\n")
# print(f"Sizdan {mahs[a]} so'm")

# 4.Telefon kontaktlari: Telefon kontaktlarini (ism va telefon raqami) saqlovchi dictionary yarating. Foydalanuvchi kontakt kiritganda uni izlab toping yoki qo‘shing.


# kont={'Ali':'(94)-364-85-53','Vali':'(33)-725-64-82',"Salim":'(97)-777-77-77'}
# son=int(input("Nechta kontakt kerak:\n"))
# for s in range(son):
#     a=input("Kontakt kiriting:\n")
#     if a in kont:
#         print(kont[a])
#     else:
#         b=input("Kontakt raqamini kiriting-->(XX)-XXX-XX-XX:\n")
#         kont[a]=b
# print(kont)


# Ma'lumot turi: dict, if, for
# 5.O'rtacha bahoni hisoblash: Talabalarning baholari saqlangan dictionary berilgan. Har bir talabaning o'rtacha bahosini hisoblang.


bah={'Ali':(5,4,5),'Vali':(3,5,5),'Ravshan':(4,4,5),'Munisa':(4,4,3),'Ahmad':(3,4,3)}
for a in bah:
    b=sum(bah[a])//len(bah[a])
    bah[a]=b
print(bah)


# Ma'lumot turi: dict, for
# 6.Ovoz berish: Biror bir ovoz berish tizimida ovoz berilgan variantlarni to‘plang va har bir variantning necha marta ovoz olinganligini hisoblang.

# Ma'lumot turi: list, dict, for
# 7.Maxsus belgilardan tozalash: Foydalanuvchidan string qabul qiling va maxsus belgilarni olib tashlang (masalan, !, @, # va h.k.).

# Ma'lumot turi: str, if, for
# 8.Set yordamida do'stlar ro'yxatini yaratish: Do‘stlaringiz ro'yxatini yaratib, takrorlanadigan ismlar bo'lsa olib tashlang.

# Ma'lumot turi: set
# 9.Shaharlar bo'yicha sayohatlar: Foydalanuvchidan qaysi shaharlarga borganligini kiriting va yangi shaharlarga tashrif buyurganligini tekshiring.

# 10.Ma'lumot turi: list, set, if
# Xarid ro'yxati: Do'kondagi mahsulotlarning narxi dictionaryda saqlangan. Xarid ro'yxatidagi mahsulotlarning umumiy narxini hisoblang.

# Ma'lumot turi: list, dict, for
# 11.Yangi obunachilar: Biror xizmat uchun yangi obunachilar ro'yxati saqlanadi. Agar obunachi ro‘yxatda allaqachon mavjud bo‘lsa, uni qo‘shmang va xabar bering.

# Ma'lumot turi: list, set, if, for
# 12.Sinfdagi yuqori baholarni toping: Talabalar va ularning baholari bor. Faqat 80 dan yuqori bo'lgan baholarni chiqarib bering.

# Ma'lumot turi: dict, if, for
# 13.Elektron pochta tozalash: Elektron pochta ro'yxatidan takrorlangan pochta manzillarini olib tashlang va yangi ro‘yxatni qaytaring.

# Ma'lumot turi: set, list
# 14.Eng yaxshi savdogarni toping: Sotuvchilar va ularning sotuv hajmlari berilgan dictionary mavjud. Eng ko‘p sotgan sotuvchini toping.

# 15.Ma'lumot turi: dict, if, for
# Davlatlar va poytaxtlar: Davlatlar va ularning poytaxtlarini saqlaydigan dictionary yarating. Foydalanuvchi davlat nomini kiritsa, uning poytaxtini ko'rsating.

# Ma'lumot turi: dict, if