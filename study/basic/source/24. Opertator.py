### Operator (연산)

## Assign(할당)
# = += -= *= /=

count = 0

count += 1

print(count)



## Arithmetic(산술)
# + - * / ** // %

# ** 제곱
print(3 ** 2)

print(7 / 3)

# // 몫
print(7 // 3)

# % 나머지
print(7 % 3)





## %로 홀짝 구분하기
numbers = [1, 2, 3, 4, 5, 6, 7]
oddnumbers = []
evennumbers = []

for number in numbers:
    if number % 2 == 1:
        oddnumbers.append(number)
    else:
        evennumbers.append(number)

# 홀수
print('홀수 :', oddnumbers)
# 짝수
print('짝수 :', evennumbers)





## 문자열 연산자
# + *


str = '나찬곤' + 'X' + '파이썬'
print(str)
# 나찬곤X파이썬

print('안녕' * 5)
# 안녕안녕안녕안녕안녕





## Comparison (비교 연산자)
# == != > < >= <=
bool1 = 1 < 2
bool2 = 2 == 1

print(bool1)
print(bool2)



## Logical (논리 연산자)
# and or not

print('논리 연산자')
print(True and True)
print(True and False)

print(True or False)

print(not True)


height = 120
age = 8

print(height > 140 and age > 10)



## Membership (멤버십 연산자)
# List 안에 값이 있는지 확인하는 연산자
# in / not in


member = ['나찬곤', '이선영', '유현진']

print('멤버십 연산자')
print('나찬곤' in member)
print('이선홍' in member)

print('류현진' not in member)
