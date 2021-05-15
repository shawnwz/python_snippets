maths = [59, 64, 75, 86]
physics = [78, 98, 56, 56]

list1 = [x + y for x,y in zip(maths,physics)]

import operator
list2 = list(map(operator.add, maths, physics))

import numpy as np
list3 = np.add(maths, physics)

print (list1, list2, list3, sep="\n")