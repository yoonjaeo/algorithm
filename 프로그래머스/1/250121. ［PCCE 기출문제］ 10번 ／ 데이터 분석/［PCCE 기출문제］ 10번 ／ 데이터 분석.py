def solution(data, ext, val_ext, sort_by):
    #data : code, date, maximum, remain
    # val_ext : 조건 
    sort_by_dict = dict(zip(["code", "date", "maximum", "remain"],range(4)))
    answer = [x for x in data if x[sort_by_dict[ext]] <= val_ext]
    answer = sorted(answer, key = lambda x : x[sort_by_dict[sort_by]])
    
    return answer