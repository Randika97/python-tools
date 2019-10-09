def area(a):
    pi=3.14
    return pi*a**2
def circum(b):
    pi=3.14
    return 2*pi*b
r = float(input("Enter the radius of the circle : "))
print ("Area is "+ str(area(r)))
print ("circumference is "+ str(circum(r)))
