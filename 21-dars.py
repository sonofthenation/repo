# from abc import ABC, abstractmethod
#
# class Action(ABC):
#     @abstractmethod
#     def action(self):
#         pass
#
# class



# Library title,genre,location
# cataolog,book,magazine,audiobook,display
# from abc import ABC, abstractmethod
#
#
# class LibraryItem(ABC):
#     def __init__(self, title, genre):
#         self.title = title
#         self.genre = genre
#
#     @abstractmethod
#     def locate(self):
#         pass
#
#
# class Book(LibraryItem):
#     def __init__(self, title, genre, isbn, authors):
#         super().__init__(title, genre)
#         self.isbn = isbn
#         self.authors = authors
#
#     def locate(self):
#         return f"Kitoblar bo'limida joy olgan"
#
#
# class Magazine(LibraryItem):
#     def __init__(self, title, genre,volume):
#         super().__init__(title, genre)
#         self.volume = volume
#
#     def locate(self):
#         return f"Jurnallar bo'limida joy olgan"
#
# class Audiobook(LibraryItem):
#     def __init__(self, title, genre, time):
#         super().__init__(title, genre)
#         self.time = time
#
#
#     def locate(self):
#         return f"Audio bo'limida joy olgan"
#
# class DisplayBook(LibraryItem):
#     def __init__(self, title, genre, type_dvd):
#         super().__init__(title, genre)
#         self.type_dvd = type_dvd
#
#     def locate(self):
#         return f"Displaylar bo'limida joy olgan"
#
#
# class Catalog:
#     def __init__(self):
#         self.books = []
#
#
#     def add(self, item):
#         self.books.append(item)
#
#     def __str__(self):
#         return self.books
#
# def brain_stop():
#     cat = Catalog()
#     print("""
#     1 Add book
#     2 Add magazine
#     3 Add audiobook
#     4 Add displaybook
#     5 exit
#     """)
#     while True:
#         # brain_stop()
#         nums=input("Enter your choice: ")
#         n=["1","2","3","4"]
#         if nums in n:
#             title = input("Enter title(back for back): ")
#             genre = input("Enter genre: ")
#             if nums == "1":
#                 isbn=input("Enter ISBN: ")
#                 authors=input("Enter authors: ")
#                 item=Book(title, genre, isbn, authors)
#                 print(item.locate())
#             elif nums == "2":
#                 volume=input("Enter volume: ")
#                 item=Book(title,genre,volume)
#                 print(item.locate())
#             elif nums=="3":
#                 time=input("Enter time: ")
#                 item = Book(title, genre, time)
#                 print(item.locate())
#             elif nums=="4":
#                 type_dvd=input("Enter type: ")
#                 item = Book(title, genre, type_dvd)
#                 print(item.locate())
#
#             cat.add(item)
#             print(cat.books)
#
#
#
# brain_stop()


# Library title,genre,location
# cataolog,book,magazine,audiobook,display
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    count = 0

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        LibraryItem.count += 1

    @abstractmethod
    def locate(self):
        pass

    @classmethod
    def count_get(cls):
        return cls.count

    @abstractmethod
    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, genre, isbn, authors):
        super().__init__(title, genre)
        self.isbn = isbn
        self.authors = authors

    def locate(self):
        return f"Kitoblar bo'limida joy olgan"

    def get_info(self):
        return f"{self.title} {self.genre} {self.authors}"


class Magazine(LibraryItem):
    def __init__(self, title, genre, volume):
        super().__init__(title, genre)
        self.volume = volume

    def locate(self):
        return f"Jurnallar bo'limida joy olgan"

    def get_info(self):
        return f"{self.title} {self.genre} {self.volume}"


class AudioBook(LibraryItem):
    def __init__(self, title, genre, time):
        super().__init__(title, genre)
        self.time = time

    def locate(self):
        return f"Audio bo'limida joy olgan"

    def get_info(self):
        return f"{self.title} {self.genre} {self.time}"


class DisplayBook(LibraryItem):
    def __init__(self, title, genre, type_dvd):
        super().__init__(title, genre)
        self.type_dvd = type_dvd

    def locate(self):
        return f"Displaylar bo'limida joy olgan"

    def get_info(self):
        return f"{self.title} {self.genre} {self.type_dvd}"


class Catalog:
    def __init__(self):
        self.books = []

    def add(self, item):
        self.books.append(item)

    def get_books(self):
        jami = [item.get_info() for item in self.books]
        return jami

    def search(self, keyword):
        jami_list = []
        for obj in self.books:
            if obj.title == keyword or obj.genre == keyword:
                jami_list.append(obj)
        javob = [item.locate() for item in jami_list]
        return javob


def brain_stop():
    cat = Catalog()
    print("""
    1 Add book
    2 Add magazine
    3 Add audiobook
    4 Add displaybook

    5 view
    6 search
    """)
    while True:
        nums = input("Enter your choice: ")

        if nums == "1":
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            isbn = input("Enter ISBN: ")
            authors = input("Enter authors: ")
            item = Book(title, genre, isbn, authors)
            print(item.locate())
            cat.add(item)
        elif nums == "2":
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            volume = input("Enter volume: ")
            item = Magazine(title, genre, volume)
            print(item.locate())
            cat.add(item)

        elif nums == "3":
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            time = input("Enter time: ")
            item = AudioBook(title, genre, time)
            cat.add(item)

        elif nums == "4":
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            type_dvd = input("Enter type: ")
            item = DisplayBook(title, genre, type_dvd)
            cat.add(item)
            print(item.locate())
        elif nums == "5":
            print(cat.get_books())
        elif nums == "6":
            keyword = input("Enter keyword: ")
            print(cat.search(keyword))


brain_stop()




