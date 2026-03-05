import sys

x = 1
# print(f"Type {type(x)}, x memory : {sys.getsizeof(x)} bytes") # 28 bytes

y = 12345678911
# print(f"Type {type(y)}, Y memory : {sys.getsizeof(y)} bytes") # 32 bytes

lst2 = range(1,201) # Type <class 'range'>, lst2 memory : 48 bytes
# print(f"Type {type(lst2)}, lst2 memory : {sys.getsizeof(lst2)} bytes") #88 bytes

lst = [10, 20, 30, 40, 50]
# print(f"Type {type(lst)}, lst memory : {sys.getsizeof(lst)} bytes") #88 - 148 bytes

# print(lst * 2) # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
# print(lst + 10)
lst1 = [i+10 for i in lst]
# print(lst)
# print(lst1)

data  = [23, 1, 36, 57, 28, 17, 16, 44]

def check_even(no):
  if no % 2 == 0:
    return True # Add element to new list
  # else:
  #   return False # ignore element.
 
even_no_lst = []  
for n in data:  
  if check_even(n):
    even_no_lst.append(n)

# print(even_no_lst)
  
data1  = [23, 1, 36, 57, 28, 17, 16, 44]   

# Higher order function
# filtered_even_no_list = filter(check_even,data1)
filtered_even_no_list = filter(lambda num: num % 2 == 0,data1)
# print(filtered_even_no_list) # <filter object at 0x000001B2C0DC5BD0>
# print(list(filtered_even_no_list)) # [36, 28, 16, 44]
# print(list(filtered_even_no_list)) # []


numbers = [10,20,30,40,50]
def double_the_no(num):
  return num * 2

mapped_obj = map(double_the_no, numbers)
print(f"Type {type(mapped_obj)}, {mapped_obj}") 
# Type <class 'map'>, <map object at 0x00000141EF736410>

print(f"{list(mapped_obj)}") # [20, 40, 60, 80, 100]
print(f"{list(mapped_obj)}") # []

