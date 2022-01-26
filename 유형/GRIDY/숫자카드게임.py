
# Q.숫자 카드 게임 유형
# 가장 작은 행 중에서 가장 큰 수 찾는 유형

# n은 행의갯수, m은 열의갯수

n, m = map(int, input().split())
print(n)

result = 0

for i in range(n):
    data = list(map(int ,input().split())) # 한줄씩 받아서 확인하겠다
    #print(data)

    # 행 중에 가장 작은 수를 찾는다
    min_value = min(data)
    # 가장 작은 수 중에 큰 수 를 찾을거얌
    result = max(result, min_value)

print(result)
