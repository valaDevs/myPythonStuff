# take width and length of rectangle from user to calculate the area and perimeter of rectangle
length = int(input("Enter rectangle length : "))
width  = int(input("Enter rectangle width : "))

# Area
area = length * width

# perimeter
perimeter = (length + width) * 2

# the (end) keyword prevernts line break , prints output in one line 
print("The area of rectangle is ",area, end=", ")
print("The perimeter of rectangle is ", perimeter)



