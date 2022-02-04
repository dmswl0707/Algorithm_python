

from sys import stdin

INF = int(1e9)
n,m = map(int,stdin.readline().split())
graph = [[INF]* (n+1) for _ in range(n+1)]

for i in range(m):
  a,b = map(int,stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1
x, k = map(int,stdin.readline().split())

# 시작: 1, k를 거쳐 x 까지 가야함

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0

for i in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][i]+graph[i][b])

distance = graph[1][k] + graph[k][x]

if distance == INF:
  print(-1)
else:
  print(distance)