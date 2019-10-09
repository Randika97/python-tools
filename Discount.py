x=input("Bill Amount R.s:")
if int(x)>15000:
    x=int(x)-int(x)*(20/100)
    print(x)
elif int(x)>10000:
    x=int(x)-int(x)*(10/100)
    print(x)
elif int(x)>5000:
    x=int(x)-int(x)*(5/100)
    print(x)
else:
    print(x)
    
