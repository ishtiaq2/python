print('************* yield ********************')
print ('suspends function execution and return the yield position value back to the caller')
print ('retaining enough info to resume from where it was suspended')

def yield_func():
    yield 1
    yield 2
    yield 3

y = yield_func()
print 'yield_func: ', next(y)
print 'yield_func: ', next(y)
print 'yield_func: ', next(y)

print ('********************* loop through yield_func ******************')
for x in yield_func():
    print 'loop through yield_func: ', x

def create_cubes(n):    
    for x in range(n):
        yield x**3


for x in create_cubes(10):
    print (x)



print('******************* Fibonoci *******************')


def gen_fibonoci(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a, b = b, a+b

for x in gen_fibonoci(10):
    print x


print('******************* What is happening behind the scene **************')
print('******************* next, iter **************************************')

def simple_gen():
    for x in range(3):
        yield x


for n in simple_gen():
    print (n)

gen = simple_gen()
print (next(gen))
print (next(gen))
print (next(gen))

s= 'hello'
for l in s:
    print (l)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

