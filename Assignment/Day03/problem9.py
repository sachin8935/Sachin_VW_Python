
def combination(list1,list2):
    result=[]
    for i in list1:
        for j in list2:
            result.append(i+j)
    return result
list1= ["Hello", "take"]
list2 = ["Dear", "Sir"]
x =combination(list1,list2)
for i in x:
    print(i)