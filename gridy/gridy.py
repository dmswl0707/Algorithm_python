

# 그리디? 탐욕적 알고리즘
# 당장 좋은 것을 먼저 선택하는 방법
# 당장 큰수를 고르는 것이 최적의 해를 장담하지는 않음


n = 1260
count = 0

# 동전의 종류
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n//coin  # 총 금액을 동전 타입으로 나눔
    n %= coin

print(count)

