import numpy as np

#make a list of random numbers
list_1 = [50, 60, 80, 100, 200, 300, 500, 600]

#make that list into a numpy array
my_numpy_array = np.array(list_1)

#check that it is a numpy array
print(f'{type(my_numpy_array)} \n\n')

#make a new numpy array as a multi-dimensional array
my_matrix = np.array([ [2, 5, 8], [7, 3, 6]])
print(f'Here is a multidimensional array: \n\n {my_matrix}\n\n')

#challenge 1, create 2x4 numpy array from 3 7 9 3 and 4 3 2 2 
challenge_1 = np.array([ [3, 7, 9, 3], [4, 3, 2, 2]])
print(f'Here is challenge 1\'s array: \n\n {challenge_1} \n\n')
