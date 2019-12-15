import random

def my_decorator(fn):
    def new_func():
        print("Before calling fn..." + fn.__name__)
        print(fn())
        print("After calling fn..." + fn.__name__)
    return new_func

@my_decorator
def myFunc():
    print("My function called..")

@my_decorator    #way to use decorator when fn has been created by me
def add():
    print(f"10 + 15 is {10+15}")

myFunc()
add()

def mySecondFn():
    print("My Second fn called..")

mySecondFn = my_decorator(mySecondFn)
mySecondFn()

# print(random.random())

myRandomFn = my_decorator(random.random)  #way to use decorator when using some built-in fn
myRandomFn()