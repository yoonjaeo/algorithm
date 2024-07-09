def solution(prices):
    answer = []
    prices_delta = []
    
    answer = [0]*len(prices)
    
    for idx, price in enumerate(prices):
        # print(prices_delta)

        if len(prices_delta) != 0 and prices_delta[-1][1] > price:
            for price_d in prices_delta[::-1]:
                last_idx, last_price = price_d
                if last_price > price :
                    answer[last_idx] = idx - last_idx
                    prices_delta.pop()
        prices_delta.append((idx,price))
                    
    
    for idx in range(len(prices[:-1])):
        if answer[idx] == 0:
            answer[idx] = len(prices) - (idx + 1)
            
            
    
    
#     for i, price in enumerate(prices[:-1]):
#         j = i + 1
#         for next_p in prices[i+1:]:
#             if price > next_p:
#                 answer.append(j-i)
#                 break
#             if j == len(prices)-1:
#                 answer.append(j-i)
#             j += 1
#     answer.append(0)
            
        
    return answer