def solution(park, routes):
    answer = []
    # N : [0,-1], S : [0,+1], W :[-1,0], E [1, 0]
    route_dict = {"N" : [-1,0], "S" : [1,0], "W" :[0,-1], "E" :[0,1]}
    # start, 장애물 지점 확인하기
    block = []
    for e1,p in enumerate(park):
        for e2, p2 in enumerate(p):
            if p2 == "S":
                answer = [e1, e2]
            if p2 == "X":
                block.append([e1, e2])
                
    # park 길이 확인하기
    x_len, y_len = len(park[0]) -1 , len(park)-1
    print(block)
    for route in routes:
        flage = True
        op, n = route.split()
        n = int(n)
        # 하나씩 가보기
        go = answer.copy()
        for i in range(n):
            go[0] += route_dict[op][0]
            go[1] += route_dict[op][1] 
            if go[0] > y_len or go[0] < 0 or go[1] > x_len or go[1] <0 :
                flage = False
                break
            if go in block:
                flage = False
                break
        if flage :
            answer = go
        
        
            
        
    return answer