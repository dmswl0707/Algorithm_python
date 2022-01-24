# Q.음료수 얼려먹기 유형
'''
특정 지점의 상하좌우 살펴본 후
주변 지점에서 '0'인 지점이 있다면 해당 지점을 방문한다.
'''
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if
