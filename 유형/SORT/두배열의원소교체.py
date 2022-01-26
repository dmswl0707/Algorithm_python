
# Q.두 배열의 원소 교체
'''
N 개의 원소
K번의 바꿔치기
배열은 A,B로 두개의 배열
배열 A의 합이 최대가 될 수 있게 만들어야함
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# k번 반복될 경우
for i in range(k):
    if a[i]< b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))