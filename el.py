u=float(input("Enter the number of units consumed:"))
if u<=100:
    print("Your total electricity bill:Rs 0")
elif u>100 and u<200:
    print("Your total electricity bill:Rs",(u-100)*5)
elif u>=200:
    un=(u-200)*20+500
    print("Your total electricity bill:Rs",un)
    
