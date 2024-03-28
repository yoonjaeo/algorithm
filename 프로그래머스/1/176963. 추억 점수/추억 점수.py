def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))

    for p in photo:
        result = 0
        for n in p:
            if n in dic:
                result += dic[n]
        answer.append(result)
            
    return answer