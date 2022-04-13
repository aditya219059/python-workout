'''m=int(input("Enter the number of times:"))
a=[]
for i in range(m):
    n=int(input())
    a.append(n)
print(a)'''
a=list(map(int,input("Enter the multiple numbers:").split()))
for j in a:
    count=0
    for p in range(2,j):
        if j%p==0:
            count+=1
            print(j,"is not prime")
            break
    if count<1:
        if j==1:
            print(j,"is not prime")
        else:
            print(j,"is prime")
    
