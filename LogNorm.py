import sympy
from sympy import *


h=Symbol('h', real=True)

R = int(input("Enter the number of rows and columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(R):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)


A = Matrix(matrix)
# identity matrix
I = eye(R)
# matrix in the norm
main_matrix =I+h*A
#print(main_matrix)
# logarithmic norm using 1-norm
print(limit((main_matrix.norm(1)-1)/h, h, 0, '+'))
# logarithmic norm using Frobenius norm
print(limit((main_matrix.norm()-1)/h, h, 0, '+'))
# logarithmic norm using infinity norm
print(limit((main_matrix.norm(oo)-1)/h, h, 0, '+'))
