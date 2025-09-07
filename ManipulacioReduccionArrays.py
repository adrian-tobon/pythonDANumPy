import numpy as np

#copia de arrays a otras variables
z = np.array([2,3,4])
x = z

z[1] = 9
x[0] = 14
print("x:",x)
print("z:",z)

y = z.copy()
y[1] = 32
print("y:",y)

#cambiar la forma de una array

a = np.arange(1,10)
print(a)

b = a.reshape(3,3)
print(b)

#crea un copia aplanada del arreglo
c = b.flatten()
print(c)

#se iguala con el arreglo objetivo (apunta al mismo espacio de memoria del arreglo objetivo)
d = b.ravel()
print(d)

d[0] = 99
print(b)
print(d)

e = b.transpose()
print(e)

#funciones de agregacion sobre filas y columnas especificas
print(np.mean(b,axis=0))


#vectorizar funciones

def is_even(num):
    return num % 2 == 0

vect_is_even = np.vectorize(is_even)

numbers = np.array([1,2,3,4,5,6])

results = vect_is_even(numbers)
print(results)


