'''
Q.왕실의 나이
### 개인적으로 난이도, ***
8x8 평면 좌표
행의 위치 : 1~8
열의 위치 : a_h

처음 위치는 a1.
움직일 수 있는 형태
1. 수직으로 두칸 이동 후, 수평으로 한칸 이동
2. 수평으로 두칸 이동 후, 수직으로 한칸 이동
(-2, 1), (-2, -1), (-1, 2), (-1, -2),(1, 2), (1, -2), (2, -1), (2, 1) -> (행, 열)
'''

# 현재의 위치 입력으로 받기
locate = input()
row = int(input(locate[1]))
column = int(ord(locate[0]))-int(ord('a'))+1

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 위치 이동시키기
result = 0
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]
    # 이동할 때 위치 옮기기
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)
