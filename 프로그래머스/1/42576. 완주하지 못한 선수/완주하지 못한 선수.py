import collections

def solution(participant, completion):
    answer = ''
    
    # print(collections.Counter(participant))
    # print(collections.Counter(completion))
    # print(collections.Counter(participant) - collections.Counter(completion))
    participant.sort()
    completion.sort()
    
    for i in range(len(participant) -1):
        if participant[i] != completion[i] :
            return participant[i]
    
        
            
    
    return participant[-1]

