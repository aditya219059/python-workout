#program to print the simple interest and compound interest. 
p=float(input("Enter the Principal Amount: "))
r=float(input("Enter the Rate of interest: "))
t=float(input("Enter the Time Period(months): "))
#formulae for simple interest. 
si=(p*r*t)/100
print("Simple Interest: ",si)
n=int(input("Enter the numbers of times Interest applied: "))
#formulae for compund interest.
ci=p*(1+r/n)**t
print("Compound Interest: ",ci)
