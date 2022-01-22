# DFS (Depth First Search) - 깊이 우선 탐색 알고리즘
# 노드와 엣지로 구성, 간선이 만나는 곳을 정점(vertex)라고함
# 인접 행렬 또는 인접리스트로 연결관계를 표현
'''
인접 행렬 방식과 인접 리스트 방식 비교
- 메모리 측면 특징
1. 인접 행렬방식은 모든 관계를 저장하기 때문에 노드가 많을 수록, 메모리는 비효율적
   반면, 인접 리스트 방식은 연결된 정보만 저장하기 때문에, 메모리 사용이 더 효율적
- 정보 검색 속도 특징
2. 인접 리스트는 연결된 정보를 하나하나 확인해야하기 때문에, 특정 노드 연결 정보의 검색 속도는 느리다.
   반면, 인접 행렬방식은 모든 관계를 저장하고 특정 정보만 검색하기 때문에, 연결 정보 확인 속도가 빠르다.
'''

# 인접 행렬 표현 방식

INF = 999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

#print(graph)

# 인접 리스트 표현 방식

# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph2 = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph2[0].append((1,7))
graph2[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph2[1].append((0,7))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph2[2].append((0,5))

#print(graph2)
