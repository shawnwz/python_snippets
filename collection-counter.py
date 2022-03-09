from collections import Counter

input()

l = list(map(int, input().split()))

cnt = Counter(l)

print(cnt)

ans = 0
for i in range(int(input())):
    size , price = [int(i) for i in input().split()]
    if cnt[size] > 0:
        ans += price
        cnt.subtract({size:1}) # subtract by 1
print(ans)