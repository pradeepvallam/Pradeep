import numpy as np

a = np.array([1,3,5,6,8,9,15,17,4,2,20,16,11,18,7])
print(a)
b = a.reshape((3,5)) #shaped to 3 rows and 5 columns
print(b)
c = b.max(axis=1) #axis=1 checks max for each row where axis=0 checks max for each colum
print(c)
d = c.reshape((3,1)) #reshaped array c t0 3x1 to compare it with b
print(d)
e = np.where(b!=d,b,0) #np.where(condition,true=value,false=value) based on these it replaces the value
print(e)


