s="happy coding"
v={'a','e','i','o','u'}
x=""
y=""
if s.upper():
    s.lower()
for i in s:
    if i in v:
        x+=i
    else:
        y=y+i
print(y)                