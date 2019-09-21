Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1 = 't20 world cup will be played soon'
>>> str1.capitalize()
'T20 world cup will be played soon'
>>> str1 = 'T20 world cup wiLL be plaYed Soon'
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str1.lower()
't20 world cup will be played soon'
>>> str1.casefold()
't20 world cup will be played soon'
>>> print(str1)
T20 world cup wiLL be plaYed Soon
>>> len(str1)
33
>>> str1.center(100)
'                                 T20 world cup wiLL be plaYed Soon                                  '
>>> str2 = str1.center(100)
>>> str2
'                                 T20 world cup wiLL be plaYed Soon                                  '
>>> len(str2)
100
>>> str2 = str1.center(70)
>>> str2
'                  T20 world cup wiLL be plaYed Soon                   '
>>> str2 = str1.center(30)
>>> 
>>> str2
'T20 world cup wiLL be plaYed Soon'
>>> str2 = str1.center(300)
>>> str2
'                                                                                                                                     T20 world cup wiLL be plaYed Soon                                                                                                                                      '
>>> str1.count(20)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str1.count(20)
TypeError: must be str, not int
>>> str1.count('20')
1
>>> str1.index('20')
1
>>> str1.count('w')
2
>>> str1.index('w')
4
>>> str1.find('w')
4
>>> str1.rfind('w')
14
>>> str1.count('o')
3
>>> str1.find('o')
5
>>> str1.rfind('o')
31
>>> str1.find('o')
5
>>> str1.find('o',6)
30
>>> str1.find('o',31)
31
>>> str1.find('python')
-1
>>> str1.index('python')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    str1.index('python')
ValueError: substring not found
>>> #python is utf-8 based
>>> #ascii consists of 128 characters only including english alphabets and numbers
>>> 
>>> #bytes
>>> 
>>> newStr = 'āßš'
>>> print(newStr)
āßš
>>> newStr[0]
'ā'
>>> newStr.encode()
b'\xc4\x81\xc3\x9f\xc5\xa1'
>>> newStr = 'āabcd1234ß@#$%š'
>>> newStr.encode()
b'\xc4\x81abcd1234\xc3\x9f@#$%\xc5\xa1'
>>> encodedString = newStr.encode()
>>> type(encodedString)
<class 'bytes'>
>>> encodedString
b'\xc4\x81abcd1234\xc3\x9f@#$%\xc5\xa1'
>>> encodedString.decode()
'āabcd1234ß@#$%š'
>>> #internationalization (I18N)
>>> 
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str1.startswith('t')
False
>>> str1.startswith('T')
True
>>> str1.startswith('T20')
True
>>> str1.startswith('T20 world cup')
True
>>> str1.endswith('n')
True
>>> str1.endswith('soon')
False
>>> str1.endswith('Soon')
True
>>> str5 = 't20\tworld\tcup'
>>> print(str5)
t20	world	cup
>>> print(str5.expandtabs(10))
t20       world     cup
>>> print(str5.expandtabs(20))
t20                 world               cup
>>> str5 = 't20\tworld\t\tcup'
>>> print(str5)
t20	world		cup
>>> print("Sum of {} and {} is {}")
Sum of {} and {} is {}
>>> #print("Sum of {} and {} is {}".format(a,b,c))
>>> 'a match is going on currently'.find('match')
2
>>> #print("Sum of {a} and {b} is {c}".format_map(dict1))
>>> dict1 = {}
>>> dict1 = {
	'a':10,
	'b':20,
	'c':30
	}
>>> print("Sum of {} and {} is {}".format(dict1))
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print("Sum of {} and {} is {}".format(dict1))
IndexError: tuple index out of range
>>> print("Sum of {} and {} is {}".format(dict1, dict1, dict1))
Sum of {'a': 10, 'b': 20, 'c': 30} and {'a': 10, 'b': 20, 'c': 30} is {'a': 10, 'b': 20, 'c': 30}
>>> print("Sum of {a} and {b} is {c}".format_map(dict1))
Sum of 10 and 20 is 30
>>> 'abcd1224'.isalnum()
True
>>> 'abcd1224$'.isalnum()
False
>>> 'abcd1224$'.isalpha()
False
>>> 'abcd'.isalpha()
True
>>> 'a match is going on currently'.isalpha()
False
>>> 'a match is going on currently'.replace(' ', '')
'amatchisgoingoncurrently'
>>> newStr = 'a match is going on currently'.replace(' ', '')
>>> newStr.isalpha()
True
>>> 'a match is going on currently'.replace(' ', '').isalpha()
True
>>> #function chaining
>>> '@#$abcd1234'.isascii()
True
>>> '@#$abcd1234āßš'.isascii()
False
>>> 'ß'.isascii()
False
>>> #isdecimal works for normal numbers
>>> #isdigit works for superscript and subscript as well
>>> #isnumeric works for fractions also
>>> 't20'.identifier()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    't20'.identifier()
AttributeError: 'str' object has no attribute 'identifier'
>>> 't20'.isidentifier()
True
>>> '$t20'.isidentifier()
False
>>> t20 = 120
>>> $t20 = 120
SyntaxError: invalid syntax
>>> #variable is also known as identifier
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str1.islower()
False
>>> str1.lower().islower()
True
>>> str1.isupper()
False
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str1.swapcase()
't20 WORLD CUP WIll BE PLAyED sOON'
>>> 'a'.isprintable()
True
>>> '\t'.isprintable()
False
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str1.title()
'T20 World Cup Will Be Played Soon'
>>> str1.istitle()
False
>>> str1.title().istitle()
True
>>> string1 = 't20 world cup'
>>> string2 = 'will be played'
>>> string3 = 'soon'
>>> ' '.join(string1,string2,string3)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    ' '.join(string1,string2,string3)
TypeError: join() takes exactly one argument (3 given)
>>> ' '.join([string1,string2,string3])
't20 world cup will be played soon'
>>> '$'.join([string1,string2,string3])
't20 world cup$will be played$soon'
>>> ' $$ '.join([string1,string2,string3])
't20 world cup $$ will be played $$ soon'
>>> string1.join([string2, string3])
'will be playedt20 world cupsoon'
>>> string1.join([string2, string3, string2, string3])
'will be playedt20 world cupsoont20 world cupwill be playedt20 world cupsoon'
>>> str1.center(100)
'                                 T20 world cup wiLL be plaYed Soon                                  '
>>> str1.ljust(100)  #left-justified
'T20 world cup wiLL be plaYed Soon                                                                   '
>>> str1.ljust(100, '#')  #left-justified
'T20 world cup wiLL be plaYed Soon###################################################################'
>>> str1.center(100, '#')
'#################################T20 world cup wiLL be plaYed Soon##################################'
>>> newStr = str1.center(100, '#')
>>> newStr
'#################################T20 world cup wiLL be plaYed Soon##################################'
>>> newStr.find('T')
33
>>> newStr[32] = ' '
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    newStr[32] = ' '
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> str1.replace(' ', '')
'T20worldcupwiLLbeplaYedSoon'
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str2 = str1.replace(' ', '')
>>> id(str1)
4612638920
>>> id(str2)
4578159952
>>> id(str1) == id(str2)
False
>>> str1
'T20 world cup wiLL be plaYed Soon'
>>> str1[0] = ' '
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    str1[0] = ' '
TypeError: 'str' object does not support item assignment
>>> str1 = 'anmol'
>>> id(str1)
4578117872
>>> str1 = ' t20 world cup will be played soon '
>>> newStr = str1.center(100, '#')
>>> newStr
'################################ t20 world cup will be played soon #################################'
>>> str1
' t20 world cup will be played soon '
>>> str1 = 't20 world cup will be played soon'
>>> len(33)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    len(33)
TypeError: object of type 'int' has no len()
>>> len(str1)
33
>>> str1.center(35)
' t20 world cup will be played soon '
>>> newStr = str1.center(35)
>>> newStr.center(100, '#')
'################################ t20 world cup will be played soon #################################'
>>> str1 = '      t20 world cup will be played soon       '
>>> str1.strip()
't20 world cup will be played soon'
>>> #strip removes leading(in beginning) and trailing (at the end) spaces
>>> str1.lstrip()
't20 world cup will be played soon       '
>>> str1.rstrip()
'      t20 world cup will be played soon'
>>> str1.rjust(100)
'                                                            t20 world cup will be played soon       '
>>> str1
'      t20 world cup will be played soon       '
>>> str1.replace('t20', 'odi')
'      odi world cup will be played soon       '
>>> str1
'      t20 world cup will be played soon       '
>>> str1.replace('2', '5')
'      t50 world cup will be played soon       '
>>> str1.replace('t', 'f')
'      f20 world cup will be played soon       '
>>> 
