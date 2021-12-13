# 1-- Giev a list of inntegers ,return True if the array contains a 3 next to a 3 somewhere

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1,2,3,3]))
print(has_33([1,2,3,1]))


# 2-- given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
  result = ''
  for char in text:
     result += char * 3 
     
  return result
 
print(paper_doll("hello"))


# 3-- return the sum of the numbers in the array , except ignore sections of numbeers starting with a 6 and extending to the next 9 (eveey 6 will be followed by at least one  9 ) return 0 for no numbers

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,3,5]))
print(summer_69([2,1,3,3,4]))



# 4-- write a function that takes in a list of integers and returns True iff it container 007 in order
def spy_game(arr):
    code = [0,0,7,'X']
    for num in arr:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
            
            
            
            
            
# 4-- write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    # check for zero or one input
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break    
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
    
    
    
    
# 5-- write a function that takes in a single letter , and retuen 5 * 5 reprensentation of that letter

def print_big(letter):
    patterns = {
        1: " * ",
        2: " ** ",
        3: " *** ",
        4: " **** ",
        5: " ***** ",
        6: " ****** ",
        7: " ******* ",
        8: " ******** ",
        9: " *     ",
    }
    
    alphabet = {
        'A':[1,2,4,3,3],
        'B':[5,3,5,3,5],
        'C':[4,9,9,9,4],
        'D':[5,3,3,3,5],
        'E':[4,9,4,9,4],
    }
    
    for patetrn in alphabet[letter.upper()]:
        print(patterns[patetrn])
        
print_big('e')