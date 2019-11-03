Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple1 = (1,2,3,4,5)
>>> tuple1[0]
1
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> tuple1[0] = 100
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> tuple1 = (11,22,[33,44,55])
>>> tuple1[-1]
[33, 44, 55]
>>> tuple1[-1][-1] = 555
>>> tuple1 = (11,22,[33,44,55])
>>> tuple1[-1][-1] = 555
>>> tuple1
(11, 22, [33, 44, 555])
>>> 
>>> list1 = [1,2,3,4,5]
>>> list2 = list1
>>> list1.append(6)
>>> list1
[1, 2, 3, 4, 5, 6]
>>> list2
[1, 2, 3, 4, 5, 6]
>>> list2 - list1.copy()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list2 - list1.copy()
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> list2 = list1.copy()
>>> list1 == list2
True
>>> list1
[1, 2, 3, 4, 5, 6]
>>> list2
[1, 2, 3, 4, 5, 6]
>>> list1 is list2
False
>>> list1.append(7)
>>> list1
[1, 2, 3, 4, 5, 6, 7]
>>> list2
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> list1 = [11,22,[33,44,55]]
>>> list2 = list1.copy()
>>> list1 is list2
False
\
>>> list1[-1]
[33, 44, 55]
>>> list1[-1].append(66)
>>> list1
[11, 22, [33, 44, 55, 66]]
>>> list2
[11, 22, [33, 44, 55, 66]]
>>> hex(id(list1))
'0x10f08cf08'
>>> hex(id(list2))
'0x10c68c288'
>>> hex(id(list1[-1]))
'0x10c68bf48'
>>> hex(id(list2[-1]))
'0x10c68bf48'
>>> import copy
>>> list2 = copy.deepcopy(list1)
>>> list1[-1]
[33, 44, 55, 66]
>>> list1[-1].remove(66)
>>> list1
[11, 22, [33, 44, 55]]
>>> list2
[11, 22, [33, 44, 55, 66]]
>>> 
>>> 
>>> set1 = {1,2,3,4,5,6,'True','hello', 'bye', 'python', 'Mannan'}
>>> set1
{1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'hello', 'True', 'bye'}
>>> set1 = {1,2,3,4,5,6,True,'hello', 'bye', 'python', 'Mannan'}
>>> set1
{1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'hello', 'bye'}
>>> set1 = {1,2,3,4,5,6,True,'hello', 'bye', 'python', 'Mannan', False}
>>> set1
{False, 1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'hello', 'bye'}
>>> 
>>> int(True)
1
>>> int(False)
0
>>> 
>>> 
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> for element in set1:
	print(element)

	
False
1
2
3
4
5
6
Mannan
python
hello
bye
>>> 
>>> set1.add('java')
>>> set1
{False, 1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'hello', 'java', 'bye'}
>>> 
>>> #Difference -> Set1-Set2 -> All those elements which exist in Set1 but are not present in Set2
>>> 
>>> set1
{False, 1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'hello', 'java', 'bye'}
>>> set2 = {1, 2, 3, 4, 5, 6, 'Mannan', 'python'}
>>> set1.difference(set2)
{False, 'bye', 'hello', 'java'}
>>> set2 = {1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript'}
>>> 
>>> set1 - set2
{False, 'bye', 'hello', 'java'}
>>> 
>>> set1.symmetric_difference(set2)
{False, 'javascript', 'hello', 'java', 'bye'}
>>> 
>>> (set1 - set2).union((set2 - set1))
{False, 'hello', 'java', 'bye', 'javascript'}
>>> 
>>> 
>>> set1.union(set2)
{False, 1, 2, 3, 4, 5, 6, 'java', 'Mannan', 'python', 'javascript', 'hello', 'bye'}
>>> {False, 1, 2, 3, 4, 5, 6, 'java', 'Mannan', 'python', 'javascript', 'hello', 'bye'}
{False, 1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript', 'hello', 'java', 'bye'}
>>> {False, 1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript', 'hello', 'java', 'bye'}
{False, 1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript', 'hello', 'java', 'bye'}
>>> 
>>> 
>>> set1.intersection(set2)
{1, 2, 3, 4, 5, 6, 'Mannan', 'python'}
>>> 
>>> 
>>> set1.intersection_update(set2)
>>> set1
{1, 2, 3, 4, 5, 6, 'Mannan', 'python'}
>>> 
>>> 
>>> set1
{1, 2, 3, 4, 5, 6, 'Mannan', 'python'}
'
>>> set2
{1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript'}
>>> set1.update(set2)
>>> set1
{1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript'}
>>> 
>>> 
>>> set1.pop()
1
>>> set1.pop()
2
>>> set1.pop()
3
>>> set1.pop()
4
>>> set1.remove('javascript')
>>> set1.discard('javascript')
>>> set1.remove('javascript')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    set1.remove('javascript')
KeyError: 'javascript'
>>> set1.discard('javascript')
>>> set3 = {100,200,300}
>>> set1
{5, 6, 'Mannan', 'python'}
>>> set2
{1, 2, 3, 4, 5, 6, 'Mannan', 'python', 'javascript'}
>>> set3
{200, 100, 300}
>>> set1.isdisjoint(set2)
False
>>> set1.intersection(set2)
{'python', 'Mannan', 5, 6}
>>> set1.intersection(set3)
set()
>>> set1.isdisjoint(set3)
True
>>> 
>>> set1.issubset(set2)
True
>>> set2.issuperset(set1)
True
>>> 
>>> set5 = frozenset(set1)
>>> set5
frozenset({'python', 'Mannan', 5, 6})
>>> dir(frozenset)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> 
>>> set5.add(10)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    set5.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> 
>>> def1 = 'Data science is a "concept to unify statistics, data analysis, machine learning and their related methods" in order to "understand and analyze actual phenomena" with data. It employs techniques and theories drawn from many fields within the context of mathematics, statistics, computer science, and information science.'
>>> def2 = 'As the world entered the era of big data, the need for its storage also grew. It was the main challenge and concern for the enterprise industries until 2010. The main focus was on building framework and solutions to store data. Now when Hadoop and other frameworks have successfully solved the problem of storage, the focus has shifted to the processing of this data. Data Science is the secret sauce here. All the ideas which you see in Hollywood sci-fi movies can actually turn into reality by Data Science. Data Science is the future of Artificial Intelligence. Therefore, it is very important to understand what is Data Science and how can it add value to your business.'
>>> #tokenization
>>> tokens_1 = def1.split()
>>> tokens_1
['Data', 'science', 'is', 'a', '"concept', 'to', 'unify', 'statistics,', 'data', 'analysis,', 'machine', 'learning', 'and', 'their', 'related', 'methods"', 'in', 'order', 'to', '"understand', 'and', 'analyze', 'actual', 'phenomena"', 'with', 'data.', 'It', 'employs', 'techniques', 'and', 'theories', 'drawn', 'from', 'many', 'fields', 'within', 'the', 'context', 'of', 'mathematics,', 'statistics,', 'computer', 'science,', 'and', 'information', 'science.']
>>> def1.replace('"', '')
'Data science is a concept to unify statistics, data analysis, machine learning and their related methods in order to understand and analyze actual phenomena with data. It employs techniques and theories drawn from many fields within the context of mathematics, statistics, computer science, and information science.'
>>> def1 = def1.replace('"', '')
>>> def1 = def1.replace(',', '')
>>> def1 = def1.replace('.', '')
>>> def1
'Data science is a concept to unify statistics data analysis machine learning and their related methods in order to understand and analyze actual phenomena with data It employs techniques and theories drawn from many fields within the context of mathematics statistics computer science and information science'
>>> def2 = def2.replace(',', '')
>>> def2 = def2.replace('.', '')
>>> def2
'As the world entered the era of big data the need for its storage also grew It was the main challenge and concern for the enterprise industries until 2010 The main focus was on building framework and solutions to store data Now when Hadoop and other frameworks have successfully solved the problem of storage the focus has shifted to the processing of this data Data Science is the secret sauce here All the ideas which you see in Hollywood sci-fi movies can actually turn into reality by Data Science Data Science is the future of Artificial Intelligence Therefore it is very important to understand what is Data Science and how can it add value to your business'
>>> tokens1 = def1.split()
>>> tokena1
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    tokena1
NameError: name 'tokena1' is not defined
>>> tokens1
['Data', 'science', 'is', 'a', 'concept', 'to', 'unify', 'statistics', 'data', 'analysis', 'machine', 'learning', 'and', 'their', 'related', 'methods', 'in', 'order', 'to', 'understand', 'and', 'analyze', 'actual', 'phenomena', 'with', 'data', 'It', 'employs', 'techniques', 'and', 'theories', 'drawn', 'from', 'many', 'fields', 'within', 'the', 'context', 'of', 'mathematics', 'statistics', 'computer', 'science', 'and', 'information', 'science']
>>> tokens2 = def2.split()
>>> tokens2
['As', 'the', 'world', 'entered', 'the', 'era', 'of', 'big', 'data', 'the', 'need', 'for', 'its', 'storage', 'also', 'grew', 'It', 'was', 'the', 'main', 'challenge', 'and', 'concern', 'for', 'the', 'enterprise', 'industries', 'until', '2010', 'The', 'main', 'focus', 'was', 'on', 'building', 'framework', 'and', 'solutions', 'to', 'store', 'data', 'Now', 'when', 'Hadoop', 'and', 'other', 'frameworks', 'have', 'successfully', 'solved', 'the', 'problem', 'of', 'storage', 'the', 'focus', 'has', 'shifted', 'to', 'the', 'processing', 'of', 'this', 'data', 'Data', 'Science', 'is', 'the', 'secret', 'sauce', 'here', 'All', 'the', 'ideas', 'which', 'you', 'see', 'in', 'Hollywood', 'sci-fi', 'movies', 'can', 'actually', 'turn', 'into', 'reality', 'by', 'Data', 'Science', 'Data', 'Science', 'is', 'the', 'future', 'of', 'Artificial', 'Intelligence', 'Therefore', 'it', 'is', 'very', 'important', 'to', 'understand', 'what', 'is', 'Data', 'Science', 'and', 'how', 'can', 'it', 'add', 'value', 'to', 'your', 'business']
>>> 
>>> stopwords = {'is', 'a', 'to', 'and', 'their', 'the', 'in', 'with', 'it', 'from', 'of', 'as', 'for', 'its', 'also', 'was', 'on', 'have', 'has', 'this', 'can', 'into', 'by'}
>>> 
>>> words1 = []
>>> words2 = []
>>> words1 = {}
>>> words2 = {}
>>> for token in tokens1:
	words1.add(token.lower())

	
Traceback (most recent call last):
  File "<pyshell#155>", line 2, in <module>
    words1.add(token.lower())
AttributeError: 'dict' object has no attribute 'add'
>>> words1 = set()
>>> words2 = set()
>>> for token in tokens1:
	words1.add(token.lower())

	
>>> words1
{'techniques', 'analysis', 'and', 'of', 'machine', 'statistics', 'unify', 'phenomena', 'the', 'context', 'it', 'understand', 'fields', 'with', 'science', 'from', 'employs', 'a', 'drawn', 'analyze', 'mathematics', 'computer', 'information', 'data', 'is', 'learning', 'within', 'their', 'theories', 'methods', 'order', 'concept', 'to', 'many', 'related', 'actual', 'in'}
>>> words1.difference_update(stopwords)
>>> words1
{'techniques', 'analysis', 'machine', 'statistics', 'unify', 'phenomena', 'context', 'understand', 'fields', 'science', 'employs', 'drawn', 'analyze', 'mathematics', 'computer', 'information', 'data', 'learning', 'within', 'theories', 'methods', 'order', 'concept', 'many', 'related', 'actual'}
>>> for token in tokens2:
	words2.add(token.lower())

	
>>> words2.difference_update(stopwords)
>>> words2
{'how', 'hadoop', 'focus', 'secret', 'important', 'era', 'you', 'sci-fi', 'storage', 'industries', 'store', 'intelligence', 'data', 'your', 'therefore', 'big', 'business', 'other', 'hollywood', '2010', 'movies', 'until', 'sauce', 'solutions', 'actually', 'processing', 'successfully', 'shifted', 'now', 'future', 'value', 'enterprise', 'add', 'understand', 'problem', 'all', 'frameworks', 'see', 'challenge', 'which', 'very', 'world', 'ideas', 'need', 'grew', 'when', 'building', 'reality', 'concern', 'turn', 'science', 'here', 'solved', 'artificial', 'main', 'framework', 'entered', 'what'}
>>> 
>>> #Jaccards distance formula  ->   intersection / union *100
>>> 
>>> i = words1.intersection(words2)
>>> u = words1.union(words2)
>>> d = len(i) / len(u) * 100
>>> d
3.7037037037037033
>>> len(i)
3
>>> len(u)
81
>>> 
 RESTART: /Users/anmolrajarora/Documents/python-reg-sept/movie_recommendation2.py 
Most watched category is action
{'Manikarna The Queen', 'Sahoo'}
>>> 
