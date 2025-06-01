# 2 та режим
# админ(кирганда логин и пароль сураб текширади): студент кушиш, тичер кушиш, курс яратиш, вазифа яратиш(,вазифа текшириш)
# студент: курс танлиди, тичер берилади, айди берилади, менинг курсларим, менинг уй вазифам (,вазифа юклаш, жараённи куриш)

import random

class Ustudy:
    students=[]
    teachers=[]
    courses=set()
    home_tasks={}
    task_answers={}
    task_status={}
    CONST=""
    passwuses=1

    @classmethod
    def age(cls,name):
        for a in cls.students:
            if a.name==name:
                return a.age
            else:
                return "Xato"

    @classmethod
    def aget(cls,name):
        for a in cls.teachers:
            if a.name==name:
                return a.age
            else:
                return "Xato"

class Admin(Ustudy):
    def __init__(self,login):
        self.__login=login
        if Ustudy.passwuses!=0:
            self.__password=Admin.randp()
        else:
            self.__password=Ustudy.CONST




    def authol(self,login):
        return self.__login==login

    @staticmethod
    def randp():
        x=""
        HARF = "qwertyuiopasdfghjklzxcvbnm"
        UHARF = HARF.upper()
        for a in range(7):
            x+=random.choice([random.choice(HARF),random.choice(UHARF),str(random.randint(0,9))])
        return x

    def authop(self,passw):
        return self.__password==passw

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,const):
        if Ustudy.passwuses!=0:
            Ustudy.CONST=const
            self.__password=Ustudy.CONST
            Ustudy.passwuses = 0

    @classmethod
    def addstud(cls,obj):
        cls.students.append(obj)
        return f"Student qo'shildi!"


    @classmethod
    def addteach(cls,obj):
        if obj.spec in cls.courses:
            cls.teachers.append(obj)
            return "Teacher kursga tayinlandi!"
        else:
            return "Bizda bunday kurs yo'q!"

    @classmethod
    def addcourse(cls,course):
        cls.courses.add(course)




class Teacher(Admin):
    mystud = []
    def __init__(self,name,age,spec):
        self.name=name
        self.age=age
        self.spec=spec
        # super().__init__(login)
        # self.login=login
        self.__password=Ustudy.CONST
        # self.authop(password)

    @property
    def profile(self):
        son=len(Teacher.mystud)
        for a in Ustudy.students:
            if a.course==self.spec:
                son+=1
                Teacher.mystud.append(a)
        return f"""
        Teacher ismi: {self.name}
        Teacher yoshi: {self.age}
        Teacher yo'nalishi: {self.spec}
        Teacher studentlari soni: {son}
"""

    @property
    def my_students(self):
        for i in Teacher.mystud:
            print(f"""
            Student ismi: {i.name}
            Student yoshi: {i.age}
            Student id: {i.id}
""")

    def authop(self,passw):
        return self.__password==passw

    @classmethod
    def spec(cls,name):
        for k in cls.teachers:
            if k.name==name:
                return k.spec
            else:
                return None

    @classmethod
    def addtask(cls,course,task):
        cls.home_tasks[course]=task
        cls.task_answers[task]=""

    @classmethod
    def check_task(cls):
        print(cls.task_answers)
        for k,v in cls.task_answers.items():
            print(v)
            a=input("""To'grimi?
            1 HA\t2 YO'Q: """)
            if a=="1":
                Ustudy.task_status[k]="Barakalla! To'ppa to'g'ri!"
            elif a=="2":
                Ustudy.task_status[k]="Noto'g'ri, qayta urining!"


class Student(Ustudy):
    tan='Tanlanmagan'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.id = self.get_id
        self.course=self.getcourse
        self.teacher=self.getteacher
        Ustudy.students.append(self)

    @classmethod
    def check(cls,name):
        return name in cls.students

    @property
    def getcourse(self):
        course=input(f"Kurs tanlang {Ustudy.courses}: ")
        self.course=Student.tan
        if course in Ustudy.courses:
            self.course=course
        return self.course


    @property
    def getteacher(self):
        self.teacher=Student.tan
        for b in Ustudy.teachers:
            if b.spec==self.course:
                self.teacher=b.name
        return self.teacher

    @property
    def get_id(self):
        id=random.randint(1000000,9999999)
        return id


    @classmethod
    def profile(cls,name):
        for a in cls.students:
            if a.name==name:
                return f"""
                Student ismi: {a.name}
                Student kursi: {a.course}
                Student teacheri: {a.teacher}
                Student id: {a.id}
        """
            else:
                return None

    @classmethod
    def get_task(cls):
        return cls.task_answers

    def do_task(self,task,answer):
        Ustudy.task_answers[task]=answer
        Ustudy.task_status[task] = "Tekshirilmoqda..."

while True:
    ustudy=Ustudy()
    c=input("""
        1 ADMIN
        2 Student
        3 Teacher
        Tanlang: 
    """)
    if c == "1":
        obj = Admin("SPIDERMAN")
        a = input("Login: ")
        if ustudy.passwuses!=0:
            b = input(f"Password(bugungi password {obj.password}): ")
        else:
            b = input(f"Password: ")
        abc=obj.authol(a)
        ab=obj.authop(b)
        if abc and ab:
            print(f"{a}! Xush kelibsiz")
            if ustudy.passwuses != 0:
                x=input("Passwordni o'zgartiring: ")
                obj.password=x
                print("Muvaffaqiyat!")
        else:
            print("Qayta urining")
            continue
        while True:
            xy=input("""
            1 Kurs yaratish
            2 Teacher qo'shish
            3 Student qo'shish
            4 Chiqish
            Tanlang: 
            """)
            if xy=="3":
                objs=Student(input("Ismi: "),input("Yoshi: "))
                print(obj.addstud(objs))
            elif xy=="2":
                objt=Teacher(input("Teacher ismi: "),input("Yoshi: "),input("Yo'nalish: "))
                print(obj.addteach(objt))
            elif xy=="1":
                obj.addcourse(input("Kurs nomi: "))
                print(obj.courses)
            # elif xy=="4":
            #     obj.addtask(input("Qaysi kursning taski: "),input("""
            #     Task:
            #     """))
            #     print(obj.home_tasks)
            # elif xy=="5":
            #     obj.check_task()
            elif xy=="4":
                if input("""Tasdiqlaysizmi?
                1 HA\t2 YO'Q:\n""")=="1":
                    break
    elif c=="3":
        ism=input("Ismingiz: ")
        for ob in ustudy.teachers:
            if ism == ob.name:
                parol=input("Password: ")
                obj=Teacher(ism,ustudy.aget(ism),Teacher.spec(ism))
                if obj.authop(parol):
                    while True:
                        xy = input("""
                        1 Mening profilim
                        2 Vazifa yaratish
                        3 Vazifani tekshirish
                        4 Chiqish
                        Tanlang: 
                        """)
                        if xy=="1":
                            print(obj.profile,f"""
                            
                            1 Studentlarimni ko'rish
                            2 Ortga qaytish
                            Tanlang: 
    """)
                            a=input()
                            if a=="1":
                                print(obj.my_students)
                            elif a=="2":
                                continue
                            else:
                                print("Qayta urining!")
                        elif xy=="2":
                            obj.addtask(obj.spec,input("""
                            Task: 
                            """))
                        elif xy=="3":
                            obj.check_task()
                        elif xy=="4":
                            bb=input("""
                            Tasdiqlaysizmi?
                            1 HA\t2 YO'Q: 
                            """)
                            if bb=="1":
                                break
                            elif bb=="2":
                                continue
                            else:
                                print("Qayta urining!")
                        else:
                            print("Bunday buyruq yo'q")
                else:
                    print("Qayta urining")

    elif c=="2":
        a=input("Ismingiz: ")
        for ob in ustudy.students:
            if a==ob.name:
                while True:
                    xy = input("""
                    1 Mening profilim
                    2 Vazifa yuklash
                    3 Vazifa holatini ko'rish
                    4 Chiqish
                    Tanlang: 
                    """)
                    if xy=="1":
                        print(Student.profile(a))
                    elif xy=="2":
                        print(Ustudy.task_answers)
                        ob.do_task(input("Qaysi taskni bajarasiz: "),input("""
                        Javob yozing: 
                        """))
                    elif xy=="3":
                        print(ob.task_status)
                    elif xy=="4":
                        if input("""Tasdiqlaysizmi?
                        1 HA\t2 YO'Q:\n""") == "1":
                            break
                break

        else:
            print("Ismingiz topilmadi, adminga murojaat qiling!")
            continue










