# 1- write a function that computes the volume of sphere give its radius

def vol(rad):
    return (4 / 3) * (3.14) * (rad ** 3)

print(vol(2))

# 2- write a function that checks wether a number is in a given range(inclusive of high and low)


def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(f'the {num} is in range {low} and {high}')
    else:
        print("Number is not in range !")


# 3-write a python function that accepts a string and calculates the number of upper and lower case letters

def up_low(s):
    # d = {'upper': 0, 'lower': 0} can be dictonary
    lowerCase = 0
    upperCase = 0

    for char in s:
        if char.isupper():
            upperCase += 1
        elif char.islower():
            lowerCase += 1
        else:
            pass
    print(f"original String : {s}")
    print(f"lower case count : {lowerCase}")
    print(f"upper case count : {upperCase}")


# up_low("Hello I Am Vala Here ! How Are you")

# 4- write a function that takes a list  and returns a new list with unuque elements of the first list

def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return  seen_numbers

# print(unique_list([1,1,1,1,1,2,2,2,2,2,3,5,5,5]))


# 4- write a function to multiply all the numbers in a list

def multiply(numbers):
    total = 1

    for num in numbers:
        total = total * num
    return total

# 5- palindrome


def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]


print(palindrome("nurses run"))

























