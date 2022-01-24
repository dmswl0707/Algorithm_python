
# Q.큰 수의 법칙 유형
# 다양한 수의 배열이 있을 때, M번 더하여 가장 큰수를 만드는 법칙

# 배열의 크기 N = 5
# 숫자가 더해지는 횟수 M = 8
# 이웃하여 더해지는 횟수 K = 3

# 여러 데이터를 받을 때에는 list나 map으로 받음.

# 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

data= list(map(int, input().split()))

data.sort() # 입력받은 수 정렬하기(오름차순 또는 내림차순)

first = data[n-1]
second = data[n-2]
'''
result = 0

while True:
    for i in range(k): # 큰수로 세번 더해주기
        if m==0:
            break
        result += first
        m -= 1

    if m ==0:
        break
    result += second
    m -= 1

print(result)
'''

# 반복되는 수열을 파악하자
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second
print(result)

