
## 정수 N개의 합

number = list(range(1, 10001))

def num_sum(n):
    sum = n * (n+1) // 2
    print(sum)

#num_sum(10)
# 리스트를 해결하지 못함.

def solve(a):
    print(sum(a))

#solve(number)

def solve_2(a):
    total = 0
    for x in a:
        total += x
    print(total)

#solve_2(number)


## 셀프 넘버 ****

def d(n):
    x = 0
    a = list(str(n))
    for i in a:
        x = x + int(i)

    #print(x)
    return n+x

rmv = set()

for j in range(1, 10000):
    rmv.add(d(j))

ans = set(range(1, 10000)) - rmv
for num in sorted(ans):
    print(num)

## 한수 *****

def hansu(n):
    x = 0
    for i in range(1, n+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            x += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            x += 1
    return x

num = int(input())
print(hansu(num))
