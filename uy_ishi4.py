# ✅ 1. Takroriy sonlarni olib tashlash
# Masala: Berilgan ro‘yxatda takroriy elementlar mavjud. Faqat unikal (bir martalik) elementlardan iborat ro‘yxatni qaytaring.
# nums = [1, 2, 3, 2, 4, 1, 5]

# nums=[1,2,3,2,4,1,5]
# nums=set(nums)
# print(list(nums))


# # Natija: [1, 2, 3, 4, 5]
# ✅ 2. Ikkita ro‘yxat orasidagi umumiy elementlar
# Masala: Ikkita ro‘yxat berilgan. Ular orasidagi umumiy elementlarni toping.
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]


# a=[1,2,3,4]
# b=[3,4,5,6]
# print(set(a).intersection(set(b)))


# # Natija: {3, 4}
# ✅ 3. Faqat birinchi ro‘yxatda bor elementlar
# Masala: Ikkita ro‘yxat berilgan. Faqat birinchi ro‘yxatda bor, lekin ikkinchisida yo‘q elementlarni toping.
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]


# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# print(set(a).difference(set(b)))


# # Natija: {1, 2}
# ✅ 4. To‘plamda nechta element borligini aniqlang
# Masala: Berilgan ro‘yxatni to‘plamga aylantirib, undagi elementlar sonini aniqlang.
# data = [1, 2, 2, 3, 4, 4, 5]


# data=[1,2,2,3,4,4,5]
# print(len(set(data)))


# # Natija: 5
# ✅ 5. Foydalanuvchi kiritgan so‘zlar orasidan yagona so‘zlar sonini aniqlash
# Masala: Foydalanuvchi n ta so‘z kiritadi. Ular orasida nechtasi unikal ekanligini aniqlang.
# # Kirish:
# # 5
# # apple
# # banana
# # apple
# # orange
# # banana


# a=set()
# ab=int(input())
# for c in range(ab):
#     a.add(input())
# print(len(a))


# # Chiqish: 3
# ✅ 6. Matndan unikal harflarni ajratib oling
# Masala: Berilgan matndan barcha unikal harflarni set yordamida ajratib oling (faqat harflarni).
# text = "hello world"


# text="hello world"
# a=set()
# for c in text:
#     if c.isalpha():
#         a.add(c)
#     else:
#         a=a
# print(a)


# # Natija: {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
