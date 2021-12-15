num = int(input("Enter a number : "))
hlp = num 
sum = 0
while hlp != 0:
    sum += hlp % 10
    hlp = hlp // 10
    
print("Numbers : ", num,"Sum of Digits is : ",sum )