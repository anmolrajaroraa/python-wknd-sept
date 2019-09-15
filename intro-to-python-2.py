Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> c = a + b
>>> print("Sum of" + a + "and" +  b + "is" + c)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("Sum of" + a + "and" +  b + "is" + c)
TypeError: can only concatenate str (not "int") to str
>>> a = str(a)
>>> print("Sum of" + a + "and" +  str(b) + "is" + str(c))
Sum of10and20is30
>>> print("Sum of " + a + " and " +  str(b) + " is " + str(c))
Sum of 10 and 20 is 30
>>> print("Sum of", a, "and",  b, "is", c)
Sum of 10 and 20 is 30
>>> print("Sum of {} and {} is {}")
Sum of {} and {} is {}
>>> print("Sum of %d and %d is %d")
Sum of %d and %d is %d
>>> print("Sum of %d and %d is %d"%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("Sum of %d and %d is %d"%(a,b,c))
TypeError: %d format: a number is required, not str
>>> a = 10
>>> print("Sum of %d and %d is %d"%(a,b,c))
Sum of 10 and 20 is 30
>>> a = str(10)
>>> print("Sum of %d and %d is %d"%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("Sum of %d and %d is %d"%(a,b,c))
TypeError: %d format: a number is required, not str
>>> print("Sum of %s and %d is %d"%(a,b,c))
Sum of 10 and 20 is 30
>>> print("Sum of {} and {} is {}")
Sum of {} and {} is {}
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 10 and 20 is 30
>>> print("Sum of {a} and {b} is {c}")
Sum of {a} and {b} is {c}
>>> print(f"Sum of {a} and {b} is {c}")
Sum of 10 and 20 is 30
>>> input()

''
>>> input("What's your name: ")
What's your name: Anmol
'Anmol'
>>> name = input("What's your name: ")
What's your name: Anmol
>>> name
'Anmol'
>>> name = input("Enter some integer")
Enter some integer100
>>> name
'100'
>>> 
