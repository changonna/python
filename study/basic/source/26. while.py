## Loop

# while
"""
while 조건:
    실행할 명령1
    실행할 명령2
"""

num = 0

while num < 5:
    print('{}는 5보다 작습니다'.format(num))
    num += 1



cnt = 0
# continue, break
while cnt < 10:
    cnt += 1
    if cnt < 4:
        continue
    print('횟수:', cnt)
    if(cnt == 8):
        break
