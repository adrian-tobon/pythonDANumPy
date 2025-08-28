import numpy as np

#broadcasting

vector= np.array([1,2,3])

#el escalar hace el broadcast hacia el array [5,5,5]
#print(vector+5)
#print(vector+[5,5,5])

#broadcasting con matrices

a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

b = np.array([[1],[2],[3]])

#print(a)
#print(b)
#print(a*b)

'''
b quedaria asi al hacer el broadcasting

[1,2,3]
[1,2,3]
[1,2,3]

'''

#funciones universales

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))


angles = np.array([0,30,60,90])
angles_rad = np.radians(angles)

print(np.sin(angles_rad))
print(np.cos(angles_rad))
print(np.tan(angles_rad))

print(np.greater(a,b))
print(np.greater_equal(a,b))
print(np.less(a,b))
print(np.less_equal(a,b))
print(np.equal(a,b))
print(np.not_equal(a,b))

print(np.power(a,b))

print(np.mean(a))
print(np.std(a))

