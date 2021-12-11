n = None
if n < 100:
    exp = 50
else:
    exp = 500

# convert to ternary 

exp = 50 if n < 100 else 500


# code exaple
num = int(input("Enter a number : "))
count = 100 if num < 0 else 200
print("number = ",num,"counter = ",count)