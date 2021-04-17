
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
if (a%4== and a%100!=0) or a%400==0:
    print(1)
else:
    print(0)