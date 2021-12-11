import math

# area of circle formula ==> r * 3.14 ** 2
# r ==> stands for radius

r = float(input("Enter the circle radius : "))

area = math.pi * r ** 2

print("radius", "area", sep = 5 * " ")
print(r,area, sep = 7 * " ")

# sep ==> stands for seprate and pust empty cells for output 