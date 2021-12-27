'''n=int(input("enter the number:"))
for i in range(n):
    for j in range(1,n-i+1):
        print(j,end=" ")
    print("\r")'''
n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\r")
