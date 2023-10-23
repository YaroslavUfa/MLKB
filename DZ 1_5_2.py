def f(x):
    x = list(x)
    for i in range(len(x)):
        if x[i] != ' ':
            x[i] = x[i].upper()
            break
    for i in range(len(x)):
        if x[i] in '.!?' and i+1 < len(x) and x[i+1] != ' ':
            x[i+1] = x[i+1].upper()
    return ''.join(x)
a = input('введи текст')
b = f(a)
print(b)
