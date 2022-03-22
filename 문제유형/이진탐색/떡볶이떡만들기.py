n, m =list(map(int, input().split(' ')))

array =list(map(int, input().split()))

start = 0
end = max(array)

# 결과값
result = 0

while(start<=end):
    # 떡볶이 길이 값 합
    total = 0
    mid = (start+end)//2
    for x in array:
        if x>mid:
            total += x - mid

   # 길이가 짧다면 왼쪽 탐색
    if total < m :
        end = mid - 1

    else:
        result=mid # 최대한 덜 잘랏을때가 정답
        start=mid+1

print(result)

