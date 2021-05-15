a,b = 5,7

# Method 1
b,a = a,b
print(a, b)
# Method 2
def swap(a,b):
  return b,a
swap(a,b)

print(a, b)