def union_team(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return


def find_parent(parent, a):
    if a != parent[a]:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def is_cycle(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return True
    else:
        return False


N, M = map(int, stdin.readline().split())
parent = [0] * (N + 1)
queue = []
result = 0

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    A, B, C = map(int, stdin.readline().split())
    queue.append((C, A, B))

last = 0
queue.sort()
for item in queue:
    C, A, B = item
    if is_cycle(parent, A, B):
        continue
    else:
        union_team(parent, A, B)
        result += C
        if last < C:
            last = C

print(result - last)