sum = 0
num = int(input("Enter a number 0 to Exit"))

while num != 0:
    sum += num ** 2
    num = int(input("Enter a number 0 to Exit : "))
    
print("The sum of numbers is : ", sum)