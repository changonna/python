## random
import random

## random.choice()
students = ['나찬곤', '이선영', '유현진']

student = random.choice(students)
print(student)
# '이선영'


## random.sample()
## 여러개의 값을 중복없이 한 번에 뽑을 수 있다.
student = random.sample(students, 2)
print(student)
# ['나찬곤', '유현진']


## random.randint()
## 범위 숫자 중에서 하나를 골라준다
'''
random.randint(startInt, endInt)
'''

student = random.randint(8, 10)
print(student)
# 10
