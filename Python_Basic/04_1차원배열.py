

# 최대, 최소 난이도 **
a = int(input())
b = list(map(int, input().split()))

print('{} {}'.format(min(a),max(b)))

#최댓값
num_list=[] #리스트에 자연수 넣어주기
for i in range(0, 9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)+1)) #n번쨰 수 출력 시에 항상 +1

#숫자의 갯수
a, b, c =map(int, input().split())
result = list(str(a*b*c))
for i in range(1,10):
    print(result.count(str(i)))  #리스트 안에 요소 갯수를 세는 법

# 나머지 난이도 **
num_list=[]
for i in range(10):
    n = int(input())
    num_list.append(n%42)
num_list=set(num_list) #집합 자료형으로 만들어준다 (중복을 제거한다.)
print(len(num_list))

# 평균
n = int(input(()))
a = list(map(int, input().split()))
M = max(a)

new = []
for score in a:
    new.append(score/M*100)

test_avg = sum(new)/n

#OX퀴즈 난이도 ***

n = int(input())
ox_list = list(input())

for i in range(n):
    score = 0
    sum_score = 0 # 합계의 초깃값
    for ox in ox_list:
        if ox == '0':
            score += 1 # 0이라면 점수가 하나 커진다.
            sum_score += score
        else:
            score = 0
    print(sum_score)

# 평균은 넘겠지 난이도 ****
case = int(input())

for i in range(case):
    score = list(map(int, input.split()))
    student = case[0]
    score = case[1:]
    avg = sum(score) / student

    count = 0

    for sc in score:
        if sc > avg:
            count+=1
    rate = count / student * 100
    print('rate : {.3f%}'.format(rate))







