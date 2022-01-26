'''
Q.게임 개발
난이도 ***

세로(행) N x 가로(열) M로 된 직사각형 3<=N,M<=50
맵의 각 칸은 (A, B)
A : 북쪽으로부터 떨어진 갯수
B : 서쪽으로부터 떨어진 갯수

게임 움직임 순서
1.왼쪽 방향부터 차례대로 갈 곳을 정한다.
- 왼쪽 진행 할 수 있다면 : 왼쪽으로 회전 후, 전진
- 왼쪽 진행 할 수 없다면 : 왼쪽으로 회전 후, 다시 1단계로
2. 네 방향 갈 곳 선정
- 네 방향 모두 가본 적있거나, 바다이면 : 바라보는 방향으로 뒤로 1칸 전진 후, 다시 1단계로
- 뒤쪽 방향이 바다인 경우 : 움직임을 멈춘다.

방향 d
0: 북쪽, 1:동쪽, 2:남쪽, 3:서쪽
'''

# 변수를 뭘 쓸건지 정의하는 작업이 우선
n, m = map(int, input().split())

# 방문한 위치를 기록하기 위해 맵을 초기화
d = [[0]*m for _ in range(n)]

# 캐릭터의 위치 받기
x, y, direction = map(int, input().split())

# 현재 좌표 처리
d[x][y] = 1 # *** 현재 위치에 대한 정의가 필요하겠죠?

# 맵 정보를 입력으로 받아 array로 저장 *** 맵정보를 array로 할당하고, 저장해주는 것도 필요함
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의 *** 방향을 정해줘야함
# 북(음), 동(양), 남(양), 서(음)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    # 센스있게 전역 변수를 할당 ^^
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 게임 시작
count = 1
turn_time = 0

while True:
    # 처음 왼쪽으로 회전하여 이동
    turn_left() # 자주 사용하는 기능 함수 처리^^
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가본 적이 없다면
    # d[nx][ny]  array[nx][ny]가 다른 점??이 뭘까
    # d[nx][ny]가 현재 위치, array[nx][ny]이 움직인 기록
    if d[nx][ny] == 0 and array[nx][ny]==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 가본 적이 있거나, 바다라면!
    else :
        turn_time+=1

    # 네 방향 모두 갈수 없다면
    if turn_time==4:
        # 굳이 빼는 이유가 무엇일까?
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 후진
        if array[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break

        # turn_time을 다시 0으로 초기화하는 이유?
        turn_time = 0


print(count)




