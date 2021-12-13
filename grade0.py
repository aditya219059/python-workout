name=input("enter your name:")
p=int(input("enter your obtained percent:"))
if (p<101 and p>90):
    print("grade obtained by ",name," is A+")
elif (p<91 and p>80):
    print("grade obtained by ",name,"is A")
elif (p<81 and p>70):
    print("grade obtained by ",name," is B")
elif (p<71 and p>60):
    print("grade obtained by ",name," is C")
elif (p<61 and p>50):
    print("grade obtained by ",name," is D")
elif (p<51 and p>40):
    print("grade obtained by ",name," is E")
else:
    print("grade obtained by ",name," is F")
    

