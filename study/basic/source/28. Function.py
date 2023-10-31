### Function

'''
def 함수이름(인자1, 인자2, ...):
    실행할 명령1
    실행할 명령2

    return 결과
'''

## 예제1
def add(num1, num2):
    return num1 + num2

sum = add(1, 2)
print(sum)
# 3




## return을 여러개
'''
def 함수이름(인자1, 인자2, ...):
    실행할 명령1
    실행할 명령2

    return 결과1, 결과2, ...

'''

def add_mul(num1, num2):
    return num1 + num2, num1 * num2
## --> 결과값이 tuple로 저장

my_add_mul = add_mul(1, 2)
print(my_add_mul)
# (3, 2)

print(type(my_add_mul))
# <class 'tuple'>


## packing과 unpacking을 통해 튜플을 각각 변수에 저장한다.
my_add, my_mul = add_mul(1, 2)

print(my_add)
# 3

print(my_mul)
# 2

