pr=input("Enter the name of the product:")
cp=float(input("Enter the cost price of product:"))
rp=float(input("Enter the extra amount invested in product:"))
sp=float(input("Enter the sell price of product:"))

if (cp+rp)<sp:
    gp=((s-(cp+rp))*100)/cp
    print("Gain percentage:",gp,"%")
else:
    lp=((cp+rp)-sp)*100/cp
    print("Loss percentage:",lp,"%")
