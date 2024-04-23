'''
[문제]
동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오.
예를들어,
N = 5 , 동전이 3,2,1,1, 9원 짜리가 있을대 만들수 없는 금액 중 최소값은 8원이다.
N = 3, 동전이 3,5,7 있을 때, 만들 수 없는 최소값은 1원입니다.
'''

N = int(input())
list_money = [x for x in map(int, input().split())]
list_money.sort()
target = 1

for x in list_money:
    if target < x:
        print(x, target)
        break
    target += x
print(target)