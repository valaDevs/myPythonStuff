import  math

a = int(input("Enter value a : "))
b = int(input("Enter value b : "))
c = int(input("Enter value c : "))

result = math.sqrt(math.fabs(a - b) ** math.fabs(c))
print("result is" , result)


# ===============================
n = int(input("Enter value n : "))
p = int(input("Entre Power : "))
res = math.exp(n * math.log(a))