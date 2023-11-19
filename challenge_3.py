import numpy as np

#make two arrays of 10 numbers
a = np.arange(1,10)
print(f'A range of 9 numbers, array a \n\n{a}\n\n')

b = np.arange(1,10)
print(f'A range of 9 numbers again, array b \n\n{b}\n\n')

#add the two arrays together
sum = a + b
print(f'The sum of array a & b\n\n{sum}\n\n')

#square array a
squared = a ** 2
print(f'Array a squared\n\n{squared}\n\n')

'''
Challenge: Given X & Y values below, obtain distance between them
X = [5, 7, 20]
Y = [9, 15, 4]
'''	

# Make the points into a numpy array
X = np.array([5, 7, 20])
Y = np.array([9, 15, 4])

#  Use a numpy method to make a new array that's just the difference between consecutive points
dX = np.diff(X, append=X[0])  
dY = np.diff(Y, append=Y[0])
#append is there because i need to get distance between 3rd & first point at the end. 

#what is dX and dY? Make sure this actually works, since this method wasn't gone over in the course. 
print(f'This is dX \n\n{dX}\n\n')
print(f'This is dY \n\n{dY}\n\n')

# calculating distances, square root of (x2 - x1)^2 + (y2 - y1)^2
#since .diff already did the subtraction & placed it in dX & dY, the rest is simple
howfar = np.sqrt(dX**2 + dY**2)
print(howfar)
