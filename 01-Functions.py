x = 10 #global variables
y = 20
def add():
    x = 100 #local variables
    y = 200
    z = 300
    print(f"Sum of {x} and {y} is {x+y}")
    print(z)
    return z

def subtract(x,y):    #arguments list
    print(f"Diff of {x} and {y} is {x-y}")

def multiply(x=0 , y=0):    #default arguments
    print(f"Product of {x} and {y} is {x*y}")

#dynamic arguments
#   *args ->  multiple arguments -> creates a tuple
#   **kwargs -> keyword arguments -> creates a dictionary

def divide(x =1, y=1, *other):
    print(f"Quotient after division of {x} and {y} is {x/y}")
    print(f"Other is {other}")
    if len(other) >= 2:
        for i in range(len(other) - 1):
            print(f"{other[i]} / {other[i+1]} is {other[i] / other[i+1]}")

def modulus( x=1, y=1, *other, **someOtherValues):
    print(f"Quotient after division of {x} and {y} is {x/y}")
    print(f"Other is {other}")
    print(f"someOtherValues is {someOtherValues}")

# newVar = add()
# print(f"Sum of {x} and {y} is {x+y}")
# print(newVar)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# subtract(num1,num2)     #positional arguments    
# subtract( y=num1, x=num2 )    #mapping the arguments (keyword arguments)

# multiply(num1, num2)

# divide(100,20,300,76,567,76)

# modulus(y=100, x = 999, z=888)
# modulus(500, 300, 3282399, "shjsdk", z = 27, a ="sjkvkv")


def employee(id,name,salary, *otherDetails, **extraDetails):
    print(f"id is  {id}")
    print(f"name is {name}")
    print(f"salary is {salary}")
    print(f"Other details are {otherDetails}")
    print(f"Some other details are {extraDetails}")
    # print(f"Designation is {extraDetails['designation']}")

employee(101, 'Ram', 10000, age=25, leavesLeft=3, designation="Dev")