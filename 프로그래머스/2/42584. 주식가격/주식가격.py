from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    price_q = deque()
    
    for e, price in enumerate(prices):
        if len(price_q) == 0 :
            price_q.append((e, price))
        elif price_q[-1][1] > price:
            while price_q and price_q[-1][1] > price :
                q_e, q_price = price_q.pop()
                answer[q_e] = e - q_e
        price_q.append((e, price))

        
    for e, price in price_q:
        answer[e] = len(prices) - e -1
                
    return answer