# Numpy --> compare Data Location and type

import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array([1,2,3,4,5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])

print("#"*50)

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

print("#"*50)
my_list_of_data=[1,2,"A","B",True,10.50]
my_array_of_data=np.array([1,2,"A","B",True,10.50])

print(my_list_of_data) #[1, 2, 'A', 'B', True, 10.5]
print(my_array_of_data) #['1' '2' 'A' 'B' 'True' '10.5']

print("#"*50)
print(type(my_list_of_data[0])) #int
print(type(my_array_of_data[0])) #string

my_array_of_data_two=np.array([1,2])
print(type(my_array_of_data_two[1])) #int32

my_array_of_data_three=np.array([1,2,10.5])
print(type(my_array_of_data_three[1])) #float64

