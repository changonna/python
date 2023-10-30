## Dictionary
# {key1: val1, key2: val2 ...}


my_dict = {}



print(type(my_dict))
      
my_dict[0] = 'a'

my_dict['b'] = 2

my_dict['학생1'] = '나찬곤'

print(my_dict)

# 삭제
del my_dict[0]
del my_dict['b']

print(my_dict)



## Dictionary method

my_dict = {'학생1': '나찬곤', '학생2': '이선영', '학생3': '유현진'}

# 
for std in my_dict:
    print(std)

# dict.keys()
# key 값만
for std in my_dict.keys():
    print(std)

# dict.values()
# value 값만
for std in my_dict.values():
    print(std)
 
# dict.items()
# key와 value 둘 다
for key, val in my_dict.items():
    print('key: {}, val: {}'.format(key, val))
