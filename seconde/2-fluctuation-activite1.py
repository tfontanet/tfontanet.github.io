from random import *
n=100
m=1
M=0
for i in range(10):
    a=0
    for j in range(n):
        s=randint(1,6)+randint(1,6)+randint(1,6)
        if s>=13:
            a=a+1
    f=a/n
    print(f)
    if f<m:
        m=f
    if f>M:
        M=f
print(m,M)


