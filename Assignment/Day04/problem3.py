# Define a function subtract() that takes two lists and returns difference (i.e. excess elements from list1). If list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], then result should be [10, 20].
list1 = [10,20,30,40]
list2 = [30,40,50,60]
list3=[]
for val in list1:
    if(val not in list2):
        list3.append(val)
for val in list3:
    print(val)
