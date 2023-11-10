
def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split("."))
    # 개인정보 유효기간 dict
    term_dict = {}
    for t in terms:
        term_dict[t.split()[0]] = t.split()[1]
        
    # 약관 종류별 현재날짜로 파기 될 최대 날짜 
    del_dict = {}
    for t in terms:
        k , p = t.split()[0],int(t.split()[1]) 
        
        # 달을 연수랑 달로 변경해주기 
        y, m = p//12 , p%12
        
        # 파기될 날짜 정해주기 y -> m-> d순서 
        # year
        del_y = year - y
        # month
        if month - m > 0:
            del_m = month - m 
        else:
            del_y -= 1
            del_m = 12 - (m- month)
            
        del_dict[k] = [del_y, del_m, day]        
    
    # 각 폐기될 날짜 보다 가입한 날짜가 더 전이면 이거나 같으면 폐기 
    
    for e, pri in enumerate(privacies):
        p , k = pri.split()[0], pri.split()[1] # p : 기간, k : 약관종류
        y,m, d = map(int, p.split("."))
        d_y, d_m, d_d = del_dict[k]
        
        if y > d_y :
            continue
        elif y < d_y:
            answer.append(e+1)
            continue
        else:
            if m > d_m:
                continue
            elif m < d_m:
                answer.append(e+1)
                continue
            else:
                if d <= d_d:
                    answer.append(e+1)
          
        
    print(del_dict)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))