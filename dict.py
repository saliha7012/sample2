x=[34,'word',4.5,'code',89,9.0]
for i in x:
    if type(i) is int:
        print("int :",i)
    elif type(i) is str:
        print("str :",i)
    elif type(i) is float:
        print("float :",i)
    else:
        break            