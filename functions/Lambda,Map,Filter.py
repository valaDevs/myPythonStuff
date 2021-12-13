# =========== MAP =================

def square(num):
    return num ** 2

my_nums = [1,2,3,4,5,6]

for item in map(square,my_nums):
    print(item)



def splicer(myStr):
    if len(myStr) % 2 == 0:
        return 'EVEN'
    else:
        return myStr[0]
    
names = ['vala', 'eve', 'andy']
res = list(map(splicer,names))
print(res)



# =========== FILTER =================

def check_even(num):
    return num % 2 == 0

myNums = [1,2,3,4,5,6,7]

for eve in filter(check_even,myNums):
    print(eve)






# =========== LAMBDA =================

def sq(num): return num ** 2 

# convert the top function to lambda 👇

square2 = lambda num : num ** 2
 
print(square2(5)) 
 
  

# best use of lambda expression is in MAP and Filter or other methods

a = list(map(lambda num : num ** 2, my_nums))
print(a)




b = list(filter(lambda num : num % 2 == 0, my_nums))
print(b)




c = list(map(lambda x : x[0], names))

print(c)







