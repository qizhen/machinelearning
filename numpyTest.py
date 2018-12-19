# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:44:47 2018

@author: Administrator
"""
#######exp1

'''
arange reshape
'''
import numpy as np
a = np.arange(15).reshape(3, 5)
a.shape
a.dtype.name   
a.itemsize
a.size
type(a)

###exp2
'''
Array Creation
arange
linspace
random
''' 
a = np.array([2,3,4])

np.zeros( (3,4) )
 
np.ones( (2,3,4), dtype=np.int16 )

np.empty( (2,3) ) 

np.arange( 10, 30, 5 )

np.linspace( 0, 2, 9 ) 

np.random.random((2,3))

def f(x,y):
     return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)


###exp3

'''
index
'''

a = np.arange(10)**3

a[:6:2] = -1000

a[ : :-1] 

b= np.random.random((2,3))

for row in b:
    print(row)
    
for element in b.flat:
    print(element)
    
'''
Indexing with Arrays of Indices
'''
a = np.arange(12)**2

i = np.array( [ 1,1,3,8,5 ] )
a[i]

j = np.array( [ [ 3, 4], [ 9, 7 ] ] )
a[j] 

palette = np.array( [ [0,0,0],                # black
                       [255,0,0],              # red
                       [0,255,0],              # green
                       [0,0,255],              # blue
                       [255,255,255] ] )       # white
    

image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
                     [ 0, 3, 4, 0 ]  ] )
    
palette[image]


a = np.arange(12).reshape(3,4)
 
i = np.array( [ [0,1],                        # indices for the first dim of a
                [1,2] ] )

j = np.array( [ [2,1],                        # indices for the second dim
                [3,3] ] )
    
a[i,j]

a = np.arange(12).reshape(3,4)

b = a > 4

a[b]


import numpy as np
import matplotlib.pyplot as plt
def mandelbrot( h,w, maxit=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime
plt.imshow(mandelbrot(400,400))
plt.show()
########exp4
'''
shape Manipulation
'''

a = np.floor(10*np.random.random((3,4)))

a.ravel()  # returns the array, flattened

a.reshape(6,2)  # returns the array with a modified shape

a.T

a.resize((2,6)) # 改变a的形状

 a.reshape(3,-1) #s -1 in a reshaping operation, the other dimensions are automatically calculated:
 
'''
Stacking together different arrays
连接列表
vstack 竖直拼接
hstack 水平拼接
r_
c_
'''

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))

np.vstack((a,b))
 
np.hstack((a,b))

np.r_[1:4,0,4]

##########exp5

'''
Copies and Views
'''

'''
No Copy 
'''
a = np.arange(12)

b = a
b is a
true

'''
View or Shallow Copy
'''

c = a.view()
c is a
false

c.shape = 2,6   # a's shape doesn't change

c[0,4] = 1234                      # a's data changes

#Slicing an array returns a view of it:

s = a[ : , 1:3]
s[:] = 10           # a's data changes
 

'''
Deep Copy
'''

d = a.copy() 

d is a
false

d[0,0] = 9999   #a's data no changes 