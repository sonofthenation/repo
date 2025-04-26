# tuple


# user={}
# user[input('Ismingiz:\n')]=input('Yoshingiz:\n')
# print(user)

# week={
#     ('Dushanba','Chorshanba','Juma'):"O'qish",
#     ('Seshanba','Payshanba','Shanba'):"Dam"
# }
# print(week.keys)
# print(week.items)
# print(week.values)
# print(list(week.items))

x=0
y=0
soni=int(input("Nechta tovar olay:\n"))
bozorlik=set()
for a in range(soni):
    tovar=input(f"{a+1}-tovar nomi:\n")
    bozorlik.add(tovar)
bozorlik=list(bozorlik)
korzinka={
    "non":5000,
    "sut":15000,
    "olma":10000,
    "cola":17000
}
summa=[]
tovr=[]
for b in bozorlik:
    if b in korzinka:
        summa.append(korzinka[b])
        tovr.append(b)
        if x<int(korzinka[b]):
            x=int(korzinka[b])
            y=b
    else:
        print(f"{b} bizda yo'q")
print(f"Sizdan jami {sum(summa)} sum\nSiz harid qilgan tovarlar:\n{tovr}\nEng qimmat tovar: {y} - {x} so'm")


