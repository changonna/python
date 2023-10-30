Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# List indexing
fruits = ['apple', 'banana', 'watermelon', 'melon']

fruits[1]
'banana'

fruits[4]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fruits[4]
IndexError: list index out of range



# del
# 삭제
fruits
['apple', 'banana', 'watermelon', 'melon']
del fruits[3]
fruits
['apple', 'banana', 'watermelon']



# List slicing
fruits[0:1]
['apple']

fruits[1:2]
['banana']

fruits[0:2]
['apple', 'banana']
>>> 
>>> fruits[1:]
['banana', 'watermelon']
>>> 
>>> fruits[:1]
['apple']
>>> 
>>> 
>>> 
>>> fruits
['apple', 'banana', 'watermelon']
>>> fruits.append('coconut')
>>> fruits
['apple', 'banana', 'watermelon', 'coconut']
>>> 
>>> # list.sort() 정렬
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'coconut', 'watermelon']
>>> 
>>> 
>>> # list.count() 숫자 세기
>>> fruits.count()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    fruits.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> fruits.count('apple')
1
>>> 
>>> 
>>> len(animals)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    len(animals)
NameError: name 'animals' is not defined
>>> len(fruits)
4
