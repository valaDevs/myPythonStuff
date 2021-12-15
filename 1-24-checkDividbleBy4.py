sum = 0
N = 10
for i in range(N):
    num = int(input("Enter numbers  : "))
    
    if num % 4 == 0:
        sum += num
print("Dividble count : ",sum)
    