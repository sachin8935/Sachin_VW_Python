def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

print(overlapping([1, 2, 3], [3, 4, 5]))
print(overlapping([1, 2], [4, 5]))
