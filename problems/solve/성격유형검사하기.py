'''
프로그래머스 문제  : 성격 유형 검사하기 
https://school.programmers.co.kr/learn/courses/30/lessons/118666 
선택은 1 ~7 까지 가능
'''

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
return_1 = "TCMA"

# 지표 리스트 
indi = {'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0}
         


def solution(survey, choices):
    answer = ''
    for e, s in enumerate(survey):
        choice = choices[e]
        if choice == 4:
            continue
        elif choice < 4:
            indi[s[0]] += (4- choice)
        else :
            indi[s[1]] += (choice - 4)

    indi_key = list(indi.keys())
    for i in range(0,8,2):
        if indi[indi_key[i]] >= indi[indi_key[i +1 ]]:
            answer += indi_key[i]
        else:
            answer += indi_key[i + 1]

    return answer

print(solution(survey, choices))