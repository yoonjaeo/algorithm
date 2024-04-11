def solution(number):
    answer = 0
    for i_1 in range(len(number[:-2])):
        for i_2 in range(i_1+1, len(number)) :
            num_zero = -1*(number[i_1] + number[i_2])
            if num_zero in number[i_2+1:]:
                answer += number[i_2+1:].count(num_zero)
    
    return answer