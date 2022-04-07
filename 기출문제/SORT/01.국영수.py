
"""
도현이네 반 학생 N명, 국영수 성적
1. 국어 점수가 감소하는 순서
2. 국어 점수가 같으면, 영어 점수가 증가하는 순서
3. 국어와 영어점수가 같으면, 수학 점수가 감소하는 순서로
4. 모든 점수(국영수)가 같으면, 이름이 사전 순으로 증가하는 순서로
"""

N = int(input())

# 여러 타입의 인풋데이터를 받을 때
information = []
for i in range(N):
    input_data = input().split()
    information.append(input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3]))

# 여러 조건이 있는 정렬은 sorted와 lambda를 이용한다.
information = sorted(information, key = lambda x: (-x[1],x[2], -x[3], x[0]))

for name in information:
    print(information[0])

