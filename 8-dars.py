
# def func(a):
#     return len(a)

# ism=input("Ismingiz:\n")


# def fun(b):
#     return b*'a'

# uzuna=func(ism)

# print(fun(uzuna))


# mevalar=["olma","banan","uzum","nok"]
# narxlar=(5000,7000,10000)

# bogl=list(zip(mevalar,narxlar))
# print(bogl)

# f=0

# def lenn(b):
#     a=len(b)
#     return a

# def aa(x):
#     b=x*'a'
#     return b.title()




# ism=input("Ismingiz:\n")
# a=lenn(ism)
# print(aa(a))




# def len(x):
#     ln=0
#     for i in x:
#         ln+=1
#     return ln



# ab=input("Ism:\n")
# print((len(ab)))




# def yuza(a,b):
#     return 2*(a+b)

# def per(a,b):
#     return a*b

# a=int(input("A tomon:\n"))
# b=int(input("B tomon:\n"))

# print(f"Yuza-{yuza(a,b)}\nPerimetr-{per(a,b)}")





# def a_find(m):
#     return m.count('a')


# a=input("Matn kiriting:\n")
# print(a_find(a))




# def dis(narx,cheg):
#     if cheg<100:
#         narx-=narx/100*cheg
#     else:
#         print("Chegirma foizi xato")
#     return f"Yangi narx-{narx}"

# narx=int(input("Mahsulot narxini kiriting:\n"))
# cheg=float(input("Chegirma foizini kiriting:\n"))
# print(dis(narx,cheg))





# def salary(a):
#     for i in a:
#         a[i]*=8*22
#     return a


# ishchilar={"Ali":15000,"Vali":20000,"Olim":18000}
# print(salary(ishchilar))





# new=lambda a,b:a+b

# print(new(20,10))





# sonlar=[1,2,3,4,5,6,7,8]


# new=map(lambda x:x**2,sonlar)
# print(list(new))






# ishchilar={"Ali":15000,"Vali":20000,"Olim":18000}
# salary=list(map(lambda x:ishchilar[x]*8*22,ishchilar))
# for a in ishchilar:
#     b=0
#     ishchilar[a]=salary[b]
#     b+=1
# print(ishchilar)



# sonlar=list(range(6))
# m=list(filter(lambda x:x>2,sonlar))
# hisob=tuple(map(lambda x:x**4,m))
# print(hisob)



# ishchilar={"Ali":15000,"Vali":20000,"Olim":18000}
# salary=list(map(lambda x:ishchilar[x]*8*22,ishchilar))
# print(dict(zip(ishchilar,salary)))



# mevalar=["olma","banan","uzum"]
# narxlar=[5000,7000,10000,3000]
# boglangan=list(zip(mevalar,narxlar))
# print(boglangan)



# mevalar=["olma","banan","uzum"]
# for index,meva in enumerate(mevalar,1):
#     print(f"{index}.{meva}")


# print(dict(enumerate(mevalar,1)))




# user=input("Hafta kuni:\n")
# day=int(input("Nechchi:\n"))
# if any([user=='Yakshanba',day>5]):
#     print("Konsertga kettik")
# else:
#     print("Konsertga borolmayman")




# def tashqi(x):
#     def ichki(y):
#         return x-y
#     return ichki

# addf=tashqi(12)
# print(addf(5))
# print(type(addf))






# def login(p):
#     parol='123'
#     def check():
#         return parol==p
#     return check

# a=input("Parol kiriting:\n")
# m=login(a)
# if m():
#     print("Tizimga kirdingiz")
# else:
#     print("Parol xato")








# def change(a):
#     b=a.count('i')
#     c=a.replace('a','o')
#     return b,c

# x=input("Nimadur:\n")
# print(change(x))








# def hisoblagich():
#     son=0

#     def qoshish():
#         nonlocal son
#         son+=1
#         if son==5:
#             son=1
#         return son
    
#     return qoshish

# hisob=hisoblagich()
# print(hisob())
# print(hisob())
# print(hisob())
# print(hisob())
# print(hisob())
# print(hisob())






# def fun(*args,**kwargs):
#     print(args,kwargs)


# print(fun(2,4,5,6,2,3,b=5))





# def upper_dec(a):
#     def wr(*args,**kwargs):
#         print("Starting...")
#         jav=a(*args,**kwargs)
#         print("Welcome")
#         return jav
    
#     return wr

# @upper_dec
# def player(a):
#     print(f"Access for {a}..")
#     return f"{a}!"


# c=input("Your name:\n")
# b=player(c)
# print(b)




# def upper_dec(func):
#     def wrapper(*args,**kwargs):
#         print("kod wrapperda")
#         javob=func(*args,**kwargs)
#         print("kod asosiyda")
#         return javob
#     return wrapper

# @upper_dec
# def soz(m):
#     print('kod sozga keldi')
#     return m

# s=input("Nimadur:")
# n=soz(s)
# print(n)







# def dec(fun):
#     def wrap(*args,**kwargs):
#         a=fun(*args,**kwargs)
#         return a**2
#     return wrap

# @dec
# def son(a):
#     return a

# x=int(input("Son:\n"))
# print(son(x))






# def konvert(dollar):
#     imena=set()
#     def davat(imya,summ):
#         if imya in imena:
#             print("Ti zadolbal")
#         else:
#             print("Eto tibe")
#             imena.add(imya)
#             dollar(imya,summ)
#             print("Beregi eto")
#     return davat

# @konvert
# def kupyura(name,a):
#     print(f"{name}, tut {a} dollarov")


# imya=input("Kak tebya zovut:\n")
# money=int(input("Skolko mne tebe dat:\n"))
# print(kupyura(imya,money))





# def deco(fun):
#     def oops(*args,**kwargs):
#         print("Hello!")
#         answ=fun(*args,**kwargs)
#         return answ*10
#     return oops

# @deco
# def num(a):
#     return a

# i=int(input("The number:\n"))
# print(num(i))

















