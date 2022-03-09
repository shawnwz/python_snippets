str = "ABCDEFGHIJKLMNO"

for i in zip(*[iter(str)]*4):
    print(i)



for part in zip(*[iter(str)] * 3):
    print(part)