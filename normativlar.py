# nom=input("Sotilgan mahsulot nomini kiriting:\n")
# son=int(input(f"Bugun sotilgan {nom} sonini kiriting:\n"))
# narx=float(input(f"Har bir {nom}ning narxini kiriting:\n"))
# print(f"""Mahsulot nomi: {nom}
# Bugun sotilgan {nom}lar soni: {son}
# Har bir {nom}ning narxi: {narx} so'm
# Umumiy savdo summasi: {son*narx} so'm""")









# oquvchilar = ["Ali", "Vali", "Laylo", "Mavluda"]
# reytinglar = { "Ali": (5, 4, 3),
#               "Vali": (4, 4, 5),
#               "Laylo": (5, 5, 5),
#               "Mavluda": (3, 4, 3)
#               }
# tugilgan_kunlar = {"Ali": "2005-05-01",
#                    "Vali": "2004-08-15",
#                    "Laylo": "2005-09-12",
#                    "Mavluda": "2004-12-25"
#                    }
# qatnashuvchilar=set(oquvchilar)
# a=input("Yangi o'quvchi ismini kiriting: ")
# oquvchilar.append(a)
# reytinglar[a]=(0,0,0)
# bd=input(f"{a}ning tug'ilgan kunini kiriting (YYYY-MM-DD): ")
# tugilgan_kunlar[a]=bd
# och=input("O'chiriladigan o'quvchi ismini kiriting: ")
# oquvchilar.remove(och)
# del reytinglar[och]
# del tugilgan_kunlar[och]
# qatnashuvchilar.discard(och)
# qatn=input("Darsga qatnashayotgan o'quvchini kiriting: ")
# qatnashuvchilar.add(qatn)
# kelmagan=input("Darsga kelmagan o'quvchini kiriting: ")
# qatnashuvchilar.discard(kelmagan)

# print(f"\n\n{a} ro'yhatga qo'shildi.\n\n{och} ro'yxatdan o'chirildi.\n\nO'quvchilar va ularning reytinglari:")

# for k,v in reytinglar.items():
#     print(f"{k}:{v}")
#     if sum(v)//len(v)==5:
#         print(f"-{k}ning reytingi a'lo! Tabriklaymiz!")
#     elif sum(v)//len(v)==4:
#         print(f"-{k}ning reytingi yaxshi!")
#     else:
#         continue
# print("\n\nO'quvchilarning tug'ilgan kunlari:")
# for k1,v1 in tugilgan_kunlar.items():
#     print(f"{k1}:{v1}")
# print(f"\n\n{a} qatnashuvchilar ro'yhatiga qo'shildi.\n\n{kelmagan} qatnashuvchilar ro'yhatidan o'chirildi.\n\nDarsga qatnashayotgan o'quvchilar:\n{qatnashuvchilar}")























