a = input('введите числа').split()
a = list(a)
b = a[0]
for i in a:
    if i > b:
        b = i
print(b)  
