def square(x):
    return x ** 2

#this not return the value, it return the iterator instead
print(map(square, [1,2,3,4,5]))

print(list(map(square, [1,2,3,4,5])))

print(list(map(lambda x : x ** 2, [1,2,3,4,5,6])))