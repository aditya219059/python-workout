def num(n,m):
    count=0
    while n>0:
        temp=n%10
        n=n//10
        if temp==m:
            count+=1
    return count

a=int(input("Enter:"))
b=int(input("Enter digit:"))
print("Frequency:",num(a,b))
