# def counter(n):
#     for i in range(1,n+1):
#         yield i
#
# b=int(input("Son: "))
# gen=counter(b)
# for a in iter(gen):
#     print(a)

# class Counter:
#     def __init__(self,start,end):
#         self.current=start
#         self.end=end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current>=self.end:
#             raise StopIteration
#         self.current+=1
#         return self.current-1
#
# coun=Counter(1,15)
# for n in coun:
#     print(n)

# class InfiniteNumbers:
#     def __iter__(self):
#         self.num=0
#         return self
#
#     def __next__(self):
#         self.num+=1
#         return self.num
#
# inf=InfiniteNumbers()
# it=iter(inf)
#
# print(next(it))
# print(next(it))
# print(next(it))



# class WaterDispatcher:
#     _instance=None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance=super().__new__(cls)
#             cls._instance.orders=[]
#         return cls._instance
#
#     def add_order(self,order):
#         self.orders.append(order)
#         print(f"Buyurtma qabul qilindi: {order}")
#
# disp1=WaterDispatcher()
# disp2=WaterDispatcher()
#
# disp1.add_order("12 ta suv etkazish")
# disp2.add_order("20 ta suv etkazish")
# print(disp1.orders,disp2.orders)
# print(disp1 is disp2)



# class European:
#     def connect(self):
#         return "eu Evropa VPNga ulandi"
#
# class US:
#     def __init__(self,vpn):
#         self.vpn=vpn
#
#     def conn(self):
#         return self.vpn.connect()+" -> AQSH VPNga ulandi"
#
# eur=European()
# a=US(eur)
# print(a.conn())

# class Observer:
#     def update(self, mess):
#         print(f"📢 Yangilik: {mess}")
#
# class NewsChannel:
#     def __init__(self):
#         self.subscribers = []
#
#     def subscribe(self, subscriber):
#         self.subscribers.append(subscriber)
#
#     def notify(self, message):
#         for subscriber in self.subscribers:
#             subscriber.update(message)
#
# # Obunachilar
# user1 = Observer()
# user2 = Observer()
#
# # Yangilik kanali
# channel = NewsChannel()
# channel.subscribe(user1)
# channel.subscribe(user2)
#
# channel.notify("Salom")





