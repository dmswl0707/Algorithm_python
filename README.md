# Algorithm_python
> 알고리즘 코딩 테스트 유형 정리 및 문제 풀이 😇  

## 1. Chapter 구성
*나동빈 저, 이것이 코딩 테스트다 with 파이썬*

|목차|유형|문제1|문제2|문제3|문제4|
|------|---|---|---|---|---|
|Chapter1|**그리디**|큰 수의 법칙|숫자 카드 게임|1이 될 때까지|
|Chapter2|**구현**|시각|왕실의 나이|게임 개발|
|Chapter3|**DFS,BFS**|음료수 얼려먹기 유형|미로탈출|
|Chapter4|**정렬**|위에서아래로|성적이낮은순서로학생출력하기|두배열의원소교체|
|Chapter5|**이진탐색**|부품찾기|떡볶이떡만들기|
|Chapter6|**다이나믹프로그래밍**|1로만들기|개미전사|바닥공사|효율적인화폐구성|
|Chapter7|**최단경로**|가장빠른길찾기|미래도시|전보|
|Chapter8|**그래프이론**|팀결성|도시분할계획|커리큘럼|

## 2. 유형 정리
### (1) 그리디
최소한의 아이디어로 빠르게 또는 탐욕적으로 문제를 해결하는 방식.단순 문제 해결 방식.  
> 예시) 하나몬이 아르바이트를 하러 간 사이에, 안타깝게도 하나몬의 집에 도둑이 들었다.
도둑의 가방은 35kg까지의 물건만 담을 수 있고, 하나몬의 집에는 4개의 물건이 있다.

주로, 집계 함수나 경우의 수, 반복된 수열의 구조를 파악하여 문제를 해결한다.
> #### 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 그리디의 경우 -> 집계 함수, 경우의 수, 반복된 수열의 형태 중 어떤 접근 방식이 최적일 지 방법을 선택한다.
> 3. 코드의 전체적인 구조를 설계하고 접근법을 검토한다.  
     (최적의 해를 찾는 것이 아니므로, dynamic programming이랑 헷갈리지 말자.)

### (2) 구현
전체적인 구현 능력을 평가하는 유형. 그리디에서는 문제 해결 과정을 보여준다면, 구현에서는 코드의 전체적인 구조를 **상세히** 설계하는 데에 초점.  

특별한 알고리즘 적용 없이, 문제의 요구사항에 맞게 코드를 작성하는 것이 핵심.  
++ 완전 탐색이나 시뮬레이션 유형에서 주로 요하는 문제.

> #### 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 완전 탐색의 경우 -> 주어진 데이터가 적을 때, 리스트 안의 요소를 검사하여 처리한다. (모든 경우의 수 계산을 위해, DFS/BFS나 순열/조합을 이용)  
> 3. 시뮬레이션의 경우 -> 상하좌우의 좌표 개념으로 접근.
> > - 상하좌우 각 좌표를 리스트화한 다음, 방문한 곳을 기록한다.  
> ex) steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]  
> > - 방문한 곳을 기록할 때, 리스트 컴프리헨션 방법을 이용한다.  
> ex)  d = [[0] * m for _ in range(n)]

### (3) DFS/BFS
(1) DFS : 깊이 우선 탐색 알고리즘. 최대한 멀리 있는 노드를 우선으로 탐색. 스택의 자료구조를 이용.  
(2) BFS : 너비 우선 탐색 알고리즘. 가까운 노드를 우선으로 탐색. 큐의 자료구조를 이용.  

> #### 접근 방식  
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. DFS의 경우 -> 재귀 용법 또는 스택 구조 이용. (재귀용법 대신 스택구조로만 활용하면 시간복잡도 줄일 수 있음)
>  - 탐색 시작 노드를 스택에 저장하고 방문 처리.  
>  - 시작 지점에서 방문하지 않은 인접 노드가 있다면, 스택에 넣고 방문 처리.  
>  - 방문한 인접노드 밖에 없다면, 스택에서 꺼냄. (2-3번을 반복하면 모든 노드를 순회)  
> ```python
> def dfs(graph, v, visited):
>    # 현재 노드 방문 처리
>    visited[v]=True
>    print(v, end=' ')
>    # 현재 노드와 방문한 노드를 재귀적으로 호출
>    for i in graph[v]:
>        if not visited[i]:
>            dfs(graph, i, visited)
> 
> # ++ 스택을 이용할 때는, 리스트와 append/pop을 이용한다.
> ```
> 3. BFS의 경우 -> 큐 구조 이용.
>  - 탐색 시작 노드를 큐에 저장하고 방문 처리.
>  - 시작 지점에서 방문하지 않은 인접 노드가 있다면, 큐에 넣고 방문 처리.
>  - 방문한 인접노드 밖에 없다면, 큐에서 꺼냄. (2-3번을 반복하면 모든 노드를 순회)  
> ```python
> def bfs(graph, start, visited):
>    # 큐 구현 -> deque 사용
>    queue = deque([start])
>    # 현재 노드 방문 처리
>    visited[start] = True
>    while queue:
>        # 피포
>        v = queue.popleft()
>        print(v, end=' ')
>        for i in graph[v]:
>            if not visited[i]:
>                queue.append(i)
>                visited[i]=True
> ```
### (4) 정렬
정렬 유형은 주로, 데이터가 여러 개 주어지고 정렬 알고리즘 개념을 이용하여 문제를 해결하는 유형

|순번|알고리즘|정의|복잡도|특징|
|---|---|---|---|---|
|1|선택정렬|가장 작은 데이터를 선택하여, 정렬되지 않은 데이터의 가장 앞쪽 데이터와 순서를 변경|시간 복잡도 : O(N^2), 공간 복잡도 : O(N)|아이디어가 가장 직관적|
|2|삽입정렬|데이터를 앞에서부터 하나씩 확인하며, 데이터를 적절한 위치에 삽입하는 방법|시간 복잡도 : O(N^2), 공간 복잡도 : O(N)|데이터가 정렬되어 있을 때 사용|
|3|퀵정렬|기준 데이터를 설정한 후, 기준데이터 보다 큰 데이터와 작은 데이터의 위치를 변경|시간 복잡도 : O(NlogN), 공간 복잡도 : O(N)|대부분의 경우에서, 퀵 정렬을 사용(일반화 성능이 좋음)|
|4|계수정렬|특정한 값을 가지는 데이터를 카운트하는 방법|시간 복잡도 : O(N+k), 공간 복잡도 : O(N+k)|데이터 크기가 한정되어 있을 때 사용|

#### ++ 파이썬 정렬 라이브러리(sort/sorted)  
계수정렬을 사용하는 경우(가장 빠른 연산)가 아니라면, 주로 파이썬 정렬 라이브러리를 사용 
최악의 경우에도, 시간 복잡도 O(NlogN)  
- Sort ->  리스트 자체를 변경  
- Sorted ->  정렬된 리스트 값을 반환

### (5) 이진 탐색
이진 탐색 유형은 *데이터 탐색 범위를 반으로 줄여나가면서, 데이터를 빠르게 탐색* 하는 기법  
내부의 데이터가 *정렬* 되어 있을 때, 시작점/중간점/끝점 세가지 변수를 이용하여 적용. 

> #### 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 재귀함수 또는 반복문을 이용해 데이터를 탐색한다.  
> -  재귀함수를 이용한 방식  
> ```python
> def binary_search(array, target, start, end):
>    if start>end:
>        return None
>    mid = (start+end)//2
>
>    if array[mid]==target:
>        return mid
>    elif array[mid]>target:
>        return binary_search(array, target, start, mid-1)
>    else:
>        return binary_search(array, target, mid+1, end)
> ```  
> - 반복문을 이용한 방식 
> ```python
> def binary_search(array, target, start, end):
>    while start<=end:
>        mid = (start+end) // 2
>        if array[mid] == target:
>            return mid
>        elif array[mid] > target:
>            end = mid - 1
>        else:
>            start = mid + 1
>    return None
> ```

#### ++ 파이썬 이진탐색 라이브러리(bisect)
```python
from bisect import bisect_left, bisect_right
a = [1,2,4,4,6]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))
```
### (6) 다이나믹 프로그래밍(=동적 계획법)
다이나믹 프로그래밍이란, 계산된 부분을 다시 계산하지 않도록 하여(메모제이션) 연산속도를 증가시키고,
인접한 항 사이의 관계를 점화식으로 정리하여 문제에서 요구하는 요점을 효율적으로 해결하는 유형이다.

> #### 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 1차원 리스트에 메모리를 기록하도록 선언한다.
> 3. 탑 다운 유형
> - 재귀 함수를 이용하여 큰 문제에서 작은 문제를 해결하는 방식
> ```python
> d = [0] * 100
> def fibo(x):
>    if x==1 or x==2:
>        return 1
>    if d[x]!=0:
>        return d[x]
>    d[x]=fibo(x-1)+fibo(x-2)
>    return d[x]
> ```
> 4. 보텀 업 유형
> - 단순한 반복문을 이용해 작은 문제를 해결하고, 큰 문제를 해결하는 방식
> ```python
> d = [0] * 100
> d[1]=1
> d[2]=1
> n = 99
> for i in range(3, n+1):
>     d[i] = d[i-1]+d[i-2]
> 
> print(d[n])
> ```

### (7) 최단 경로
최단 경로 유형은 그래프 상에서 가장 짦은 경로를 찾아 문제를 해결하는 유형으로,
최단 경로 이외의 최소 비용을 이용하는 다양한 문제에도 적용됨.  

크게, 다익스트라와 플로이트 워셜 알고리즘을 이용함.  

|순번|알고리즘|정의|복잡도|특징|
|---|---|---|---|---|
|1|다익스트라|방문하지 않은 노드 중, 최단 거리가 짧은 거리를 선택하여 그 노드를 거쳐가는 경우를 확인하여 최단 거리 갱신|O(ElogV)|한 지점에서 다른 모든 지점까지의 최단 경로를 계산, 우선순위 큐를 사용하여 구현, 그리디 유형에 해|
|2|플로이드워셜|다이나믹 프로그래밍을 이용하여, 방문하는 최단 거리 테이블을 갱신(점화식 이용)|O(V^3)|모든 지점에서 다른 모든 지점까지의 최단 경로를 계산|

> #### 접근 방식
> 1. 문제의 요점을 파악하여, 문제 유형을 가려낸다.
> 2. 한 지점에서 모든 최단 경로를 계산해야하는지, 모든 지점에서 모든 최단 경로를 계산해야하는지 파악한다.
> 3. 다익스트라 유형
> - 출발 노드를 선정한다.
> - 최단 거리 테이블을 초기화한다
> - 방문하지 않은 노드 중에서 최단 노드를 선택한다.
> - 해당 노드를 거쳐 다른 노드를 가는 비용을 계산한다.
> - 3/4번을 반복한다.
> ```python
> ```
> 4. 플로이드 워셜 유형형
> -
> -
> -
> -
> -
> ```python
> ``` 

### (8) 그래프 이론
그래프 이론 유형은 그래프 자료구조 내용에 기반하여, 문제를 해결하는 유형이다.
주로, 서로소 집합/신장 트리/크루스칼/위상정렬 알고리즘을 사용한다.

