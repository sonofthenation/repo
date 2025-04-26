# import random

# son=random.randint(1,100)
# urinish=0
# while True:
#     user_answer=input('sonnin taxmin qilib koring:stop')
#     if user_answer=='stop':
#         break
#     urinish+=1
#     if urinish==5:
#         print(f'Siz topa olmadingiz {son} edi')
#         break
#     if int(user_answer)>son:
#         print('Kichikroq ayting')
#     elif int(user_answer)<son:
#         print('Kattaroq ayting')
#     else:
#         print(f'topdingiz {son} urinish soni {urinish}')
#         break

# import random

# tomon={'1':'chap uchun','2':"o'rta uchun",'3':'o\'ng uchun'}
# gol=0
# negol=0
# urinish=0
# liss=list(tomon.keys())
# while True:
#     varata=random.choice(liss)
#     user_attack=input(f'{tomon} qaysi tomonga tepasiz (stop):')
#     if user_attack=='stop':
#         print(f"gollar={gol},negol={negol},urinish={urinish}\nGol urish koeffitsienti:{gol/urinish*100}%")
#         break
#     if user_attack not in liss:
#         continue
#     urinish+=1
#     if user_attack==varata:
#         negol+=1
#         print('negol')
#     else:
#         gol+=1
#         print('gol')








import random

tomon={'1':'chap uchun','2':"o'rta uchun",'3':'o\'ng uchun'}
fp=input("Birinchi o'yinchi ismi:\n")
sp=input("Ikkinchi o'yinchi ismi:\n")
gol1=0
gol2=0
urinish=0
liss=list(tomon.keys())
while True:
    varata=random.choice(liss)
    if urinish==10:
            print(f"{fp}ning gollari={gol1}ta, {sp}ning gollari={gol2}ta, urinishlar={int(urinish/2)}tadan\nGol urish koeffitsientlari:\n{fp}--->{gol1/(urinish/2)*100}%\n{sp}--->{gol2/(urinish/2)*100}%")
            break
    if urinish%2==0:
        user_attack=input(f'{fp}, qaysi tomonga tepasiz {tomon} (yoki stop):\n')
        if user_attack=='stop':
            print(f"{fp}ning gollari={gol1}ta, {sp}ning gollari={gol2}ta, urinishlar={int(urinish/2)}tadan\nGol urish koeffitsientlari:\n{fp}--->{gol1/(urinish/2)*100}%\n{sp}--->{gol2/(urinish)/2*100}%")
            break
        if user_attack not in liss:
            continue
        urinish+=1
        if user_attack==varata:
            print('negol')
        else:
            gol1+=1
            print('gol')
    elif urinish%2==1:
        user_attack=input(f'{sp}, qaysi tomonga tepasiz {tomon} (yoki stop):\n')
        if user_attack=='stop':
            print(f"{fp}ning gollari={gol1}ta, {sp}ning gollari={gol2}ta, urinishlar={int(urinish/2)}tadan\nGol urish koeffitsientlari:\n{fp}--->{gol1/(urinish/2)*100}%\n{sp}--->{gol2/(urinish/2)*100}%")
            break
        if user_attack not in liss:
            continue
        urinish+=1
        if user_attack==varata:
            print('negol')
        else:
            gol2+=1
            print('gol')




