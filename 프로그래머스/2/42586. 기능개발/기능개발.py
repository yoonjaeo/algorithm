# progresses : 작업의 진도가 적힌 정수배열
# speeds : 작업의 개발 속도 
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    q = deque(progresses)
    s_q = deque(speeds)
    
    left_pr = 100 - q.popleft()
    sp_q = s_q.popleft()
    
    front_day = left_pr//sp_q + int(left_pr%sp_q != 0)
    answer_num =1
    
    while q:
        left_pr = 100 - q.popleft()
        sp_q = s_q.popleft()
        day = left_pr//sp_q + int(left_pr%sp_q != 0)
        
        if front_day >= day :
            answer_num += 1
        else:
            answer.append(answer_num)
            answer_num = 1
            front_day = day
    
    answer.append(answer_num)
    
    return answer