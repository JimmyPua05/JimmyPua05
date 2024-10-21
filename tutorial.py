import numpy as np

np1=np.zeros((2,10))
print (np1)

np2=np.full((2,10),6)
print(np2)

np3=np.arange(0,30,2)
print (np3)
print(np3[1:4]) # between index 1 to 4
print (np3[1:5:2]) #between index 1 to 4 steps 2

np4=np.random.random((5,5))
print (np4)
print (np4[1,2])
print (np4[0:3,1:3])

#squareroot
#np.sqrt(np1)

#np.absolute(np1) absolute value
#np.exp(np1) exponent

#np.sign(np1) sign positive or negative

#view and copy

#reshape np3=np1 .reshape(3,4)

np5=np.array([[1,2,3,4],[5,6,7,8]])
for x in np5:
    for z in x:
        print(z)

for x in np.nditer(np5):
    print(x)
        
np6=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np6)

#np.sort sort yoyoyo
'''
filtered=np5>2
print(np5)
print(filtered)
print(np5[filtered])

'''
