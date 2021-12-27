a=int(input("Enter integer:"))
b=a
for i in range(1,len(str(a))+1):
    a=b%10
    b=b//10
    print(a,"is at",i,"position")
