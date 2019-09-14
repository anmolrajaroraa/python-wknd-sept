Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my name is anmol
SyntaxError: invalid syntax
>>> #my name is anmol
>>> #include<stdio.h>
>>> #include<conio.h>
>>> #void main()
>>> #clrscr()
>>> #getch()
>>> #class
>>> #public static void main(String[] args)
>>> 2 + 3
5
>>> print('hello')
hello
>>> print('hello');
hello
>>> print("hello");
hello
>>> print('hello');
hello
>>> 2 + 6
8
>>> print('hello python');
hello python
>>> print('hello "python"');
hello "python"
>>> print("hello "python"");
SyntaxError: invalid syntax
>>> print('hello "python"');
hello "python"
>>> print("hello 'python'");
hello 'python'
>>> print("let's learn python");
let's learn python
>>> print('let\'s learn "python"');
let's learn "python"
>>> print("let\'s learn \"python\"");
let's learn "python"
>>> # \n, \t, \r - whitecase or non-printable or escape characters
>>> print
<built-in function print>
>>> print() #function call

>>> print "hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
>>> 2 + 3
5
>>> 2 - 3
-1
>>> 2 * 3
6
>>> 2 ** 3
8
>>> 2 ** 4
16
>>> 3 ** 3
27
>>> 5 ** 5
3125
>>> 2 / 3
0.6666666666666666
>>> 737839/364
2027.0302197802198
>>> 737839 // 364
2027
>>> 737839 / 364 #classic division
2027.0302197802198
>>> 737839 // 364  #floor division
2027
>>> 
>>> #number
>>> #integers - 10,20,654,9756
>>> #float - 10.0, 10.1, 10.9389394
>>> #double - 10.12345675431245
>>> a = 10
>>> 10
10
>>> 20
20
>>> var = 20
>>> print(var)
20
>>> type(var)
<class 'int'>
>>> type(10.0)
<class 'float'>
>>> type(10.00000000000)
<class 'float'>
>>> var = int(20)
>>> type(20)
<class 'int'>
>>> #everything is an object
>>> 10
10
>>> 'anmol'
'anmol'
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> false
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> #number, string, boolean (True or False)
>>> None
>>> true = None
>>> true
>>> print(true)
None
>>> a = 10
>>> a = int('hsjdl
	
SyntaxError: EOL while scanning string literal
>>> a = int('10')
>>> a
10
>>> a = int('100')
>>> a
100
>>> a = int('100a')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a = int('100a')
ValueError: invalid literal for int() with base 10: '100a'
>>> a = str(10)
>>> a
'10'
>>> type(a)
<class 'str'>
>>> a = str('10')
>>> a
'10'
>>> a = '10'
>>> a
'10'
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = str('abc')
>>> a
'abc'
>>> a = str(True)
>>> a
'True'
>>> type(a)
<class 'str'>
>>> a = str(True)
>>> a
'True'
>>> a = int(True)
>>> a
1
>>> a = int(False)
>>> a
0
>>> a = bool('True')
>>> a
True
>>> type(a)
<class 'bool'>
>>> a = bool('not present')
>>> a
True
>>> #int is without quotes - 10, 20
>>> #int can be converted to string
>>> a = bool(10)
>>> a
True
>>> a = bool(0)
>>> 
>>> a
False
>>> #int is without quotes - 10, 20
>>> #int can be converted to string and boolean as well
>>> #string is with single or double quotes
>>> #string can be converted to int iff(if and only if) your string contains only digits
>>> a = bool(None)
>>> a
False
>>> #string will always be converted to True
>>> a = bool('')
>>> a
False
>>> #string will always be converted to True if there is atleast a character present, if no characters are present,
>>> #it will convert to False
>>> #boolean contains only two values - True or False
>>> #True gets converted to 1 and False gets converted to 0
>>> #True gets converted to 'True' and False gets converted to 'False'
>>> #If we write bool(None), we will get False. None means empty object
>>> a = None
>>> type(a)
<class 'NoneType'>
>>> a = 10
>>> id(a)
4474551760
>>> b = 20
>>> id(20)
4474552080
>>> id(b)
4474552080
>>> #binary - 0 or 1
>>> #octal - 0 to 7
>>> #decimal - 0 to 9
>>> #hexadecimal - 0 - 15
>>> #0 to 9, 10 -> a, 11->b, c, d , e, 15 -> f
>>> hex(id(a))
'0x10ab43dd0'
>>> hex(id(b))
'0x10ab43f10'
>>> #hex is used for converting decimal numbers (0 to 9) into hexadecimal numbers (0 to 9, a to f)
>>> #id is used to get memory location of our object
>>> True = 'present'
SyntaxError: can't assign to keyword
>>> str()
''
>>> str = 'present
SyntaxError: EOL while scanning string literal
>>> str = 'present'
>>> str()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    str()
TypeError: 'str' object is not callable
>>> str
'present'
>>> #str int bool print input id hex sum
>>> a = 10
>>> b = 20
>>> a + b
30
>>> a + b
30
>>> c = a + b
>>> c
30
>>> print(c)
30
>>> print("Sum of 10 and 20 is 30")
Sum of 10 and 20 is 30
>>> print("Sum of 10 and 20 is " + c)  #string concatenation (joining) -> + ,
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    print("Sum of 10 and 20 is " + c)  #string concatenation (joining) -> + ,
TypeError: can only concatenate str (not "int") to str
>>> #converting from one type to another type is 'type casting'
>>> print("Sum of 10 and 20 is " + str(c))
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    print("Sum of 10 and 20 is " + str(c))
TypeError: 'str' object is not callable
>>> 
