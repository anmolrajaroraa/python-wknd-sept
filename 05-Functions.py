from functools import reduce
from itertools import accumulate
import operator

numbers = [2,34,56,78,9,78,6,54,31]

list1 = [1,2,3,4,5]
# 1+2 = 3  ->  [3,3,4,5]
# 3+3 = 6 -> [6,4,5]
# 6+4 = 10 -> [10,5]
# 10+5 = 15

#  [1,3,6,10,15]


# print(reduce( lambda x,y : x + y, numbers))

def add(x,y):
    print(f"{x} + {y}")
    return x + y

# print(reduce(add, numbers))

# print(list(accumulate(numbers, add)))

print(reduce(operator.truediv, numbers))