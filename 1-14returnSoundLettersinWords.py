st = input("Enter a string")
sound = "aAeEiIoOuU"
count = 0

for char in st:
    if char in sound:
        count += 1
print("the count of sound letters is : ", count)