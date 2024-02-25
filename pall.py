s=input("enter a word:")
for i in s:
    if s==s[::-1]:
        print("yes!",s,"is pallindrome")
    break    