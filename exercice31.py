nombre=int(input("taper un entier n : "))

while nombre<0 :
    nombre=int(input("taper un entier (positif ou null): "))
U0=0
U1=1
for i in range(1,nombre+1):
    if i==1 :
        print(U1)
    else :
        Un=U1 +U0
        print(Un)
        U0=U1
        U1=Un
