# import requests
#
#
# url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
# def dic(url):
#     ans=requests.get(url).json()
#     p={}
#     for pul in ans:
#         p[pul['Ccy']]=pul['Rate']
#     return p
#
# p=dic(url)
#
# def conv(x,y):
#     try:
#         a=int(input("Valyuta tanlang:\n1. USD\t2. EUR\t3. RUB:\n"))
#         sel=''
#         match a:
#             case 1:
#                 sel='USD'
#             case 2:
#                 sel='EUR'
#             case 3:
#                 sel='RUB'
#             case _:
#                 print("Xato")
#         if y==1:
#             jav=f"{x/float(p[sel])} {sel}"
#         if y==2:
#             jav=f"{x*float(p[sel])} So'm"
#         return jav
#     except Exception:
#         print(f"Qayta urining")
#
# def fin(x):
#     if x.isdigit():
#         x = float(x)
#     else:
#         print("Son kiriting")
#         x = 0
#     return x
#
#
# while True:
#     chc=input("1. So'mdan o'girish\t2. So'mga o'girish(stop to stop):\n")
#     if chc=='stop':
#         break
#     if int(chc)!=1:
#         if int(chc)!=2:
#             print("Faqat 1 yoki 2 kiriting")
#             continue
#     if fin(chc)==0:
#         continue
#     b=fin(chc)
#     sum=input("Pul hajmini kiriting(stop to stop):\n")
#     if sum=='stop':
#         break
#     if fin(sum)==0:
#         continue
#
#     a=fin(sum)
#     print(conv(a,b))



