
# 시험정석 출력하기

def score(x):
    if 90<x<=100:
        print('A')
    elif 80<x<=89:
        print('B')
    elif 70<x<=79:
        print('C')
    elif 60<x<=69:
        print('D')
    else:
        print('F')

score(100)

# 윤년
a = int(input())
if (a%4==0 and a%100!=0) or a%400==0:
    print(1)
else:
    print(0)



# 사분면 고르기
x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)

# 알람 시계 난이도 ***
H, M = int(input()), int(input()) #H는 시간 M은 분을 나타낸다.
#H, M = map(int, input().split())
if M>44 :
    print(H, M-45)
elif M<45 and H>0:
    print(H-1, M+15)
elif H<0:
    print(23, M+15)
