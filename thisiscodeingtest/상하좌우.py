'''
문제]
여행가 A는 N × N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 × 1 크기의 정사각형으로 나누어져 있습니다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있습니다. 각 문자의 의미는 다음과 같습니다
L: 왼쪽으로 한 칸 이동
R: 오른쪽으로 한 칸 이동
U: 위로 한 칸 이동
D: 아래로 한 칸 이동
이때 여행가 A가 N × N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다 다음은 N = 5인 지도와 계획서입니다.

'''

N = int(input())
move_list = input().split()

start_point = [1,1]
move_point = start_point

move_dict = {"U" : [-1,0], 
             "D" : [1, 0],
             "L" : [0,-1],
             "R" : [0,1]}

for move in move_list:

    move_point[0] += move_dict[move][0]
    move_point[1] += move_dict[move][1]

    if (move_point[0] < 1) or (move_point[0] > N) or (move_point[1]) < 0 or (move_point[1] > N):
        move_point[0] -= move_dict[move][0]
        move_point[1] -= move_dict[move][1]
        

print(move_point)