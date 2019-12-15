#5! -> Factorial of 5

# 5 * 4 * 3 * 2 * 1
# 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

def check_factorial_argument(fn):
    def new_func(num):
        if type(num) == int and num > 0:
            print("Before calling ", fn.__name__)
            fn(num)
            print("After calling ", fn.__name__)
        else:
            print("Invalid argument")
    return new_func

@check_factorial_argument
def factorial(num):
    if num == 1:
        print(1)
    else:
        result = 1
        for i in range(num,0,-1):
            result = result * i
        print(result)

factorial(5)