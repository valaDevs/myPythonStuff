done = True
odds = 0

while done:
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("The number is Even enter a ODD number : ")
        continue
    odds += num
    answer = input("Do you want to continue ? (Y/N)")
    if answer.lower() == "y":
        continue
    done = False
print("Sum of ODD numbers is : ", odds)
