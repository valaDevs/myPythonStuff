sumSquare = 0
num = int(input("Enter numbers 0 to End : "))
while num != 0:
    sumSquare += num ** 2
    num = int(input("Enter a number 0 to End : "))
print("Sum of square is", sumSquare)