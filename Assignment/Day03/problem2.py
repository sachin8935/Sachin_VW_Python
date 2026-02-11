lst = list(map(int, input("Enter list elements separated by space: ").split()))

print("Alternate elements:")
for i in range(0, len(lst), 2):
    print(lst[i], end=" ")
