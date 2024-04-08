from collections import deque

def solution(arr):
    answer = []
    queue = deque(arr)

    while queue:
        tmp = queue.popleft()
        if len(answer) == 0 or answer[-1] != tmp:
            answer.append(tmp)
    
    return answer