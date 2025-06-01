
# def lis(a):
#     bb=a.split(',')
#     cc=a.split(' ')
#     if len(bb)>len(cc):
#         cc=bb
#     else:
#         bb=cc
#     innt=list(map(lambda x:int(x),bb))
#     sett=set(innt)
#     yosh=list(filter(lambda x:x<=20,innt))
#     qari=list(filter(lambda x:x>20,innt))

#     def yotoifa(x):
#         yf=max(sett)-min(sett)
#         x=f"{len(sett)}-xil yosh toifasi bor\nKatta va kichik yoshlar farqi-{yf}"
#         return x

#     def farq(x,y):
#         farqi=len(x)-len(y)
#         kaki1='Kichik'
#         kaki2='Katta'
#         if farqi>0:
#             abc=f"{kaki1}lar ko'proq-{len(x)}ta\n{kaki2}lar soni-{len(y)}ta"
#         elif farqi<0:
#             abc=f"{kaki2}lar ko'proq-{len(y)}ta\n{kaki1}lar soni-{len(x)}ta"
#         else:
#             abc="Teppa teng"
#         return abc
#     return f"{yotoifa(innt)}\n{farq(yosh,qari)}"


# a=input("O'yinchilarni yoshlarini kiriting:\n")
# b=lis(a)
# print(b)


# while True:
#     try:
#         a=int(input("Son 1:\n"))
#         b=int(input("Son 2:\n"))
#         if a=='stop' or b=='stop':
#             break
#     except ValueError:
#         print("Faqat son kiriting")
#     try:
#         try:
#             print(a/b)
#         except NameError:
#             print("Boshidan")
#     except ZeroDivisionError:
#         print("Nolga bo'lish mumkun emas")





# try:
#     a=input("smth:")
#     print(a.title())
# except IndentationError as i:
#     print(f"Xato {i}")



# dic={}
# while True:
#     a=input("So'z: ")
#     if a=='stop':
#         break
#     if a[0] in dic:
#         dic[a[0]].append(a)
#     else:
#         dic[a[0]]=[a]
# for x,y in dic.items():
#     if len(y)==1:
#         dic[x]=y[0]
# print(dic)

    





