from collections import namedtuple

n = input()
m = " ".join(input().split())

print(m)
c = 0
N = namedtuple('N', m)
for i in range(int(n)):
    n1 = N(*map(str, input().split()))
    c += int(n1.MARKS)
    print(c)
print(n1)
print(c / int(n))


# sample input
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6