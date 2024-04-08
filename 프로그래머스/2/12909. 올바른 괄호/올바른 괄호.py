from collections import deque

def solution(s):
    answer = True
    q = deque()
    s_dict = {")" : "("}
    for i in s[::-1]:
        if i == ")":
            q.append(i)
        elif not q:
            return False
        else:
            q.pop()

    return not q