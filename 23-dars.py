#
#
# with open('salom.txt', 'w') as file:
#     file.write('Hello world')
#     print("yaraldi")


# class Manager:
#     def __enter__(self):
#         print('enter')
#         return "Bu file"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#         if exc_type:
#             raise exc_type
#         return True
#
#
# with Manager() as manager:
#     print(manager)
# class File:
#     def __init__(self, filename,mode):
#         print('init')
#         self.filename = filename
#         self.mode=mode
#         self.file=None
#
#
#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename,self.mode)
#         return self.file
#
#     def __exit__(self, type, value, traceback):
#         print('exit')
#         # if type:
#         #     raise ValueError("bunda rejim xato")
#         if type:
#             self.file.close()
#         return True
#
#         # self.file.close()
#
# with File('test.txt','w') as file:
#     file.write('hello')


# import csv
#
# with open("new.csv",'w') as csvfile:
#     csv=csv.writer(csvfile)
#     csv.writerow(["A","B","C"])
#     csv.writerows([[1,2,3],[4,5,6]])
#     csv.writerow(["A","B","C"])
#     print(csv)



# import csv
#
# new_dict=[
#     {'Ism':'Ali','Yosh':20,'Kasb':'Dev'},
#     {'Ism':'Vali','Yosh':23,'Kasb':'Rassom'},
#     {'Ism':'Sli','Yosh':12,'Kasb':'Dev'},
#     {'Ism':'Alwei','Yosh':24,'Kasb':'Dev2rw'}
# ]
#
# with open("old.csv",'w',newline='') as csvfile:
#     fieldnames=['Ism','Yosh','Kasb']
#     writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(new_dict)
#     print('yozildi')
#
#
# with open("old.csv", 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)


class User:
    user=[]





