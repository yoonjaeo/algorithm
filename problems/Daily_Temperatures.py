'''
실수 온도가 list로 주어지고 각 온도에서 더 높은 온도가 나오는
최소 날짜가 answer.
만약 없다면 0 return 

ex) 
input = temperatures = [73,74,75,71,69,72,76,73]
output = [1,1,4,2,1,1,0,0]
'''

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    answer_list = [0 for i in range(len(temperatures))]
    record_list = []

    for e, temp in enumerate(temperatures):
    #     if not record_list:
    #         record_list.append(e)
    #         continue
        while record_list and temp > temperatures[record_list[-1]]:
            answer_list[record_list[-1]] = e - record_list[-1]
            record_list = record_list[:-1]
        record_list.append(e)

    return answer_list

input = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(input))
'''
문제 풀이 방식
answer list를 temperatures len만큼 생성 (0으로 초기화)
온도의 index를 기록할 list 형성(record_list) (index 기록 시 temp는 바로 추출 가능)
현재 온도와 record_list 속 온도를 비교
만약 현재 온도가 크다면?
    answer[record_list 속 마지막 인덱스] = 현재 index - record_list 속 인덱스
    record_list에서 값 빼기 
    다음 record_list와 비교 => 끝날때까지 반복 => while문 사용
공통
    record_list에 현재 index 넣기
'''