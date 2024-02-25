w="grass is greener on the other side"
s=""
r=""
x=""
c=""
if w.upper():
    w=w.lower()
for i in w:
    if i not in s:
        s=s+i
    else:
        r=r+i
        r=r.replace(" ",'') 
c={}
for j in r:
    if j in c:
        c[j]+=1
    else:
        c[j]=1
m=0
mr= ""
for j, c in c.items():
    if c>m:
        m=c
        mr=j       
print("most repeated letter is",mr)
