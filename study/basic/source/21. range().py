Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# range()

range(3)
range(0, 3)

type(range(3))
<class 'range'>
>>> # range 라는 type
>>> 
>>> [0, 1, 2]
[0, 1, 2]
>>> 
>>> for n in [0, 1, 2]:
...     print(n)
... 
...     
0
1
2
>>> 
>>> 
>>> for n in range(0, 3):
...     print(n)
... 
...     
0
1
2
>>> 
>>> 
>>> 
>>> range(3)
range(0, 3)
>>> 
>>> range(3:5)
SyntaxError: invalid syntax
>>> range(3, 5)
range(3, 5)
>>> 
>>> for n in range(3, 5):
...     print(n)
... 
...     
3
4
