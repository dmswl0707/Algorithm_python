# Q.음료수 얼려먹기 문제유형
'''
특정 지점의 상하좌우 살펴본 후 => 상하좌우의 경우에서, 재귀호출을 이용
주변 지점에서 '0'인 지점이 있다면 해당 지점을 방문한다. => dfs 또는 bfs를 사용(그래프 관점으로 접근)
'''
## 입력받기
n, m = map(int, input().split())

## 2차원 리스트 맵 정보를 담은 리스트를 선언(조건사항 구현)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

## dfs 설계
## 상하좌우로 재귀호출을 사용하여 적용
def dfs(x, y):
    if x<=-1 or x>=n or y<= -1 or y>= m:
        return False
    ### 현재 노드를 방문하지 않았다면
    if graph[x][y]==0:
        ### 방문 처리
        graph[x][y]=1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    return False

##  방문처리 할때마다, 실행
## result는 하나씩 올려서 갯수세기

result = 0
for i in range(n): # 행 
    for j in range(m): # 열
        ### 행과 열 돌면서, 상하좌우로 방문처리
        if dfs(i, j) == True:
            result += 1

print(result)


