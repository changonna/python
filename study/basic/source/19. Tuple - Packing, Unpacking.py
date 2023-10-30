Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Tuple
# (immutable) 불변
# val1, val2, ...

my_tuple = ()

my_tuple
()


t
type(my_tuple)
<class 'tuple'>


my_tuple = (1, 2, 3)
my_tuple
(1, 2, 3)
my_tuple = 1, 2, 3, 4

my_tuple
(1, 2, 3, 4)
type(my_tuple)
<class 'tuple'>

>>> 
>>> 
>>> 
>>> # Packing, Unpacking
>>> 
>>> my_tuple
(1, 2, 3, 4)
>>> my_tuple = 1, 2, 3
>>> my_tuple
(1, 2, 3)
>>> 
>>> 
>>> # 1, 2, 3을 tuple로 묶어서 저장한다
>>> my_tuple = 1, 2, 3
>>> # Packing
>>> 
>>> 
>>> # num1, num2, num3에 my_tuple을 Unpacking해서 넣는다.
>>> num1, num2, num3 = my_tuple
>>> num1
1
>>> num2
2
>>> num3
3
>>> 
>>> 
>>> 
>>> num1 = 1
>>> num2 = 2
>>> 
#
>>> # num1 = 2, num2 = 1로 변경하기
>>> num1, num2 = num2, num1
>>> num1
2
>>> num2
1
>>> # 오른쪽 행의 (num2, num1)이 packing되어서 왼쪽 행의 num1, num2로 unpacking된다.
