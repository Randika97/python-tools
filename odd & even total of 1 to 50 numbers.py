eventot = 0
oddtot = 0
count = 1
while(count < 51):
    if count%2:
        eventot=eventot+count
    else:
        oddtot=oddtot+count
    count=count+1
print("Even Total is :",eventot)
print("Odd Total is :",oddtot)
