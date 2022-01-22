# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

#print (('.|.'*(2*2 + 1)).center(27, '-'))
n = 9
m = 27
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

list = [0,1,2,3,4,5,6,7,8,9]
print(list[::-2])