# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# print(kocha.capitalize(),mahalla.upper(),tuman.lower(),viloyat.capitalize())




# a=int(input("Yoshingiz:\n"))
# print(f"Siz {2025-a}-yilsiz")




# taomlar=["Osh","Xonim","Tuxum","Shirguruch","Mastava"]
# nonushta=taomlar.copy()
# del nonushta[0:2]
# nonushta.remove("Mastava")
# nonushta.extend(["Moshxo'rda","Makaron"])
# print(taomlar)
# print(nonushta)



#                     1
# def son(a):
#     for i in range(a):
#         if i<10:
#             i=10
#         if i%2==1:
#             toq.append(i)
# toq=[]
# son(100)
# kublar=[]
# for i in toq:
#     kublar.append(i**3)
# print(kublar)

#                      2
# for a in range(100):
#     if a<10:
#         a=10
#     if a%2==1:
#         toq.append(a)
# kublar=[]
# for i in toq:
#     i**=3
#     kublar.append(i)
# print(kublar)




# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for i in cars:
#     if i=='gm':
#         print(i.upper())
#     else:
#         print(i.capitalize())




# son=0
# while True:
#     son=input("Son kiriting (yoki stop):\n")
#     if son=='stop':
#         break
#     son=int(son)
#     if son>=0:
#         son**=2
#         print(son)
#     elif son<0:
#         print("Musbat son kiriting")




# age=int(input("Yoshingiz:\n"))
# chipta='0'
# val=''
# if age<4 or age>60:
#     chipta='bepul'
# elif age<18:
#     chipta=int(chipta)
#     chipta=10000
#     val="so'm"
# elif age>=18:
#     chipta=int(chipta)
#     chipta=20000
#     val="so'm"
# print(f"Assalomu alaykum sizga kirish {chipta} {val}")




# taom={}
# for a in range(5):
#     taom[input(f"{a+1}-ism:\n")]=input(f"{a+1}-taom:\n")
# for k,v in taom.items():
#     print(f"{k} sevadi {v}ni")



# menu={'Osh':25000,"Dimlama":50000,"Qozonkabob":45000,"Shashlik":12000,"Non":5000,"Salat":15000,"Hot-Dog":13000,"Ramyo'n":10000,"Lag'mon":35000}
# summa=0
# for i in range(3):
#     a=input(f"{i+1}-ga nima buyurtma qilasiz:\n")
#     if a in menu:
#         summa+=menu[a]
#     else:
#         print("Bizda bunday taom yo'q")
# print(summa)



# def maxn(x,y):
#     return max(x,y)

# a=int(input("1-son:\n"))
# b=int(input("2-son:\n"))

# print(maxn(a,b))




while True:
    a=int(input("1)Mijoz qo'shish\n2)Tugatish"))
    if a==1:
        mijozlar=[]

        def mijozlarf(ism,fam,tyil,tjoy,*args):
            mijoz={}
            mijoz["Ismi"]=ism
            mijoz["Familiyasi"]=fam
            mijoz["Tug'ilgan yili"]=tyil
            mijoz["Yoshi"]=2025-tyil
            mijoz["Tug'ilgan joyi"]=tjoy
            mijoz["Kontakt info"]=args
        
            mijozlar.append(mijoz["Ismi"])
            return mijozlarf
        def dic(name):
            return  

        ism=input("Ismingiz:\n")
        fam=input("Familiyangiz:\n")
        tyil=int(input("Tug'ilgan yilingiz:\n"))
        tjoy=input("Tug'ilgan joyingiz:\n")
        email=input("E-mailingiz(Enter to skip):\n")
        tnum=input("Raqamingiz(Enter to skip):\n")

        print(mijozlarf(ism,fam,tyil,tjoy,email,tnum))
    elif a==2:
        print(f"Mijozlar:{mijozlar}")
        b=int(input("1)Mijozni ko'rish\n2)Tugatish"))
        if b==1:
            






