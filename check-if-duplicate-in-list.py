def has_dup(lst):
    return len(lst) != len(set(lst))

x = [1,2,2,3,4,5]
y = [1,2,3,4,5]

print(has_dup(x))

print(has_dup(y))