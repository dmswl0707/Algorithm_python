'''
다이나믹 프로그래밍 -> 동적 계획법

ex) 피보나치 수열
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))

1.큰문제를 작은 문제로 나눌수 있다 (분할정복와 유사)
2.작은 문제에서 구한 정답은 그것을 포함하는 큰문제에서도 동일하다.
-> 메모제이션(캐싱)을 이용, 중복을 제거

시간 복잡도는 O(N)
'''
# 1.탑다운 문제방식
d = [0] * 100
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

#2.보텀업 문제방식(반복문 적용)
d = [0] * 100

d[1]=1
d[2]=1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])

