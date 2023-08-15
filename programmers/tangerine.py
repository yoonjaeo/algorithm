import collections

def solution(k, tangerine):
    answer = 0
    tangerine_str = [str(k) for k in tangerine]
    tanger_dicts = collections.Counter(tangerine_str)
    max_tanger = tanger_dicts.most_common(len(tanger_dicts.keys()))
    min_type = 0


    for _,num in max_tanger:
        if min_type >= k:
            break
        else:
            min_type += num
            answer += 1
    return answer


k = 10
tangerine = [1,2,2,3,4,4,5,7,2,5,5,5]
print(solution(k, tangerine))