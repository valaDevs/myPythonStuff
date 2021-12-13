x = 25


def printer():
    x = 50
    return x

print(x) #==> 25
print(printer())# ==> 50


# LEBG rule

# Local
# lambda num : num ** 2


# Enclosing
name = "vala"
def greet():
    name = 'sammy'

    def sayHi():
        print('Hello',name)
    sayHi()
greet()


# built in keywords

# len
# open
# for ............


x = 50


def func(x):
    print(f'X is {x}')
    x = 200
    print(f'I just changed Locally x to {x}')

func(x)

print(x)

































