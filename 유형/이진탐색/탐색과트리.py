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

