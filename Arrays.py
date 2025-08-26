import numpy as np

#arreglo
L = [1,2,3]
A = np.array(L)

print(L)
print(A)

#matriz
A2 = np.array([[1,2],[3,4]])

print(A2)

#arreglos de ceros y unos
zeros_array = np.zeros((2,3))
ones_array = np.ones((3,2))
y= np.zeros(5)

print(zeros_array)
print(ones_array)
print(y)

#array de rangos
range_array = np.arange(10)
print(range_array)

#array espaciados linealmente
linspace_array = np.linspace(0,1,num=8)
print(linspace_array)

#matriz identidad
identity_matrix= np.eye(4)
print(identity_matrix)

#array con tipos de datos especificos

integer_array = np.array([1,2,3],dtype="int32")
float_array = np.array([1,2,3],dtype="float32")
print(integer_array)
print(float_array)