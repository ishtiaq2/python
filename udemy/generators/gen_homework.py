import random

# homework 1
# generate squares of numbers up to some number N

print('**************************** Home work 1 *************************')

def gen_square(n):
    for x in range(n):
        yield x**2


for x in gen_square(10):
    print (x)


print('**************************** Home work 2 *************************')

def gen_random(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

low = 20
high = 40
n = high - low
for x in gen_random(low, high, n):
    print (x)



print('**************************** Home work 3 *************************')

s = 'hello'

s_iter = iter(s)
for x in range(len(s)):
    print next(s_iter)


print('********************* generator comprehension ***********************')

my_list = [1, 2, 3, 4, 5, 6]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print (item)