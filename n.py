m=int(input("Enter the number:"))
count=0
if m==1:
    print("not prime")
else:
    for i in range(2,m):
        if m%i==0:
            count+=1
    if count==0:
        print("prime")
    else:
         print("not prime")
        
