import numpy as np

#make a numpy array
my_numpy_array = np.array([3, 5, 6, 2, 8, 10, 20, 50])
print(f'{my_numpy_array}\n\n')

#access specific indexes from the array
print(f'Access first element from the array \n\n{my_numpy_array[0]}\n\n')

#access last element from the array
print(f'Access last element from the array with -1 \n\n{my_numpy_array[-1]}\n\n')

#Get everything up to but not including the last element
print(f'Access everything besides last element: \n\n{my_numpy_array[0:-1]}\n\n')
'''The second variable in [0:-1] grabs the range from the first variable to 
one element before the second variable. -1 is the last variable, which is
why this works'''

