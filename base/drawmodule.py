
m drawille import Canvas
from math import sin, radians

c = Canvas()

dict={3:1,2:2,1:3}

for x in range(1,100):
        dict[x] = x

for key,value in dict.items():
        c.set(key,value) 
print(c.frame())

