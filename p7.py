lst1 = [10, "Vai Corinthians!!!", 30, [1, 2], 234.33, 40, 4.3]
str1 = "Engenharia na FTT!!!"
tupla1 = (12,44,4.5,"Oi")

print(lst1[0],len(lst1),type(lst1[0]))
print(lst1[-1],type(lst1[-1]))
print(lst1, type(lst1))

for i in lst1:
    print(i, type(i))

print(str1[0],len(str1), type(str1[0]))
print(str1[-1], type(str1[-1]))
print(str1, type(str1))

for i in str1:
    print(i, type(i))

for i in str1:
    print(i.upper())

for i in tupla1:
    print(i, type(i))

for i in tupla1:
    if type(i) == str:
        print(0)
    else:
        print(i, type(i))
