print("***Welcome to your friendly claculator***")
n=int(input("How many times you want to calculate:"))
print("1.circle")
print("2.square")
print("3.rectangle")
print("choose one option from above")
i=0
while i<n:
    ch=int(input("Whose area you want to find :"))
    if ch==1:
      r=int(input("Enter the radius of the circle:"))
      a=r*r*3.14
      print("Area of the circle:",a)
      i+=1
    elif ch==2:
      s=int(input("Enter the side of square:"))
      a=s*s
      print("Area of the square:",a)
      i+=1
    elif ch==3:
      l=int(input("Enter the length of rectangle:"))
      b=int(input("Enter the breadth of rectangle:"))
      a=l*b
      print("Area of the rectangle:",a)
      i+=1
    else:
      print("***Wrong choice***")
      c=input("Do you want to continue calculating (y/n)")
      if c=='y' or ch=='Y':
          i+=0
      else:
          print("End of the program")
          i=n
