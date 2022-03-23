
# 특정 조건에 만족할 때, 럭키스트레이트 기술을 사용할 수 있음
# 특정 조건 -> 점수 N을 반으로 나누어 왼쪽 각 자리수의 합과 오른쪽 각 자리수의 합이 동일할

n = int(input())
# 123,402 -> 1+2+3=4+0+2

"""
어떤 특정 수를 받으면, 
m = len(data) / 2
left = data[:m]
right = data[m:]
"""

mid = int(len(str(n)) / 2)

left = list(map(int, n[:mid]))
right = list(map(int, n[mid:]))

if (sum(left) == sum(right)) :
    print("LUCKY")
else:
    print("READY")
