def solution(friends, gifts):
    answer = 0
    gifts_dict = {}
    # dict[name] = {친구이름 : [준거, 받은거], 친구이름2 : 준거}
    
    for friend in friends:
        gifts_dict[friend] = {'ide' : 0}
        for f in friends:
            if f == friend:
                continue
            gifts_dict[friend][f] = [0,0]
            
    for gift in gifts:
        gave, back = gift.split()
        #준사람
        gifts_dict[gave][back][0] += 1
        gifts_dict[gave]['ide'] += 1
        #받은사람 
        gifts_dict[back][gave][1] += 1
        gifts_dict[back]['ide'] -= 1
    
    list_ide = [0]*len(friends)

    
    for e, friend in enumerate(friends):
        for k,v in gifts_dict[friend].items():
            if k == 'ide':
                continue
            if v[0] > v[1]:
                list_ide[e] += 1
            elif v[0] == v[1]:
                if gifts_dict[friend]["ide"] > gifts_dict[k]["ide"]:
                    list_ide[e] += 1    
                
    print(list_ide)      
    return max(list_ide)