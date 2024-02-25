t=('abc',567,'python','try',87)
s=()
for i in t:
    if type(i) is str:
        s=i[::-1]
        print(s)
    if type(i) is int:
        s=0
        while i!=0:
            d=i%10
            s=s*10+d
            i//=10
        print(s)
    