print("***Welcome to your friendly claculator***")
print("1.circle")
print("2.square")
print("3.rectangle")
print("choose one option from above")
ch=int(input("Whose area you want to find :"))
if ch==1:
   r=int(input("Enter the radius of the circle:"))
   a=r*r*3.14
   print("Area of the circle:",a)      
elif ch==2:
   s=int(input("Enter the side of square:"))
   a=s*s
   print("Area of the square:",a)
elif ch==3:
   l=int(input("Enter the length of rectangle:"))
   b=int(input("Enter the breadth of rectangle:"))
   a=l*b
   print("Area of the rectangle:",a)
else:
   print("***Wrong choice***")
    
