def s(p):
    sp=0
    for i in range(0,p):
        sp += ((-1)**i) * i
        if sp == 7 or sp == -7:
            print(i)

s(1500)
