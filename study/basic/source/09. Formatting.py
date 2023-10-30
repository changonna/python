Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Formatting
>>> # 문자열을 더 잘 표현하기 위해서 사용
>>> 
>>> my_str = 'My name is %s' % 'Changon Na'
>>> mystr
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mystr
NameError: name 'mystr' is not defined. Did you mean: 'my_str'?
>>> my_str
'My name is Changon Na'
>>> 
>>> 
>>> 
>>> '%d %d' % (1, 2)
'1 2'
>>> '%d %f %s' % (1, 2.0, 'hi')
'1 2.000000 hi'
>>> 
>>> '%f' % 3.14
'3.140000'
