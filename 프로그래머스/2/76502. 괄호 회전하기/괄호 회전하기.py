from collections import deque

def solution(s):
    answer = 0
    
    s = deque(list(s))
    s_dict = { '{' : '}', '(' : ')', '[': ']'}
    
    # 회전
    for i in range(len(s)):
        left = s.popleft()
        s.append(left)
        
        tmp = deque()
        Flag = True
        
        for j in range(len(s)):
            if s[j] in s_dict:
                tmp.append(s[j])
            elif len(tmp) == 0 or s_dict[tmp.pop()] != s[j]:
                Flag = False
                break
        
        if Flag and len(tmp) == 0:
            answer += 1
                
            
    return answer