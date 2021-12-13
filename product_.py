p=int(input("price of the product:"))
if p<1000:
    amt=p-(p*(5/100))
    print("Net payable amount:",amt)
elif p>4000 and p<5000 :
    amt=p-(p*(10/100))
    print("Net payable amount:",amt)
else:
    print("You don't get any discount")
    print("your net payable amount:",p)
