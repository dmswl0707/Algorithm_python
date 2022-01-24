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
'''