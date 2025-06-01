import random

a=0
b=0
c=a+b
x=1
y=12
print("""
This game is played with bot and a player, you should type a number from 1 to 10, and the bot does the same,
and it compares to each other every time you and bot types a number alternately, untill it reaches to 100,
who first reaches it will win""")
while c<100:
    try:
        b=int(input(f"Num {x}:\n"))
    except ValueError:
        print("Try again")
        continue
    if not 1<=b<=10:
        print("Error")
        continue
    print(f"{c}+{b}={c+b}")
    c+=b
    if c<y:
        if b==1 and x==1:
            a=random.randint(1,10)
            print(a)
            c+=a
            print(f"{b}+{a}={c}")
            x+=1
            y+=11
            continue
        elif b>1 and x==1:
            a=12-b
            print(a)
            print(f"{c}+{a}={c+a}")
            c+=a
            x+=1
            y+=11
            continue
        if c>=100:
            break
        a=11-b
        print(a)
        print(f"{c}+{a}={c+a}")
        c+=a
    elif c==y:
        if c>=100:
            break
        a=random.randint(1,10)
        print(a)
        print(f"{c}+{a}={c+a}")
        c+=a
    x+=1
    y+=11