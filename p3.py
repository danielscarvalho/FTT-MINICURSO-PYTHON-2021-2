def calc(val):
    """Faz um cálculo maluco!!"""
    try:
        if (val == 0):
            return -1
        elif (val % 2 == 0):
            val = val**2
        else:
            val = 1/val*1000
    except:
        return (val + "?? Tá me zuando maluco!!!")

    return val

print(calc(21.1), type(calc(21.1)))
print(calc(22), type(calc(22)))
print(calc(0), type(calc(0)))
print(calc("x"))
print(calc)
print(help(calc))
