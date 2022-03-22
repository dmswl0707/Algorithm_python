'''
BFS(Breadth First Search) - 넓이 우선 탐색 알고리즘 동작구조

BFS는 큐 방식을 따름 (피포 FIFO, 리로 LILO)
1. 탐색 시작 노드를 큐에 저장하고 방문 처리
2. 시작 지점에서 방문하지 않은 인접 노드가 있다면, 큐에 넣고 방문 처리
3. 방문한 인접노드 밖에 없다면, 스택에서 꺼냄. (2-3번을 반복하면 모든 노드를 순회)
'''
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현 -> deque 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    while queue:
        # 피포
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

# 그래프 정의
graph =[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보를 리스트에 저장, 초기에 False로 설정
visited = [False] * 9

bfs(graph, 1, visited)



