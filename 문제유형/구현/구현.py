
# 구현 유형에서는 머리속의 알고리즘을 구현하는 과정이 중요함
# 머리 속에 어떤 그림을 그리고 코드를 구현하는 것이 필요한 작업

# 상하좌우 문제유형

# 조건 나열
n = int(input())
x, y = 1, 1
plans = input().split()

# 이동 방향 정의해주기(왼, 오, 위, 아)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x+dx[i] # 타입 인덱스와 좌표인덱스가 같은 경우로 움직임
            ny = y+dy[i]
    # 예외 처리
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 새로운 좌표 생성
    x, y = nx, ny

print(x, y)

