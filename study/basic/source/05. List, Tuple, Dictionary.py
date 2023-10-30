Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# List
my_list = [1, 2, 3]
my_list
[1, 2, 3]
students = ['가가가', '나나나', '다다다']
students
['가가가', '나나나', '다다다']
for std in students:
    print(std)

가가가
나나나
다다다
']
SyntaxError: incomplete input



import random
print(random.choice(students))
다다다
print(random.choice(students))
가가가
students.append('라라라')
students
['가가가', '나나나', '다다다', '라라라']




# Tuple
# 값을 바꿀 수 없다
students[0]
'가가가'
>>> students[0] = '마마마'
>>> students[0]
'마마마'
>>> 
>>> 
>>> 
>>> my_tuple = ('가', '나', '다')
>>> my_tuple
('가', '나', '다')
>>> my_tuple[0]
'가'
>>> my_tuple[0] = '마'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    my_tuple[0] = '마'
TypeError: 'tuple' object does not support item assignment
>>> ## tuple에서는 값을 변경할 수 없다
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # Dictionary
p
>>> my_dict = {'가': '남', '나': '여', '다': '남'}
>>> my_dict[가]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    my_dict[가]
NameError: name '가' is not defined
>>> my_dict
{'가': '남', '나': '여', '다': '남'}
>>> my_dict['가']
'남'
>>> my_dict['나']
'여'
>>> my_dict['나'] = '남'
>>> my_dict['나']
'남'
