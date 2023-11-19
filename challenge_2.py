import numpy as np

#random numbers
x = np.random.rand(20)
print(f'random numbers\n\n{x}\n\n')

#matrix of random numbers
a = np.random.rand(3, 3)
print(f'3x3 matrix of random numbers\n\n{a}\n\n')

#single random number between 1 & 50
b = np.random.randint(1, 50)
print(f'A random number between 1 & 50\n\n{b}\n\n')

#more than one random number, between 1 & 100 - 15 to be exact
c = np.random.randint(1, 100, 15)
print(f'15 random numbers between 1 & 100\n\n{c}\n\n')

#do what range does but with numpy
d = np.arange(1,30)
print(f'A range from 1 to 30\n\n{d}\n\n')

#make a diagnoal of ones and zeros
e = np.eye(7)
print(f'Diagonal of 1s and 0s\n\n{e}\n\n')

#make a matrix of ones
f = np.ones((7,7))
print(f'A matrix of ones\n\n{f}\n\n')

#make an array of zeros
g = np.zeros(7)
print(f'An array of zeros\n\n{g}\n\n')


'''
Challenge:
take a positive integer from the user & create a 1x10 array of random numbers
'''
y = int(input("Type a positive integer here:"))
challenge_2 = np.random.randint(1, y, 10)
print(challenge_2)
