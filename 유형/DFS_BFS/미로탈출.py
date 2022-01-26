'''
Q. 미로 탈출
개인 난이도 ***
'''
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [False] * 9

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로를 벗어난 곳 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny]==1:
                continue

            # 노드 값이 1일때, 수를 하나씩 늘려가 거리정보를 반영한다.
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

bfs(graph, 1, visited)
