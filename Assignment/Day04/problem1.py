# Define a function intersection() that takes two lists and returns another list that have common elements in both lists. If list1 = [10, 20, 30, 40] and list2 = [30,40, 50, 60], then result should be [30, 40].
list1= [10,20,30,40]
list2= [30,40,50,60]
list3=[]
for val in list1:
    if(val in list2):
        list3.append(val)

for val in list3:
    print(val)