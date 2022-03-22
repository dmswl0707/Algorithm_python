
#Q.위에서 아래로
# 수열을 내림차순으로 정렬하는 문제를 푸시오.

n = int(input())

array=[]

for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")