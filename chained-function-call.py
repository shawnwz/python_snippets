def add(a,b):
  return a+b

def sub(a,b):
  return a-b

a,b=9,6

print((sub if a>b else add)(a,b))

