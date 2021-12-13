# 1-- wirte a functio that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both are odd

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        # if a < b:
        #     result = a
        # else:
        #     result = b
        result = min(a,b)
    else:
        # if a > b:
        #     result = a
        # else:
            result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))

# 2-- write a function takes a two word string and returns true if both words begin with same letter

def chck_words(text):
    wordl_list = text.lower().split()
    
    # first_word = wordl_list[0]
    # second_word = wordl_list[1]

    
    return wordl_list[0][0] == wordl_list[1][0]

print(chck_words("vala faba"))
print(chck_words("vala vaba"))
print(chck_words("Crazy cat"))

# 3-- Given two integers, return True if sum of the integer is 20 or if one of the integers is 20. if not , return False

def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        return True
    else:
        return False

print()
print(makes_twenty(10,10))
print(makes_twenty(11,9))
print(makes_twenty(10,80))