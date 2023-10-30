Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # format()
>>> 
>>> # '{ }'.format()
>>> 
>>> 'My name is %s' % 'changonna'
'My name is changonna'
>>> 
>>> 'My name is {}'.format('changonna')
'My name is changonna'
>>> 
>>> 
>>> '{} x {} = {}'.format(2, 3, 2 * 3)
'2 x 3 = 6'
>>> 
>>> 
>>> # 순서 지정해서 format 사용하기
>>> '{1} x {0} = {2}'.format(2, 3, 2*3)
'3 x 2 = 6'
