import numpy as np
my_list=[1,2,3,4,5,6]
my_array=np.array(my_list)

print(my_list) #[1,2,3,4,5,6]
print(my_array) #[1 2 3 4 5 6]

#Type
print("#"*50)
print(type(my_list)) # class 'list'
print(type(my_array)) # class 'nympy.ndarray'

#Accessing Elements 
print("#"*50)
print(my_list[0]) #1
print(my_array[0]) #1

print("#"*50)
a=np.array(10)
b=np.array([10,20])
c=np.array([[1,2],[3,4]])
d=np.array([[[5,6],[7,9]],[[1,3],[4,8]]])

print(d[1][1][1]) # 8
print(d[1,1,1]) # 8
print(d[1,1,-1]) # 8

print("#"*50)

print(a.ndim) # 0
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3

print("#"*50)
# Custom Dimenstions
my_custom_array=np.array([1,2,3],ndmin=3)
print(my_custom_array[0][0][0]) # 1