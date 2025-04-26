

# matn='abrakad abra'
# # print(matn[::-1])
# # print(matn[s:s:s])
# print(len(matn))

# full_name= 'mirjamol mirzajonov'
# print(full_name.title())

# ism='mirjamol'
# print(ism)


# ism!='mirjamol'
# print(ism!)
# ism_sharif='mirjamol mirzajonov'
# print(ism_sharif)
# IsmSharif='mirjamol mirzajonov'
# print(IsmSharif)
# ismSharif='mirjamol mirzajonov'
# print(type(ismSharif))

# ism='mirjamol'
# # print(ism.find('k'))
# # print(ism.index('ch'))
# print(ism.replace('m','n',7))

# ad=input("adresingiz:\n")
# print(ad.replace('a','o'))


# 1. Matnni o'zgartirish metodlari:
# capitalize() – Matnning birinchi harfini katta qilib, qolganini kichik qiladi.
# casefold() – Matnni kichik harflarga o‘tkazadi (katta-kichik harflarni solishtirish uchun qulay).
# lower() – Matnni kichik harflarga aylantiradi.
# upper() – Matnni katta harflarga aylantiradi.
# swapcase() – Harflarning registerini o'zgartiradi (katta-kichik).
# a='mirJaMoL'
# print(a.swapcase())
# title() – Har bir so'zning birinchi harfini katta qiladi.
# 2. Matnni qidirish va tekshirish metodlari:
# startswith(prefix) – Berilgan prefiks bilan boshlanishini tekshiradi.
# a='mirjamol'
# print(a.startswith('mib'))
# endswith(suffix) – Berilgan suffiks bilan tugashini tekshiradi.
# find(sub) – Substring qayerdan boshlanishini qaytaradi (topilmasa, -1).
# rfind(sub) – Substring qayerdan boshlanishini (oxirdan boshlab) qaytaradi.
# index(sub) – Substring qayerdan boshlanishini qaytaradi (topilmasa, xato).
# rindex(sub) – Substringni oxiridan qidiradi.
# count(sub) – Substring necha marta uchrashini hisoblaydi.
# isalnum() – Faqat harf va raqamlardan iboratligini tekshiradi.
# matn='salom2'
# if matn.isalnum():
#     print(matn)
# else:
#     print('xato')
# isalpha() – Faqat harflardan iboratligini tekshiradi.
# matn='salom'
# if matn.isalpha():
#     print(matn)
# else:
#     print('xato')
# isdigit() – Faqat raqamlardan iboratligini tekshiradi.
# matn='2482'
# if matn.isdigit():
#     print(matn)
# else:
#     print('xato')
# a=input("yoshingiz:\n")
# if a.isdigit():
#     print(2024-int(a))
# else:
#     print('xatolik, faqat son kiriting')
# islower() – Faqat kichik harflardan iboratligini tekshiradi.
# isupper() – Faqat katta harflardan iboratligini tekshiradi.
# isspace() – Faqat bo‘sh joylardan iboratligini tekshiradi.
# matn='ahdf '
# print(matn.isspace())
# istitle() – Har bir so‘z katta harf bilan boshlanganligini tekshiradi.
# matn= 'Mirjamol Mirzajonov'
# print(matn.istitle())
# 3. Matnni formatlash metodlari:
# center(width) – Matnni berilgan kenglikda markazlashtiradi.
# matn='archa'
# print(matn.center(30,'*'))
# a=input('ismingiz\n')
# print(a.center(len(a)+8,'*'))
# ljust(width) – Matnni chap tomonga hizalaydi.
# rjust(width) – Matnni o‘ng tomonga hizalaydi.
# zfill(width) – Matnni nol bilan to‘ldiradi.
# format(*args, **kwargs) – Matnni formatlash uchun ishlatiladi.
# format_map(mapping) – Lug‘at yordamida matnni formatlash.
# 4. Matnni bo‘lish va qo‘shish metodlari:
# split(sep) – Berilgan ajratuvchi bo‘yicha bo‘ladi.
# rsplit(sep) – Oxiridan boshlab bo‘ladi.
# splitlines() – Satrlarga bo‘lib qaytaradi.
# partition(sep) – Matnni uch qismga bo‘ladi (oldin, sep, keyin).
# rpartition(sep) – Oxirgi uchrashuv bo‘yicha bo‘ladi.
# join(iterable) – Iterativ obyektni matnga birlashtiradi.
# 5. Bo‘sh joylarni olib tashlash metodlari:
# strip() – Boshi va oxiridagi bo‘sh joylarni olib tashlaydi.
# matn='    salom    '
# print(matn.strip())
# lstrip() – Boshi (chap tomoni)dagi bo‘sh joylarni olib tashlaydi.
# rstrip() – Oxiri (o‘ng tomoni)dagi bo‘sh joylarni olib tashlaydi.
# 6. Matnni almashtirish metodlari:
# replace(old, new) – Berilgan eski substringni yangi substringga almashtiradi.
# translate(table) – Belgilarni xarita asosida almashtiradi.
# 7. Shablon bilan ishlash metodlari:
# startswith(prefix) – Berilgan prefiks bilan boshlanishini tekshiradi.
# endswith(suffix) – Berilgan suffiks bilan tugashini tekshiradi.
# maketrans() – Belgilarni almashtirish jadvali yaratadi.
# 8. Kodlash va dekodlash metodlari:
# encode(encoding) – Matnni ma’lum kodlashda kodlaydi.
# decode(encoding) – Matnni dekodlaydi (faqat bytes obyektlar uchun).
# 9. Boshqa metodlar:
# len() – Matn uzunligini hisoblash uchun ishlatiladi.
# isidentifier() – Matn Python identifikatori bo‘lishi mumkinligini tekshiradi.
# isascii() – Matn faqat ASCII belgilaridan iboratligini tekshiradi.



