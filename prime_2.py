n=int(input("Enter the end of sequence:"))
f=0
if n>1:
    i=1
    while i<n:
        i+=1 
        if (n%i)==0:
            f+=1
        else:
            f+=0
if f==1:
    print(n,"is prime")
else:
    print(n,"is not prime")
