def s(p):
    sp=0
    for i in range(0,p):
        sp += ((-1)**i) * i
    return sp

print(s(3))
print(s(4))
print(s(3))
