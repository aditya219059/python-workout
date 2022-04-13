n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))

for j in range(n,m):
    if j>1:
        count=0
        for i in range(1,j):
            if j%i==0:
                count+=1
        if count<=1:
            print(j,"is prime")
    
