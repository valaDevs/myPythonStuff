op = input("Enter the operator (+ , - , * , ** , / ,  //  ) : ")
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : " ))

if op == "+":
    result = num1 + num2
    print("Sum num1 and num2 is :", result)
elif op == "-":
    result = num1 - num2
    print("Substraction num1 and num2 is : ",result)
elif op == "*":
    result = num1 * num2
    print("Multiplication of num1 and num2 is : ", result)
elif op == "**":
    result = num1 ** num2
    print("Power of num1 and num2 is : ", result)
elif op == "/":
    result = num1 / num2
    print("Division of num1 and num2 is : ", result)
elif op == "//":
    result = num1 // num2
    print("Float Division of num1 and num2 is : ", result)
else:
    print("The Operator is not supported")
    