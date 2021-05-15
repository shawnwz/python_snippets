list1 = ['karl','lary','keera']
list2 = [28934,28935,28936]

dict0 = dict(zip(list1, list2))

dict1 = {key:value for key,value in zip(list1, list2)}

print(dict0, dict1, sep="\n")