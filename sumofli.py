n=[73,103,66,98]
l=[]
for i in n:
    s=0
    for j in str(i):
        s=s+int(j)
    l.append(s)
print(l)        