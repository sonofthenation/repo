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


# bah={}
# x=int(input("Nechta o'quvchi:\n"))
# for s in range(x):
#     a=input(f"{s+1}-o'quvchi ismi:\n")
#     y=(int(input("Birinchi baho:\n")),int(input("Ikkinchi baho:\n")),int(input("Uchinchi baho:\n")))
#     bah[a]=y
#     b=sum(bah[a])
#     e=len(bah[a])
#     c=(b+b//(b//e)-(e-b%e))//e
#     bah[a]=c
# print(bah)



# Ma'lumot turi: dict, for
# 6.Ovoz berish: Biror bir ovoz berish tizimida ovoz berilgan variantlarni to‘plang va har bir variantning necha marta ovoz olinganligini hisoblang.


# a=int(input("Nechta odam:\n"))
# di={"Alpha":0,"Betta":0,"Gamma":0,"Omega":0,"Sigma":0}
# c=list(di.keys())
# for i in range(a):
#     b=input(f"{i+1}-ishtirokchi, siz kimga ovoz berasiz {c}:\n")
#     di[b]+=1
# print(di)


# Ma'lumot turi: list, dict, for
# 7.Maxsus belgilardan tozalash: Foydalanuvchidan string qabul qiling va maxsus belgilarni olib tashlang (masalan, !, @, # va h.k.).


# a=input("Nimadur yozing:\n")
# b=''
# for i in a:
#     if i.isalpha():
#         b+=i
#     else:
#         continue
# print(b)


# Ma'lumot turi: str, if, for
# 8.Set yordamida do'stlar ro'yxatini yaratish: Do‘stlaringiz ro'yxatini yaratib, takrorlanadigan ismlar bo'lsa olib tashlang.


# a={'Ravshan','Ali','Aziz','Saidaziz','Ikrom','Ali','Vali','Said','Aziz','Azim'}
# print(a)


# Ma'lumot turi: set
# 9.Shaharlar bo'yicha sayohatlar: Foydalanuvchidan qaysi shaharlarga borganligini kiriting va yangi shaharlarga tashrif buyurganligini tekshiring.


# a={'Toshkent','Samarqand','Farg\'ona','Navoi','Buxoro','Namangan','Andijon','Farg\'ona','Namangan','Jizzah'}
# b=input("Qaysi shaharga bordingiz:\n")
# if b in a:
#     print("Siz bu yerda bo'lgansiz")
# else:
#     a.add(b)
#     a=list(a)
#     print(f"Siz bu yerda bo'lmagansiz\n{sorted(a)} ro'yhatingiz yangilandi")


# 10.Ma'lumot turi: list, set, if
# Xarid ro'yxati: Do'kondagi mahsulotlarning narxi dictionaryda saqlangan. Xarid ro'yxatidagi mahsulotlarning umumiy narxini hisoblang.


# mahs={'olma':5000,'nok':4000,"apelsin":6000,"non":3000,"cola":14000,"choy":10000,"konfet":8000,"saryog'":13000}
# a=['cola','non','choy','olma','saryog\'']
# b=0
# for i in a:
#     b+=mahs[i]
# print(f"Sizdan jami {b} so'm")

# Ma'lumot turi: list, dict, for
# 11.Yangi obunachilar: Biror xizmat uchun yangi obunachilar ro'yxati saqlanadi. Agar obunachi ro‘yxatda allaqachon mavjud bo‘lsa, uni qo‘shmang va xabar bering.


# lis=['Ali',"Akbar",'Shoxrux',"Vali","Aziz",'Saidaziz','Azim','Saidazim']
# a=int(input("Nechta yangi obunachi:\n"))
# for i in range(a):
#     b=input("Ismingiz:\n")
#     if b in lis:
#         print("Siz allaqachon obunachisiz")
#     else:
#         print("Siz qo'shildingiz")
#     lis.append(b)
# lis=set(lis)
# print(f"Obunachilar ro'yhati: {lis}")


# Ma'lumot turi: list, set, if, for
# 12.Sinfdagi yuqori baholarni toping: Talabalar va ularning baholari bor. Faqat 80 dan yuqori bo'lgan baholarni chiqarib bering.


# di={'Ali':84,"Vali":80,'Said':88,'Azim':65}
# d={}
# for i in di:
#     if di[i]>80:
#         d[i]=di[i]
# print(d)

# Ma'lumot turi: dict, if, for
# 13.Elektron pochta tozalash: Elektron pochta ro'yxatidan takrorlangan pochta manzillarini olib tashlang va yangi ro‘yxatni qaytaring.


# a=['helloworld@python.com','salamalaikum@brat.com','salambrat@mail.co','vaaleykum@brat.co','salamalaikum@brat.com','helloworld@python.com']
# a=set(a)
# print(a)

# Ma'lumot turi: set, list
# 14.Eng yaxshi savdogarni toping: Sotuvchilar va ularning sotuv hajmlari berilgan dictionary mavjud. Eng ko‘p sotgan sotuvchini toping.


# dic={'Ali':5,"Vali":18,"Ahmad":24,"Aziz":17,"Azim":23}
# a=0
# b=''
# for i in dic:
#     if dic[i]>a:
#         a=dic[i]
#         b=i
# print(b)


# 15.Ma'lumot turi: dict, if, for
# Davlatlar va poytaxtlar: Davlatlar va ularning poytaxtlarini saqlaydigan dictionary yarating. Foydalanuvchi davlat nomini kiritsa, uning poytaxtini ko'rsating.


# di={"O'zbekiston":"Toshkent","Qirg'iziston":"Bishkek","Qozog'iston":"Astana","Tojikiston":"Dushanbe","Rossiya":"Moskva","AQSH":"Vashington","Angliya":"London","Fransiya":"Parij","Germaniya":"Berlin"}
# a=input("Davlan nomini kiriting:\n")
# if a in di:
#     print(di[a])
# else:
#     print("Xato")


# Ma'lumot turi: dict, if