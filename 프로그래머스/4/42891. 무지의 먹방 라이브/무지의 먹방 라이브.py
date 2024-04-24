def solution(food_times, k):
    
    
    food_dict = dict(zip(range(1,len(food_times) + 1), food_times))
    quot, re = divmod(k, len(food_dict))
    
    while quot != 0 :
        zero_list = []
        for key in food_dict:
            food_dict[key] -= quot
            if food_dict[key] <= 0:
                re -= food_dict[key]
                zero_list.append(key)
        if zero_list:
            for zero in zero_list:
                del food_dict[zero]
        # print(food_dict)
        if len(food_dict) == 0:
            return -1
        quot, re = divmod(re, len(food_dict))
        # if len(food_dict) == 1 :
        #     break
    # print(food_dict)
    # print(re)

    # if len(food_dict) == 0:
    #     return -1
    # else:
    return list(food_dict.keys())[re]
    
    
    
#     food_dict = dict(zip(range(1,len(food_times) + 1), food_times))
#     # print(food_dict)
    
#     #몫, 나머지 구하기
#     quot, re = divmod(k, len(food_dict))
#     while quot != 0:
#         # print(food_dict)
#         min_num = min(food_dict.values()) #가장 작은값 구하기

#         if min_num <= quot:
#             zero_key = 0
#             len_dict = len(food_dict)
#             for key in food_dict:
#                 food_dict[key] -= min_num
#                 if food_dict[key] == 0:
#                     zero_key = key    
#             del food_dict[zero_key]
#             quot -= min_num
#         else:
#             for key in food_dict:
#                 food_dict[key] -= quot
                
#         if len(food_dict) == 0:
#             return -1
#         quot, re = divmod(re + quot*len_dict , len(food_dict))
    
#     # print(food_dict)
#     # print(list(food_dict.keys()))
#     if quot == 0:
#         return list(food_dict.keys())[re]
    
    
        
    
    
#     answer = 0
#     food_len = len(food_times) # 음식의 길이
    
#     # 몫, 나머지
#     quot, re = divmod(k, food_len)
    
#     # 음식 시간의 최소값
#     min_food = min(food_times)
    
#     if min_food <= quot:
#         re += (quot - min_food ) *food_len 
#         quot = min_food
        
#     for e, food in enumerate(food_times):
#         food_times[e] -= 1*quot
        
    
#     food_num = 0
#     # 나머지로 돌리기 
#     while re != 0:
#         if food_times[food_num] != 0:
#             food_times[food_num] -= 1
#             re -= 1
#         food_num += 1
#         if food_num == food_len:
#             food_num = 0
#         if sum(food_times) == 0:
#             return -1
#         elif len(food_times) == 1:
#             return food_num +1
    
#     while food_times[food_num] == 0 or sum(food_times) == 0:
#         food_num += 1
#         if food_num == food_len:
#             food_num = 0
        
        

#     if sum(food_times) == 0:
#         return -1
            
#     return food_num + 1