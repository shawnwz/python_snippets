from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n + 1):
    d[input()].append(str(i))

print(d)

for i in range(m):
    print(' '.join(d[input()]) or -1)


