income = int(input("Enter your income : "))

if income < 2000000:
    tax = 0.0
elif income < 3000000:
    tax = income / 0.02
elif income < 5000000:
    tax = income * 0.03
else:
    tax = income * 0.10
    
print("Income = ", income)
print("tax = ", tax)
print("net income : ", income - tax)