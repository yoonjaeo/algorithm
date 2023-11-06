'''
name = 인물이름 리스트
yearning = 그리움 점수
photo = 사진들의 속 사람들 리스트 (2차원배열) 
    만약 인물의 점수가 없다면 0
answer = 각 사진 당 추억점수
'''

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

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))