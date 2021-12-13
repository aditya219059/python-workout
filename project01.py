q=input("Do you wanna play this quiz:") 
s=0
if q=='yes' or q=='YES' or q=='Yes' or q=='Y' or q=='y':
    print("####Your quiz question will be related to science.")
    print("###Let's start###")
    print("Q1. what is the chemical formulae of water ?")
    a="CO2"
    b="H2O"
    c="NO2"
    d="MnO2"
    print("1.",a)
    print("2.",b)
    print("3.",c)
    print("4.",d)
    n=input("Enter your option number:")
    if n=='2' or n=='b':
        s+=10
        print("***your answer is right ,you are rewarded with 10 points.")
    else:
        s+=0
        print("***your answer is wrong ,you get zero point.")
    print("Your score",s,"/ 50")
    print("Q2. what is the chemical formulae of ozone?")
    a1="CO2"
    b1="KMnO3"
    c1="O3"
    d1="MnO2"
    print("1.",a1)
    print("2.",b1)
    print("3.",c1)
    print("4.",d1)
    n1=input("Enter your option number:")    
    if n1=='3' or n1=='c':
        s+=10
        print("***your answer is right ,you are rewarded with 10 points.")
    else:
        s+=0
        print("***your answer is wrong ,you get zero point.")
    print("Your score",s,"/ 50")
    print("Q3. what is the chemical formulae of pottasium carbonate ?")
    a2="CO2"
    b2="H2O"
    c2="NO2"
    d2="KCo3"
    print("1.",a2)
    print("2.",b2)
    print("3.",c2)
    print("4.",d2)
    n2=input("Enter your option number:")
    if n2=='4' or n2=='d':
        s+=10
        print("***your answer is right ,you are rewarded with 10 points.")
    else:
        s+=0
        print("***your answer is wrong ,you get zero point.")
    print("Your score",s,"/ 50")
    print("Q4. what is the chemical formulae of calcium carbonate ?")
    a3="CCo3"
    b3="H2O"
    c3="NO2"
    d3="MnO2"
    print("1.",a3)
    print("2.",b3)
    print("3.",c3)
    print("4.",d3)
    n3=input("Enter your option number:") 
    if n3=='1' or n3=='a':
        s+=10
        print("***your answer is right ,you are rewarded with 10 points.")
    else:
        s+=0
        print("***your answer is wrong ,you get zero point.")
    print("Your score",s,"/ 50")
    print("Q5. what is the chemical formulae of pottasium permanganete ?")
    a4="CCo3"
    b4="H2O"
    c4="NO2"
    d4="KMnO4"
    print("1.",a4)
    print("2.",b4)
    print("3.",c4)
    print("4.",d4)
    n4=input("Enter your option number:") 
    if n4=='4' or n4=='d':
        s+=10
        print("***your answer is right ,you are rewarded with 10 points.")
    else:
        s+=0
        print("***your answer is wrong ,you get zero point.")
    print("Your total score is ",s,"/  50")    
    if s==50:
        print("***Perfect job***")
        print("***You will be rewarded with $100")
    elif s==40:
        print("***Great job***")
        print("***You will be rewarded with $75")
    elif s==30:
        print("***Good job")
        print("***You will be rewarded with $50")
    elif s==20:
        print("***You passed the quiz ,but work hard***")
        print("***You will be rewarded with $25")
    elif s<=10:
        print("***You failed the quiz ,Work much harder***")
        print("***You don't get any reward")
else:
    print("####BYE BYE####")
