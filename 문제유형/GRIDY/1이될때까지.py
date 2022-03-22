
'''
Q. 1이 될때까지
#난이도 **
N이 1일 될때까지 다음 수행을 반복

1.N에서 1을 뺀다.
2.N을 k로 나눈다.

N와 k가 주어질 때, N이 1이 되기까지 수행해야하는 최소 횟수를 구하세요.

N과 K의 관계를 생각할 것
1) N>=K일 경우
2) N<k일 경우
'''


N = int(input())
K = int(input())
result = 0 # 우리가 구해야하는 최소 횟수

while N>=K:
    # 나누어서 0으로 떨어지지 않는다면
    while N % K != 0:
        N-=1
        result +=1
    # 나누어서 0으로 떨어진다면
    N//=K
    result +=1

#나머지 숫자 처리
while N>1:
    N-=1
    result+=1

print(result)

