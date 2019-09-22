Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1 = 't20 world cup will be played soon'
>>> #t -> f, 2 -> 5, l -> 1, o should be deleted
>>> str1.maketrans('t2l', 'f51', 'o')
{116: 102, 50: 53, 108: 49, 111: None}
>>> table = str1.maketrans('t2l', 'f51', 'o')
>>> str1.translate(table)
'f50 wr1d cup wi11 be p1ayed sn'
>>> str1.replace('world cup', 'champions league')
't20 champions league will be played soon'
>>> str1.split()
['t20', 'world', 'cup', 'will', 'be', 'played', 'soon']
>>> str1.split('l')
['t20 wor', 'd cup wi', '', ' be p', 'ayed soon']
>>> str1.split('cup')
['t20 world ', ' will be played soon']
>>> str1.split(maxsplit=3)
['t20', 'world', 'cup', 'will be played soon']
>>> str1.split('l', 2)
['t20 wor', 'd cup wi', 'l be played soon']
>>> str1.split(3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    str1.split(3)
TypeError: must be str or None, not int
>>> str1.split(maxsplit=3)
['t20', 'world', 'cup', 'will be played soon']
>>> str1.partition()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str1.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> str1.partition(' ')
('t20', ' ', 'world cup will be played soon')
>>> str1.partition('l')
('t20 wor', 'l', 'd cup will be played soon')
>>> str1.rpartition('l')
('t20 world cup will be p', 'l', 'ayed soon')
>>> 
>>> #split by default works on a single space
>>> #split has maxsplit = -1 and we can change it
>>> #partition has maxsplit = 1 and we cannot change it
>>> 
>>> str1.split('l',2)
['t20 wor', 'd cup wi', 'l be played soon']
>>> str1.rsplit('l')
['t20 wor', 'd cup wi', '', ' be p', 'ayed soon']
>>> str1.split('l')
['t20 wor', 'd cup wi', '', ' be p', 'ayed soon']
>>> str1.split('l',3)
['t20 wor', 'd cup wi', '', ' be played soon']
>>> str1.rsplit('l',3)
['t20 world cup wi', '', ' be p', 'ayed soon']
>>> str1 = 't20 world cup will be played soon\nit will be 20th edition of world cup'
>>> print(str1)
t20 world cup will be played soon
it will be 20th edition of world cup
>>> str1 = 't20 world cup will be played soon\n it will be 20th edition of world cup'
>>> print(str1)
t20 world cup will be played soon
 it will be 20th edition of world cup
>>> str1
't20 world cup will be played soon\n it will be 20th edition of world cup'
>>> str1.splitlines()
['t20 world cup will be played soon', ' it will be 20th edition of world cup']
>>> str1.split('\n')
['t20 world cup will be played soon', ' it will be 20th edition of world cup']
>>> str1.capitalize()
'T20 world cup will be played soon\n it will be 20th edition of world cup'
>>> str1.title()
'T20 World Cup Will Be Played Soon\n It Will Be 20Th Edition Of World Cup'
>>> #0001, 0010, 0100, 1000
>>> '10'.zfill(4)
'0010'
>>> '3'.zfill(4)
'0003'
>>> '999'.zfill(4)
'0999'
>>> '9997'.zfill(4)
'9997'
>>> '999734'.zfill(4)
'999734'
>>> 
