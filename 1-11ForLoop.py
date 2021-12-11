# counts the numbers in string

text = input("Enter a alphanumeric string : ")
count = 0
for char in text:
    if char >= "0" and char <= "9":
        count += 1
        print(char, end = " ")
        
print("\n Number of digits is :", count)