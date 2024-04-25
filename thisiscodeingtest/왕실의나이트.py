'''
왕실 정원은 8*8의 좌표 평면.
왕실정원의 특정한 한 칸에 나이트가 서있다.
말을 타고 있기 때문에 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없음. 
2가지의 경우로 이동 가능
1. 수평으로 두칸 이동뒤에 수직으로 한칸이동
2. 수직으로 두칸 이동 뒤에 수평으로 한칸 이동

a ~ h열, 1 ~8 행 이 존재하고 입력값이 위치로 주어질때 (ex, a1) 움직일 수 있는 경우의 수를 구하시오
'''
from datetime import datetime

location  = input()



dict_col = dict(zip(["a","b","c","d","e","f","g","h"], range(1,9)))
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1), (2,1),(1,2),(-1,2),(-2,1)]

# lo_c = a ~ h / lo_r = 1 ~8 
lo_c , lo_r = dict_col[location[0]], int(location[1])

start1 = datetime.now()


# 이동 가능한 칸 수 확인 (왼, 오, 위, 아래)
l, r, u,d = lo_c - 1, 8 - lo_c, lo_r -1, 8 - lo_r

answer = 0


# 갈수 있는지 확인해보기
# 왼, 오 먼저
if l >= 2 :
    if u >= 1:
        answer += 1
    if d >= 1:
        answer += 1

if r >= 2:
    if u >= 1:
        answer += 1
    if d >= 1:
        answer += 1

# 위 아래
if u >= 2:
    if r >= 1:
        answer += 1
    if l >= 1:
        answer += 1

if d >= 2:
    if r >= 1:
        answer += 1
    if l >= 1:
        answer +=  1

print(answer)
print(datetime.now() - start1 )


start2 = datetime.now()

result = 0
for step in steps:
    next_row = lo_c + step[0]
    next_col = lo_r + step[1]
    if next_row >=1 and next_row <= 8 and next_col >= 1 and next_col<=8:
        result += 1


print(result)
print(datetime.now() - start2 )