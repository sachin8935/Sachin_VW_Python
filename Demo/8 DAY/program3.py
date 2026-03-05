# NumPy : ndarray
# Pandas: 
#   - Series: one dimensional
#   - DataFrame :
#       - two dimensional
#       - similar to spreadsheet (rows x columns)
#       - created using series(columns)

import numpy as np
import pandas as pd

def function1():
  # list of numbers:
  numbers = [10, 20, 30, 40, 50]
  print(f"numbers = {numbers}, type = {type(numbers)}")
  
  # ndarray of numbers:
  array = np.array([10, 20, 30, 40, 50])
  print(f"array = {array}, type = {type(array)}")
  
  # series of numbers
  series = pd.Series([10, 20, 30, 40, 50])
  print(f"array = {series}, type = {type(series)}")
  
# function1()

def print_series_info(series):
  print(f"array = {series}, \ntype = {type(series)}") # 
  print(f"no of dimentions = {series.ndim}") # 
  print(f"size of series = {series.size}") # 5
  print(f"data type of items inside series = {series.dtypes}") # int64
  print(f"size of entire array = {series.nbytes} bytes") # 40 bytes
  print(f"shape of array = {series.shape}") #(5,)
  print('-'* 80)
  
def print_dataframe_info(series):
  print(f"array = {series}, \ntype = {type(series)}") # 
  print(f"no of dimentions = {series.ndim}") # 
  print(f"size of series = {series.size}") # 5
  print(f"data type of items inside series = {series.dtypes}") # int64
  print(f"shape of array = {series.shape}") #(5,)
  print('-'* 80)
  
def function2():
  # series of numbers
  series = pd.Series([10,20,30,40,50])
  print_series_info(series)
  
  # series of dictionary
  series_dict = pd.Series({"name":"person1", "email":"person1@test.com"})
  print(series_dict)
  print(f"indexes = {series_dict.index}, values = {series_dict.values}")
  
# function2()

def function3():
  # series of numbers
  series1 = pd.Series([10,20,30,40,50])
  print(series1)
  
  # positive indexing
  print(f"series[0] = {series1[0]}")
  print(f"series[1] = {series1[1]}")
  print(f"series[2] = {series1[2]}")
  print(f"series[3] = {series1[3]}")
  print(f"series[4] = {series1[4]}")
  
  # negative indexing : is not allowed
  # print(f"series[-1] = {series1[-1]}")
  
  series2 = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
  # print(series2) 
  
  series3 = pd.Series([10,20,30,40,50], index=[-1,4,7,-3,-9])
  print(series3)
  print(series3[-9])
  
  
# function3()

def function4():
  cars = pd.Series(["i10","triber","city","i20"], index=["hyundai","renault","honda","hyundai"])
  print(cars)
  
  # find model of honda
  print(f"cars['honda'] = {cars['honda']}")
  
  # find model(s) of hyundai
  print(f"cars['hyundai'] = {cars['hyundai']}")
  
# function4()

def function5():
  # series of numbers
  series = pd.Series([10,20,30,40,50])
  
  # Filtering
  print(f"series > 30= {series > 30}")
  print(f"series > 30= \n{series[series > 30]}")
  
# function5()

def function6():
  s1 = pd.Series({'1':'Peter','2':'Walter','3':'Olivia','4':'Astrid','5':'Jean'})
  df = pd.DataFrame(s1)
  print(df['1'])
  # print_dataframe_info(df)
  
  df1 = pd.DataFrame([10,20,30,40,50])
  # print(df1)
  # print_dataframe_info(df1)
  
# function6()

  
