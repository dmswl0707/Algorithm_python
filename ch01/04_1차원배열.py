

# 최대, 최소
a = int(input())
b = list(map(int, input().split()))

print('{} {}'.format(min(a),max(b)))

#최댓값
num_list=[] #리스트에 자연수 넢어주기
for i range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)+1)) #n번쨰 수 출력 시에 항상 +1

