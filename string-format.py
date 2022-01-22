a = 1
b = 1
for i in range (1, 10):
    #print ('{0:b}'.format(i))
    print ('{0:{width}b}'.format(i, width=5))
    print ('{0:3b}'.format(i))



def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

print_formatted(17)