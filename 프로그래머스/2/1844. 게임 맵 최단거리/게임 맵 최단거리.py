# from collections import deque
# def solution(maps):
#     answer = -1 
    
#     # 길이
#     r_len = len(maps)
#     c_len = len(maps[0])
    
#     # BFS 를 통해서 최단 거리 찾기 
#     # 최단거리 : BFS
#     q = deque()
#     q.append([0, 0, 1])

#     # 갈수 있는 위치 
#     dr = [1, 0, -1, 0]
#     dc = [0, 1, 0, -1]
    
#     # 방문했는지 확인
#     visited = [[0] * c_len for _ in range(r_len)]
#     visited[0][0] = 1
    
    
#     # 거리 찾기 
#     while q :

#         cur_r, cur_c, dist = q.popleft()
#         visited[cur_r][cur_c] = 1
        
#         if cur_r == r_len -1 and cur_c == c_len -1 :
#             answer = dist
#             break
        
#         for i in range(4):
#             next_r = cur_r + dr[i]
#             next_c = cur_c + dc[i]
#             if (0 <= next_r < r_len) and (0 <= next_c < c_len) and maps[next_r][next_c] == 1 :
#                 if visited[next_r][next_c] == 0:
#                     q.append([next_r, next_c, dist + 1])
#                     visited[cur_r][cur_c] = 1
                    
    
#     return answer

from collections import deque
def solution(maps):
    answer = -1
    # BFS 구현
    
    # 초기세팅
    row_len = len(maps)
    col_len = len(maps[0])
    visited = [[False] * col_len for _ in range(row_len)]
    queue = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 시작점 예약
    queue.append((0,0,1))
    visited[0][0] = True

    while queue:
        # 방문
        r, c, dist = queue.popleft()
        # 도착지점인지 확인
        if r == row_len-1 and c == col_len-1:
            answer = dist
            break

        # 예약
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < row_len and 0 <= nc < col_len and maps[nr][nc] == 1:
                if not visited[nr][nc]:
                    queue.append((nr,nc,dist+1))
                    visited[nr][nc] = True
    return answer


