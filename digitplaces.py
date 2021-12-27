n=int(input("Enter the number:"))
ones=n%10
q=n//10
tens=q%10
q=q//10
hun=q%10
q=q//10
thous=q%10
q=q//10
tenthous=q%10
q=q//10
lakh=q%10
q=q//10
tenlakh=q%10
if ones!=0:
    print(ones,"is at ones place")
if tens!=0:
    print(tens,"is at tens place")
if hun!=0:
    print(hun,"is at hundreds place")
if thous!=0:
    print(thous,"is at thousands place")
if tenthous!=0:
    print(tenthous,"is at ten-thousands place")
if lakh!=0:
    print(lakh,"is at lakh place")    
if tenlakh!=0:
    print(tenlakh,"is at ten-lakh place")    
        

