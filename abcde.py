Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> x
[]
>>> x + []
[]
>>> x
[]
>>> x + ()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x + ()
TypeError: can only concatenate list (not "tuple") to list
>>> x + ['']
['']
>>> x
[]
>>> x + [,]
SyntaxError: invalid syntax
>>> x + ['',]
['']
>>> x
[]
>>> x + ['','']
['', '']
>>> x
[]
>>> x + x
[]
>>> x+x+x
[]
>>> x = ['',]
>>> x
['']
>>> x+x
['', '']
>>> x+x+x
['', '', '']
>>> x = [y]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x = [y]
NameError: name 'y' is not defined
>>> y = []
>>> x
['']
>>> x=[]
>>> x+y
[]
>>> z=[]
>>> x
[]
>>> y
[]
>>> y = [z]
>>> x
[]
>>> y
[[]]
>>> z
[]
>>> x+y
[[]]
>>> y+z
[[]]
>>> a=[]
>>> b=[a]
>>> c=[b]
>>> a
[]
>>> b
[[]]
>>> c
[[[]]]
>>> c+b
[[[]], []]
>>> d=[c]
>>> e=[d]
>>> f=[e]
>>> g=[f]
>>> a
[]
>>> b
[[]]
>>> c
[[[]]]
>>> d
[[[[]]]]
>>> e
[[[[[]]]]]
>>> f
[[[[[[]]]]]]
>>> g
[[[[[[[]]]]]]]
>>> a+a
[]
>>> a+b
[[]]
>>> b+b
[[], []]
>>> a=[,]
SyntaxError: invalid syntax
>>> a=['',]
>>> a
['']
>>> b
[[]]
>>> a+b
['', []]
>>> a
['']
>>> z=a+b
>>> z
['', []]
>>> y= z+c
>>> y
['', [], [[]]]
>>> d
[[[[]]]]
>>> e
[[[[[]]]]]
>>> a+a
['', '']
>>> a
['']
>>> a+a
['', '']
>>> a+a+a
['', '', '']
>>> c
[[[]]]
>>> a+b
['', []]
>>> a
['']
>>> b
[[]]
>>> c
[[[]]]
>>> a+b
['', []]
>>> a+a+a
['', '', '']
>>> d
[[[[]]]]
>>> c+b+a
[[[]], [], '']
>>> a+a+a+a
['', '', '', '']
>>> b+a+a
[[], '', '']
>>> a+b+a
['', [], '']
>>> a+a+b
['', '', []]
>>> c+a
[[[]], '']
>>> a+c
['', [[]]]
>>> e
[[[[[]]]]]
>>> a+a+a+a+a
['', '', '', '', '']
>>> b+a+a+a
[[], '', '', '']
>>> a+b+a+a
['', [], '', '']
>>> a+a+b+a
['', '', [], '']
>>> a+a+a+b
['', '', '', []]
>>> c+a+a
[[[]], '', '']
>>> a+c+a
['', [[]], '']
>>> a+a+c
['', '', [[]]]
>>> c+b
[[[]], []]
>>> b+c
[[], [[]]]
>>> d+a
[[[[]]], '']
>>> a+d
['', [[[]]]]
>>> 