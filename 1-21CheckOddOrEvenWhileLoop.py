odd = 0
even = 0
while True:
    num = int(input("Enter Numbers : "))
    if num == 0:
        break
    if num % 2 == 0:
        even += num
    else:
        odd += num
        
print(f"sum of Evens : {even} and sum of Odds : {odd}")
    