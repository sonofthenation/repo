# def fun(a):
#     if a%2==1:
#         print("Bu toq son")
#     else:
#         print("Bu juft son")
# son=int(input("Son kiriting\n"))
# fun(son)

# def func(a):
#     b=0
#     for i in a:
#         if i>b:
#             b=i
#     print(b)
# sonlar=[3,5,7,9,1,10,34,99,1]
# func(sonlar)

# def f(*args):
#     list1=[]
#     list2=[]
#     for i in args:
#         if type(i)==str:
#             list1.append(i)
#         elif type(i)==int:
#             list2.append(i)
#     print(list1,list2)
# f(2,'salom',3,6)

# def get_info(ism,age):
#     print(f'Assalomu alaykum ismi:{ism} yoshi:{age}') 

# get_info('Mirjamol',18)
# get_info('Bobur',22)
# get_info()
# get_info()


# def get_address(a):
#     pul=input("Poraga qancha berasan: ")
#     job_addres='city'
#     print(f"Yashash manzilingiz {a}, bizni manzil {job_addres} otilding:{pul}")


# savol=input("Qayerda turasiz: ")
# get_address(savol)


# def salom(a):
#     print(f"Salom {list(a)}")


# b=input("Ism:\n")
# salom(b)




# def son(a):
#     if a%2==1:
#         print("Bu toq son")
#     else:
#         print("Bu juft son")

# b=int(input("Son kiriting:\n"))
# son(b)


# def max(son):
#     a=0
#     for i in son:
#         if i>a:
#             a=i
#     print(a)


# sonlar=[3,5,7,9,1,10,34,99,22]
# max(sonlar)




# def aralash(*args):
#     args=list(args)
#     print(args)

# aralash(2,2,45,23,4,256,35)

sonlar=[]
harflar=[]

def f(*args):
    for a in args:
        if str(a).isdigit():
            sonlar.append(a)
        else:
            harflar.append(a)
    print(sonlar,harflar)



f(2,'salom',3,6)




