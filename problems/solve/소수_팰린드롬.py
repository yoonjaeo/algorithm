'''
팰린드롬 : 뒤집어도 동일한 것
N보다 크거나 같고, 소수이면서, 팰린드롬인 수 중에서 가장 작은 수 출력
'''

N = int(input())

def p_func(num):
    num_list = list(str(num))
    return num_list == num_list[::-1]

prime_num = [2]

def prim_num(n):
    if n == 1:
        return False
    r_n = int(n**0.5) +1
    for i in range(2, r_n):
        if n % i == 0:
            return False
    return True

Flag = True
while Flag:

    if prim_num(N) and p_func(N):
        print(N)
        break
    N += 1
    

# 시간초과
# Flag = True
# now = 2
# while Flag:
#     while True:
#         now +=1 
#         p_len = 0
#         for i in prime_num:
#             if now % i == 0:
#                 break
#             else:
#                 p_len += 1
#         if p_len == len(prime_num):
#             break
#     prime_num.append(now)
#     if now > N and p_func(now):
#         Flag = False
#         print(prime_num[-1])
        


# # 소수인지 찾기 - 런타임 에러
# def prime_func(now):
#     global N
#     if now > N and p_func(now):
#         return 

#     # flag = True
#     while True:
#         now += 1
#         p_len = 0
#         for i in prime_num:
#             if now % i == 0:
#                 break
#             else:
#                 p_len += 1
#         if p_len == len(prime_num):
#             break
        
        
#     prime_num.append(now)
#     prime_func(now)  

# prime_func(2)
# print(prime_num[-1])