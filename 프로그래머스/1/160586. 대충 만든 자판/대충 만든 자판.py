def solution(keymap, targets):
    answer = []
    key_dict = {}
    for key in keymap:
        for e,s in enumerate(key):
            if (s in key_dict) and (key_dict[s] < e +1):
                continue
            key_dict[s] = e + 1
    
    for target in targets:
        an = 0
        for s in target:
            if s in key_dict:
                an += key_dict[s]
            else:
                an = -1 
                break
        answer.append(an)
    
    return answer

keymap, targets = ["ABACD", "BCEFD"]	,["ABCD","AABB"]
print(solution(keymap, targets))