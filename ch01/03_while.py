# A+B - 5

while True:
    a, b =map(int, input().split())
    if a==0 and b==0:
        break
    print(a+b)

# A+B - 4

while True:
  try: #for문의 if(갯수가 정해지지 않았기 떄문에 그냥 try)
    a, b =map(int, input().split())
    print(a+b)
  except: #for문의 else (에러가 발생한 경우)
    break

# 더하기 사이클 **** (다시 풀어보기)
tmp = n = int(input())
count = 0
while True:
    ten = tmp // 10
    one = tmp % 10
    res = ten + one
    count += 1
    tmp = int(str(tmp%10)) + str(res%10)
    n = int(str(n%10) + str(res % 0))
    if (tmp==n):
        break

print(count)


