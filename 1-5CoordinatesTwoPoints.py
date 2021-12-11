import math

x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))

d = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
print("Distance is : {0:8.2f}".format(d))
