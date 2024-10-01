from collections import deque
def solution(n, computers):
    answer = 0
    vi = {}
    q = deque()
    
    for r , computer in enumerate(computers):
        
        if not vi.get(r): 
            answer += 1
            q.append(r)
        
            while q:
                cur = q.popleft()

                for c, next_ in enumerate(computers[cur]):
                    if c != cur and next_ == 1 and not vi.get(c):
                        vi[c] = True
                        q.append(c)
    
    return answer