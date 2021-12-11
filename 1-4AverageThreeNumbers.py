print("Enter three numbers to calculate the average 😄")
firstNumber = int(input("Enter first number : "))
secondNumber = int(input("Enter second number : "))
thirdNumber = int(input("Enter third number : "))

# calculate the average
ave = (firstNumber + secondNumber + thirdNumber) / 3

print("n1 ={0:5d} \n n2 ={1:5d} \n n3 ={2:5d}".format(firstNumber, secondNumber, thirdNumber))
print("Average = {0:8.2f}".format(ave))
