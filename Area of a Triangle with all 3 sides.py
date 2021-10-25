import math
x=int(input("Enter side 1: "))
y=int(input("Enter side 2: "))
z=int(input("Enter side 3: "))
s=(x+y+z)/2
area=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("Area of the triangle is: ",round(area,2))