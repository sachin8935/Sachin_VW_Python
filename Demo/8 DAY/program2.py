import numpy as np
import sys

def print_array_info(array):
  print(f"array = {array}, \ntype = {type(array)}") # <class 'numpy.ndarray'>
  print(f"no of dimentions = {array.ndim}") # 1D
  print(f"size of array = {array.size}") # 5
  print(f"data type of items inside array = {array.dtype}") # int64
  print(f"size of every item = {array.itemsize}") # 8
  print(f"size of entire array = {array.nbytes} bytes") # 40 bytes
  print(f"shape of array = {array.shape}") #(5,)
  print('-'* 80)
  
def print_ndarray_info(array):
  print(f"array = {array}, \ntype = {type(array)}") # <class 'numpy.ndarray'>
  print(f"size of array = {array.size}") # 5
  print(f"data type of items inside array = {array.dtype}") # int64
  print(f"size of every item = {array.itemsize}") # 8
  print(f"size of entire array = {array.nbytes} bytes") # 40 bytes
  print(f"shape of array = {array.shape}") #(5,)
  print('-'* 80)

def function1():
  # create an array:
  #  - collection of similar items
  # lst = [10,20,30,40,50] # 88 bytes
  array1 = np.array([10,20,30,40]) # 1D array
  print_array_info(array1) 
  
  array2 = np.array([[10,20],[30,40]]) # 2D array
  print_array_info(array2)
  
  array3 = np.array([[10,20,70],[30,40,80],[50,60,90]]) # 3D array
  print_array_info(array3)

  
# function1()

def function2():
  array1 = np.array([[10,20],[30,40]]) # 2D array
  # print(array1.transpose()) 
  
  # array with all zeros
  array2 = np.zeros(5)
  print_array_info(array2)
  
  # array with all zeros
  array3 = np.zeros(5, dtype=np.int64)
  print_array_info(array3)
  
  # array with all ones
  array4 = np.ones(5)
  print_array_info(array4)
  
  # array with all ones
  array5 = np.ones(5, dtype=np.int64)
  print_array_info(array5)
  
  # array with sequential values
  # array6 = np.arange(10)
  array6 = np.arange(5,10)  
  print_array_info(array6)
  
  # array with random values
  array7 = np.random.rand(2,4)
  print_array_info(array7)
  
   # array with random int values
  array8 = np.random.randint(10,20,5)
  print_ndarray_info(array8)
  
  
# function2()

def function3():
  array = np.array([10,20,30,40,50])
  
  # positive indexing ndarray:
  print(f"value at 0 = {array[0]}")
  print(f"value at 1 = {array[1]}")
  print(f"value at 2 = {array[2]}")
  print(f"value at 3 = {array[3]}")
  print(f"value at 4 = {array[4]}")
  print('-'* 80)
  
  # negative indexing ndarray:
  print(f"value at -1 = {array[-1]}")
  print(f"value at -1 = {array[-2]}")
  print(f"value at -3 = {array[-3]}")
  print(f"value at -4 = {array[-4]}")
  print(f"value at -5 = {array[-5]}")
  print('-'* 80)
  
# function3()

def function4():
  array = np.array([10,20,30,40,50])
  
  # print(f"values = {array[1]} {array[3]}")
  print(f"values = {array[[1, 3, 4]]}")
  print(f"values = {array[[-1, 3, -4]]}")
  
  # multi indexing boolean positions
  print(f"values = {array[[False,True,False,True,True]]}")
  
# function4()

#USP of numpy : Broadcasting functionality
def function5():
  # array with numbers
  array= np.array([1,2,3,4,5])
  
  # broadcasting:
  # - performing operation with every item of the array
  print(f"array + 10 = {array + 10}")
  print(f"array - 10 = {array - 10}")
  print(f"array * 10 = {array * 10}")
  print(f"array / 10 = {array / 10}")
  print(f"array // 10 = {array // 10}")
  print(f"array ** 2 = {array ** 2}")
  print("-"* 80)
  
  # broadcasting comparison operators:
  print(f"array == 3 = {array == 3}")
  print(f"array != 3 = {array != 3}")
  print(f"array > 3 = {array > 3}")
  print(f"array >= 3 = {array >= 3}")
  print(f"array < 3 = {array < 3}")
  print(f"array <= 3 = {array <= 3}")  
  print("-"* 80)
    
# function5()
  
def function6():
  # array with salaries
  salaries = np.array([20, 30, 50, 10, 80, 90, 100])
  print(f"salaries = {salaries}")
  
  # filtering:
  print(f"salaries > 60 = {salaries[salaries > 60]}")
  
# function6()

def function7():
  array1 = np.eye(3)
  print_ndarray_info(array1)
  
  array2 = np.eye(4) * 10
  print_ndarray_info(array2)
  
  array3 = np.zeros(shape=(4,6), dtype=np.int8)
  print_ndarray_info(array3)
  
# function7()

def function8():
  # list of numbers
  numbers = [10,20,30,40,50]
  print(f"numbers = {numbers}, type = {type(numbers)}")
  print(f" memory required for an item in numbers = {sys.getsizeof(numbers[0])} bytes")
  print(f" memory required for numbers = {sys.getsizeof(numbers[0]) * len(numbers)} bytes")
  print(f"-"* 80)
  
  # array by np
  array = np.array([10,20,30,40,50])
  print(f"numbers = {array}, type = {type(array)}")
  print(f" memory required for an item in numbers = {sys.getsizeof(array[0])} bytes")
  print(f" memory required for numbers = {sys.getsizeof(array[0]) * len(array)} bytes")
  print(f"-"* 80)
  
  # array by np
  array1 = np.array([10,20,30,40,50], dtype=np.int64)
  print(f"numbers = {array1}, type = {type(array1)}")
  print(f" memory required for an item in numbers = {sys.getsizeof(array1[0])} bytes")
  print(f" memory required for numbers = {sys.getsizeof(array1[0]) * len(array1)} bytes")
  print(f"-"* 80)
  
  # array by np
  array2 = np.array([10,20,30,40,50], dtype=np.int32)
  print(f"numbers = {array2}, type = {type(array2)}")
  print(f" memory required for an item in numbers = {sys.getsizeof(array2[0])} bytes")
  print(f" memory required for numbers = {sys.getsizeof(array2[0]) * len(array2)} bytes")
  print(f"-"* 80)
  
  # array by np
  array3 = np.array([10,20,30,40,50], dtype=np.int16)
  print(f"numbers = {array3}, type = {type(array3)}")
  print(f" memory required for an item in numbers = {sys.getsizeof(array3[0])} bytes")
  print(f" memory required for numbers = {sys.getsizeof(array3[0]) * len(array3)} bytes")
  print(f"-"* 80)
  
  # array by np
  array4 = np.array([10,20,30,40,50], dtype=np.int8)
  print(f"numbers = {array4}, type = {type(array4)}")
  print(f" memory required for an item in numbers = {sys.getsizeof(array4[0])} bytes")
  print(f" memory required for numbers = {sys.getsizeof(array4[0]) * len(array4)} bytes")
  print(f"-"* 80)
  
function8()
  