x=input("enter Name:")
y=input("Enter Leaves:")
if int(y)<=5:
    print(x,"Yes","R.S 50000")
elif int(y)<=10:
    print(x,"Yes","R.S 40000")
elif int(y)<=15:
    print(x,"Yes","R.S 30000")
elif int(y)<=20:
    print(x,"Yes","R.S 20000")
elif int(y)>20:
    print(x,"No","R.S 0.00")
    
