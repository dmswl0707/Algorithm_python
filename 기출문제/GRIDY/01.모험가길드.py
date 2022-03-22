
# 반드시 n명이 있어야 여행을 떠날수 있음
# ** 최대 몇개의 그룹을 만들수 있을지 알고자함 (한 그룹당 인원제한은 없음)
# -> 최대 공포도 수 만큼 인원을 구성해야함.
# -> 작은 인원 수부터 그룹을 형성하는게 가장 많이 만들 수 있음

n = input()
x = list(map(int,input().split()))
# 5
# 2 3 1 2 2

x.sort()
# 1 2 2 2 3

count = 0 # 한 그룹당 인원수
group = 0 # 그룹 수
for xs in x:
    count += 1
    #print(i)

    if count >= xs:
        group += 1
        count = 0 # 인원 수가 다 찾을 때, 그룹의 인원수를 초기화

print(group)

"""
오름 차순으로 접근해서, 하나씩 요소를 검사하는 방식
그룹수와 인원수를 나누어서 수를 하나씩 키움 ** 요게 핵심 포인트
인원 수가 공포도만큼 다 찾을 때, 초기화하는 것이 필요함(은근 중요)
"""
