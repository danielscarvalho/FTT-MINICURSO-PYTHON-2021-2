import math
import random

file = open("data2.csv","w")

for line in range(1,1001):
    file.write("{},{},{},{},{}\n".format(line,line**2,(1/line+1)*1000,random.random()*1000,math.sin(math.radians(line))))
    
file.close()