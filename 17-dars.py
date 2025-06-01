# class Dokon:
#     def __init__(self,title,*products):
#         self.title = title
#         self.products = list(products)



# class Zavod:
#     def __init__(self,title,*jihoz):
#         self.title = title
#         self.jihoz = list(jihoz)
#
#     def __getitem__(self,item):
#         return self.jihoz[item]
#
#     def __setitem__(self,it,val):
#         if it!=2:
#             self.jihoz[it] = val
#         else:
#             j="Mumkin emas"
#             print(j)
#
#     def index(self,item):
#         try:
#             return self.jihoz.index(item)
#         except Exception:
#             return "no"
#
#     def __delitem__(self,item):
#         x=''
#         if item==3:
#             del self.jihoz[item]
#             x=self.jihoz.sort()
#         return x
#
#
#
# a=Zavod('apple inc','stul','doska','kreslo','parta')
# print(a.index('stol'))
# a[2]='baklashka'
# del a[3]
# print(a[:])



class Dokon:
    def __init__(self,title,*prices,**prodcut):
        self.title=title
        self.prices=list(prices)
        self.product=prodcut

    @classmethod
    def check_int(cls, x):
        return isinstance(x, int)

    def check_str(cls, x):
        return isinstance(x, str)

    def __getitem__(self, item):
        if self.check_int(item):
            return self.prices[item]
        if self.check_str(item):
            return self.product.get(item,"bunday mahsulot yoq")


    def __setitem__(self, key,value):
        if self.check_int(key):
            self.prices[key] = value
        if self.check_str(key):
            self.product[key]=value

    def __delitem__(self,k):
        if self.check_int(k):
            del self.prices[k]
        if self.check_str(k):
            del self.product[k]


o=Dokon('cola',12,23,34,45,45,56,choy=200,non=500,suv=600)
o['non']=7000
o[1]=55
print(o['choy'])
del o[2]
del o['non']
print(o.__dict__)
print(o[2])




