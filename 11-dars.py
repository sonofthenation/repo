

# try:
#     my_file=open('salom.txt','a+')
#     try:
#         print("Fayllar bilan ishlash")
#     finally:
#         my_file.close()
# except Exception as x:
#     print("Xatolik:",x)



# with open('bugun.txt','w+') as my_file:
#     my_file.write("bugun dushanba")
#     print('hammasi ishladi')
#
#
#
# with open('bugun.txt','a') as my_file:
#     my_file.write('\nertaga seshanba')
#
# with open('bugun.txt','r') as my_file:
#     print(my_file.read())

# while True:
#     with open('user.txt','a+') as user:
#         a=input("Nimuadur yozing:\n")
#         if a=='stop':
#             with open('user.txt', 'r') as user:
#                 print(user.read())
#             break
#         user.write(f'{a} malumot qo\'shildi\n')
# with open('hello.txt','a') as myfile:
#     print("\nhello docker.com",file=myfile)
# with open('hello.txt','w+') as file:
#     a=input('Ism:\n')
#     b=input('Age:\n')
#     c=input('Address:\n')
#     file.write(a+'\n')
#     file.write(b+'\n')
#     file.write(c+'\n')
# with open('hello.txt','r') as file:
#     a=file.read()
#     print(a)
# file.close()






# with open('myfile.txt','w+') as myfile:
#     myfile.write('Привет\nЭто тестовый файл\nПока')
# with open('myfile.txt','r') as myfile:
#     print(myfile.read())
    # a = myfile.readline()
    # b = myfile.readline()
    # c = myfile.readline()
    # print(a + b + c)
    # a=myfile.readlines()
    # for x,l in enumerate(a,1):
    #     print(x,l.strip())


# with open('hello.txt','r') as file:
#     line = file.readline()
#     while line:
#         print(line,end="")
#         line = file.readline()
#     a=input('Ism:\n')
#     b=input('Age:\n')
#     c=input('Address:\n')
#     lis=[a,b,c]
#     for x in lis:
#         file.write(x+'\n')
# with open('hello.txt','r') as file:
#     a=file.read()
#     print(a[:3])
#     if 'ali'==a[:3]:
#         print("malades")
#     else:
#         print("kalla")
# file.close()


# FILENAME="messenger.txt"
#
#
# def yoz():
#     matn=input("Matn kiriting: ")
#     with open(FILENAME,"a") as file:
#         file.write(matn+'\n')
#
# def oqi():
#     with open(FILENAME,"r") as file:
#         for i in file:
#             print(i,end="")
#
# def tamom():
#     with open(FILENAME,"r") as file:
#         file.close()
#
# while True:
#     try:
#         m=int(input("1-Yozish 2-O'qish 3-Tugatish:\n"))
#         if m==1:
#             yoz()
#         elif m==2:
#             oqi()
#         elif m==3:
#             tamom()
#             break
#         else:
#             print("To'g'ri kiriting")
#     except ValueError:
#         print("To'g'ri kiriting")







