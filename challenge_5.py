import numpy as np

#make a matrix
matrix = np.random.randint(1, 10, (5, 5))
print(f'This is a matrix:\n\n{matrix}\n\n')

new_matrix = matrix[matrix > 7]

print(f'This is only elements over 7:\n\n{new_matrix}\n\n')

odd_matrix = matrix[ matrix % 2 != 0]

print(f'Only odd numbers from our matrix:\n\n{odd_matrix}\n\n')

even_matrix = matrix[ matrix % 2 == 0]

print(f'Only eveb numbers from our matrix:\n\n{even_matrix}\n\n')

#mini challenge 5 - replace negative elements by 0, replace odd elements with -2

X = np.array([[2, 30, 20, -2, -4],
[3, 4, 40, -3, -2],
[-3, 4, -6, 90, 10],
[25, 45, 34, 22, 12],
[13, 24, 22, 32, 37]])

print(f'The array we are working on for our challenge:\n\n{X}\n\n')

rows, columns = X.shape

for line in range(rows):
	for character in range(columns):
		if X[line][character] < 0:
			X[line][character] = 0
		elif X[line][character] % 2 != 0:
			X[line][character] = -2
		else:
			pass
			
print(f'After completing the challenge:\n\n{X}\n\n')

#that was a very over-engineered solution. :( Let's try that again. 

Y  = np.array([[2, 30, 20, -2, -4],
[3, 4, 40, -3, -2],
[-3, 4, -6, 90, 10],
[25, 45, 34, 22, 12],
[13, 24, 22, 32, 37]])

print(f'The array we are working on for our challenge that I am NOT overengineering this time:\n\n{Y}\n\n')

Y[Y < 0] = 0
Y[Y % 2 != 0] = -2

print(f'Y array after simplified solution:\n\n{Y}\n\n')

			
