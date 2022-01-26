'''
Q.시각
# 문제.정수 N이 입력되면 N시 59분 58초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 경우의 수를 구하는 프로그램을 만드시오
'''


# 입력으로 받는 변수설정
i = int(input())

count = 0

# 시간/분/초 순서대로 하나씩 받아서 하나의 리스트 처리
for t in range(i+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(t) + str(m) + str(s):
                count += 1

print(count)
