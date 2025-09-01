import numpy as np


#multiplicacion de vectores
A = np.array([[1,2],[3,4]])
B = np.array([[2,0],[1,2]])

print(A)
print(B)

print(np.dot(A,B))
print(A @ B)

#producto punto
x = np.array([2,3])
y = np.array([5,2])

print(np.dot(x,y))
print(x @ y)

#determinante
print(np.linalg.det(A))
print(np.linalg.det(B))

#inversa de una matriz
M = np.array([[3,3],[3,3]])
det_A = np.linalg.det(A)

if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("Inversa de A:\n", inv_A)
else:
    print("A no es invertible")
    
#descomposicion de matrices

#QR
print(A)

Q,R = np.linalg.qr(A)
print("Factor Q:\n",Q)
print("Factor R:\n",Q) 

print(Q @ R)   
    
#eigendecomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Original Matrix A:\n", A)
print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors (columns correspond to eigenvalues):\n", eigenvectors)


#solucion a un sistema de ecuaciones lineales

A = np.array([[3,1],[1,2]])
b = np.array([9,8])
print("A:\n",A)
print("b:\n",b)

z = np.linalg.solve(A,b)
print("z:\n",z)
print(np.dot(A,x))

#solucion con pseudoinversa
B = np.array([[1,2],[3,4],[5,6]])
c = np.array([1,2,3])

print("B:\n",A)
print("c:\n",c)

d = np.linalg.pinv(B)
print("d:\n",d)

x = np.dot(d,c)
print("x:\n",x)

#autovalores y autovectores

C = np.array([[3, 1],[1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(C)
print("Autovalores:", eigenvalues)
print("Autovectores:\n", eigenvectors)




    