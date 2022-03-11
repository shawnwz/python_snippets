from itertools import permutations


s, k = map(str, input().split())

l = list(s)
l.sort()
s = "".join(l)

p = list(permutations(s, int(k)))

for i in p:
    print("".join(i))


#a better one
# s,n = input().split()
# print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')