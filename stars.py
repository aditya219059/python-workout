'''n=int(input("Enter the number:"))
for i in range(n+1):
    print(i*"*")
for j in range(n-1,0,-1):
    print(j*"*")'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")    
for i in range(n,1,-1):
    for j in range(i-1):
        print("*",end=" ")
    print(" ")    
