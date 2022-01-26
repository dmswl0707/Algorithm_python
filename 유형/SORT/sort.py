# 정렬(sort) : 데이터를 순서대로 나열하는 방식
# 선택/삽입/퀵/계수 정렬 순
'''
-선택 정렬
전체에서 가장 작은 수를 왼쪽으로 정렬한 뒤,
나머지 수 중 가장 작은 수를 선택하여 왼쪽으로 다시 정렬한다

array = [5,7,2,6,1,8,9]
for i in range(len(array)):
    min_index = i
    # for 문을 써서 나머지 범위를 줄여줌
    for j in range(i+1, len(array)):
        if array[min_index]> array[j]:
            min_index=j

    array[i], array[min_index]=array[min_index], array[i]

print(array)

시간 복잡도 O(N^2)
'''
'''
-삽입 정렬
전체에서 가장 왼쪽 두번째 수를 비교하여 작은 수를 왼쪽에 정렬
비교할 수를 한칸씩 늘려가면서 가장 작은 수를 왼쪽에 정렬한다.

array = [5,7,2,6,1,8,9]
for i in range(len(array)):
    for j in range(1, 0, -1):
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
            
print(array)

데이터가 정렬된 상태라면, 시간복잡도 O(N)
기본적으로, 시간복잡도 O(N^2)
'''
'''
- 퀵 정렬
리스트의 첫번째 데이터를 피벗으로 설정
피벗 데이터를 제외한 나머지 데이터 중에서 피벗 데이터보다 작으면 왼쪽으로, 피벗 데이터보다 크면 오른쪽으로 자리를 스위치한다.
중앙에 있는 데이터까지 순회한 다음 더이상 스위치할 것이 없으면 피벗 데이터를 중앙으로 옮긴다.
그 다음 리스트 첫번째 데이터가 되는 데이터를 피벗으로 삼아 반복 정렬한다

퀵 정렬의 시간 복잡도 O(NlogN)
데이터가 정렬된 상태인 최악인 경우, O(N^2)

array = [5, 7, 2, 6, 1, 8, 9]

def quick_sort(array, start, end):
    if start>=end: #원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    # 기본적으로 start가 작고, end가 클 때
    if left<=right:
        # 피벗보다 큰 데이터 찾을 때까지 반복
        while left<=right and array[left]<=array[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을 때까지 반봇
        while right>start and array[right]>=array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
#print(array)

# 간단한 버전
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
'''
'''
- 계수 정렬(Count sort)
각 데이터가 등장하는 숫자를 인덱스로 저장
인덱스 크기 만큼 각 숫자를 작은 값부터 출력

1. 특정 조건이 부합할 때만 사용 (모든 데이터가 정수일 때, 같은 수가 빈번하게 일어날 때)
2. 매우 빠른 정렬 알고리즘
3. 데이터 갯수가 N, 데이터 중 최댓값이 K -> 시간복잡도 O(N+K), 공간복잡도 O(N+K)
4. 비교를 통한 정렬 알고리즘이 X

array = [5, 7, 2, 6, 1, 8, 9]

# 리스트 초기화 선언
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(array)):
    for j in range(count[i]):
        print(i, end= " ")

'''
'''
### 파이썬의 정렬 라이브러리
sorted(), sort()

def setting(data):
    return data[1]
    
result = sorted(array, key=setting)
print(result)
'''