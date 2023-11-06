'''
N : 외치는 정수의 개수 (1<= N <= 100,000)
다음 N줄에 걸쳐서 외치는 정수가 차례대로 주어짐
불러진 정수중의 중간에 있는 수 출력
만약 갯수가 짝수개라면 중간에 있는 두개중 작은수 출력
'''

N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
    num_len = len(num_list)
    num_list.sort()
    if num_len == 1:
        print(num)
    elif num_len%2 == 0:
        print(num_list[int((num_len/2) -1)])
    elif num_len%2 == 1:
        print(num_list[int(num_len/2)])

# print(4/2)
        
