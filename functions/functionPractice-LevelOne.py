# 1-- write a function that capitalize the first and fourth letters of a name 

def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    forth_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween + forth_letter.upper() + rest


# 2-- Given a sentence , return a sentece with the words reversed
def master_yoda(text):
    wordlist = text.split()
    rev = wordlist[::-1]
    return ' '.join(rev)

print(master_yoda("Hello world"))



# 3-- Given aan integer n  return True if n is withon 10 of either 100 or 200 

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)