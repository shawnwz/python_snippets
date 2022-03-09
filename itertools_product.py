from itertools import product

print (*product([1,2], [3,4]))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a)
print(b)

print(*product(a, b))