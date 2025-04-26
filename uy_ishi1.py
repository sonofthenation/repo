# 1. Sonni juft yoki toqligini aniqlash
# Masala: Foydalanuvchidan biror butun son (int) kiritishni so‘rang va uning juft yoki toqligini aniqlang.

# Kirish: 15
# Chiqish: Bu son toq.

# 1-VERSION
# a=int(input('Son kiriting:\n'))
# if a%2==1:
#     print('Bu son toq')
# else:
#     print('Bu son juft')

# 2-VERSION
# a=input('Son kiriting:\n')
# if a.isdigit():
#     if int(a)%2==1:
#         print('Bu son toq')
#     else:
#         print('Bu son juft')
# else:
#     print('Faqat son kiriting')


# 2. Haroratni tahlil qilish
# Masala: Foydalanuvchidan haroratni float shaklida kiritishni so‘rang. Agar harorat 0 dan past bo‘lsa, "Havo sovuq", 0 va 20 oralig‘ida bo‘lsa "Havo salqin", 20 dan yuqori bo‘lsa "Havo issiq" deb chiqaring.

# Kirish: 18.5
# Chiqish: Havo salqin.

# a=float(input('Harorat nechchi?\n'))
# if a<=0:
#     print('Havo sovuq')
# elif 0<a<=20:
#     print('Havo salqin')
# else:
#     print('Havo issiq')


# 3. To‘rtburchak shaklidagi xonani maydonini hisoblash
# Masala: Xonaning uzunligi va kengligini float sifatida qabul qilib, maydonini hisoblang va chiqaring.

# Kirish: Uzunlik = 5.5, Kenglik = 4.2
# Chiqish: Xonaning maydoni: 23.1 kv.m.

# a=float(input('Xonaning uzunligi:\n'))
# b=float(input('Xonaning kengligi:\n'))
# print(f"Xonaning maydoni: {a*b} kv.m.")


# 4. Ism uzunligini aniqlash
# Masala: Foydalanuvchidan ismini so‘rang va agar ism uzunligi 5 dan kam bo‘lsa "Ismingiz juda qisqa", 5 dan 8 gacha bo‘lsa "Ismingiz o‘rtacha uzunlikda", 8 dan uzun bo‘lsa "Ismingiz juda uzun" deb chiqaring.

# Kirish: Sardor
# Chiqish: Ismingiz o‘rtacha uzunlikda.

# ism=input('Ismingiz:\n')
# if len(ism)<5:
#     print('Ismingiz juda qisqa')
# elif 5<=len(ism)<=8:
#     print("Ismingiz o'rtacha uzunlikda")
# else:
#     print("Ismingiz juda uzun")

# 5. Baholash tizimi
# Masala: Foydalanuvchidan ballini (int) kiritishni so‘rang va quyidagi shartlarga asosan baho qo‘ying:

# 90 va undan yuqori – A
# 80-89 – B
# 70-79 – C
# 60-69 – D
# 60 dan past – F
# Kirish: 85
# Chiqish: Sizning bahoyingiz: B

# b=int(input('Necha ball:\n'))
# a=b//10
# c=''
# if a>=9:
#     c='A'
# elif a==8:
#     c='B'
# elif a==7:
#     c='C'
# elif a==6:
#     c='D'
# else:
#     c='F'
# print(f"Sizning bahoyingiz {c}")


# 6. Yil faslini aniqlash
# Masala: Foydalanuvchidan oy tartib raqamini (int, 1-12 oralig‘ida) kiritishni so‘rang va faslni aniqlang:

# 12, 1, 2 – Qish
# 3, 4, 5 – Bahor
# 6, 7, 8 – Yoz
# 9, 10, 11 – Kuz
# Kirish: 3
# Chiqish: Bahor fasli.

# a=int(input('Oy tartib raqamini kiriting:\n'))
# b=''
# if a == (12 or 1) or 2:
#     b = 'Qish'
# elif a == (3 or 4) or 5:
#     b = 'Bahor'
# elif a == (6 or 7) or 8:
#     b = 'Yoz'
# elif a == (9 or 10) or 11:
#     b = 'Kuz'
# else:
#     print("To'g'ri kiriting")
# print(f"{b} fasli")


# a=int(input('Oy tartib raqamini kiriting:\n'))
# b=''
# if 1<=a<=12:
#     if a == 12 or a == 1 or a == 2:
#         b = 'Qish'
#     elif a == 3 or a == 4 or a == 5:
#         b = 'Bahor'
#     elif a == 6 or a == 7 or a == 8:
#         b = 'Yoz'
#     else:
#         b = 'Kuz'
#     print(f"{b} fasli")
# else:
#     print("To'g'ri kiriting")




