'''
문제 
N 개 물건
각 물건의 무게 : W
각 물건의 가치 : V (해당 물건을 가지고 가면 V만큼 즐길 수 있음 )
최대 가방의 무게 : K 

최대 가치는? ㅇ
'''

'''
풀이

1. 들고갈 수 있는 조합 모두 만들기 
1-1. 무게가 k보다 높다면 버리기 
1-2. 순서대로 정렬해서 조합 만들기 (DAT 방식 활용해보기) 
2. 그 중 가치합의 최대값 찾기(max)
'''

N , K = map(int, input().split())

thing = [[0,0]] # [물건 무게, 가치] 로 이루어진 list
d = [[0] * (K +1) for _ in range(N + 1)]


for i in range(N):
    thing.append(list(map(int, input().split())))

for i in range(1, N+ 1):
    for j in range(1, K + 1):
        w = thing[i][0] # i 번째 물건의 무게
        v = thing[i][1] # i 번째 물건의 가치
        
        if j < w:
            d[i][j] = d[i-1][j]
            print(d)
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)

print(thing)