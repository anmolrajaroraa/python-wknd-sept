# def calc(x=0,y=0,*args,**kwargs):
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     mod = x % y
#     power = 2 ** 3
#     return add, sub, mul, div, mod, power    #packing

# result = calc(9999,200)

# print(f"Result is {result}")

# a,b,c,d,*e = calc(88,22)   #unpacking

# print(a,b,c,d,e)

# def calc2(x=0, y=0, *args, **kwargs):    #function generator
#     print('abcd')
#     return None

# print(calc2())


# def calc(x=0, y=0, *args, **kwargs):    #function generator
#     yield x + y
#     yield x - y
#     yield x * y
#     yield x / y

# result = calc(100,76)   #result will receive a generator object
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())

# for value in calc(23,21):
#     print(value)


# list1 = [i for i in range(10)]
# print(list1)

# generatorObject = (i for i in range(10))
# print(generatorObject.__next__())
# print(generatorObject.__next__())
# print(generatorObject.__next__())
# print(generatorObject.__next__())

# for i in generatorObject:
#     print(i)

def nextSquare(num):
    for i in range(1,num+1):
        yield i ** 2

generatorObject = nextSquare(10)
for square in generatorObject:
    print(square)