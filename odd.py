l=[45,62,2,67,3,34,93,101]
s=[]
for i in range(0,len(l)):
    if(l[i]%2==0):
        continue
    else:
        s.append(l[i])
print(s)        