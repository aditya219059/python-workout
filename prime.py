num=int(input("enter:"))
k=0
if num==0 or num==1:
    print("not prime")
else:
    i=2
    while (i<num):
        if num%i==0:
            k=k+1
        i=i+1


if k==0:
    print("prime")
else:
    print("not prime")
