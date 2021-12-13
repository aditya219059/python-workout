amt=float(input("Enter the price of bike:"))
if amt<=50000:
    print("Road tax to be paid:",(.5*amt))
elif amt>50000 and amt<=100000:
    print("Road tax to be paid:",(.10*amt))
else:
    print("Road tax to be paid:",(.15*amt))
