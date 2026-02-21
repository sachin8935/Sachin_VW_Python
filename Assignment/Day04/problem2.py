# Define a function union() that takes two lists and returns another list that have union both lists. If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result should be [10, 20, 30, 40, 50, 60].
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
list3=[]
list3.extend(list1)
for val in list2:
    if(val not in list1):
        list3.append(val)

for val in list3:
    print(val)
