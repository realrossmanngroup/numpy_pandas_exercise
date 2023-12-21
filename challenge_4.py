import numpy as np

#make a numpy array
my_numpy_array = np.array([3, 5, 6, 2, 8, 10, 20, 50])
print(f'{my_numpy_array}\n\n')

#access specific indexes from the array
print(f'Access third element from the array \n\n{my_numpy_array[2]}\n\n')

#access last element from the array
print(f'Access last element from the array with -1 \n\n{my_numpy_array[-1]}\n\n')

#get everything from 0 through 3 in the array(the fourth item)
print(f'Access from the first element in the array to the third\n\n{my_numpy_array[0:3]}\n\n')

#Get everything up to but not including the last element
print(f'Access everything besides last element: \n\n{my_numpy_array[0:-1]}\n\n')
'''The second variable in [0:-1] grabs the range from the first variable to 
one element before the second variable. -1 is the last variable, which is
why this works'''

#defining a two dimensional numpy array

#practice what np.random.randint does
matrix = np.random.randint(1, 10, (4, 4))
print(f'This is a matrix I made: \n\n {matrix}\n\n')
print(matrix)
print(f'This is an individual element in a matrix, row 1, character 3:\n\n {matrix[0][2]}')

#mini challenge

X = np.array([[2, 30, 20, -2, -4],
[3, 4, 40, -3, -2],
[-3, 4, -6, 90, 10],
[25, 45, 34, 22, 12],
[13, 24, 22, 32, 37]])
	
print(f'This is the array for the mini challenge: \n\n{X}\n\n')

X[-1] = 0

print(f'This is the array after completing the mini challenge: \n\n{X}\n\n')

