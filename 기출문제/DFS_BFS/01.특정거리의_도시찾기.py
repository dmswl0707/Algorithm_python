from collections import deque

n, m, k, x =map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # A에서 B 까지의 거리
    A, B = map(int, input().split())
    graph[A].append(B)

# 거리 초기화
distance = [0] * (n+1)
# 방문 여부 초기화(불리언)
visited = [False]*(n+1)

queue = deque([x])
answer = []  # 최단 거리가 k인 모든 도시

def bfs(start):

    visited[start]=True
    distance[start]=0

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node]=True
                queue.append(next_node)
                # 노드 사이의 거리는 1
                distance[next_node]=distance[now]+1

                if distance[next_node]==k:
                    answer.append(next_node)

    if len(answer)==0:
            print(-1)
    else:
        answer.sort()
        for ans in answer:
            print(ans, end='\n')

# 출발 도시번호 x
bfs(x)







