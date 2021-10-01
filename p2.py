def calc(val):
    if (val % 2 == 0):
        val = val**2
    else:
        val = 1/val*1000
    
    return val

print(calc(22), type(calc(22)))
#print(calc("x"))