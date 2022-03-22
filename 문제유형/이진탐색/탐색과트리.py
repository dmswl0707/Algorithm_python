# 순차 탐색
# 리스트 안에 특정 데이터를 찾기 위해 앞에서부터 하나씩 차례대로 데이터를 확인하는 방법

# 데이터 갯수가 N개일 때, N번의 연산이 필요함으로 시간 복잡도는 O(N)

def sequential_search(n, target, array):
    # 각 원소를 돌면서 탐색(n은 인덱스)
    for i in range(n):
        if array[i]==target:
            return i + 1 # 인덱스는 0부터 시작함으로...

print('생성할 원소 갯수를 입력한 다음 문자열을 입력하세요')

input_data = input().split()
n = int(input_data[0])
# 원소의 갯수
target = input_data[1]
# 찾고자 하는 문자열

print('적은 원소 갯수만큼 다음 문자열을 입력하세요')
array = input().split()

print(sequential_search(n, target, array))

# 이진 탐색
# 원소의 갯수룰 절반씩 줄여가면서, 데이터를 확인하는 법
# 데이터 갯수가 N개일 때, 절반씩 줄면서 연산함으로 시간 복잡도는 O(logN)
# 탐색을 어떻게 할 것인가에 대해 설계

#1.재귀함수를 이용한 구현
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2

    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하진 않습니다')
else:
    print(result+1)

#2.반복문을 이용한 구현
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
