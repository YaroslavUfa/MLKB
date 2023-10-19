def f(x):
    while True:
        a = x.find('(')
        b = x.find(')')
        if a != -1 and b != -1:
            x = x[:a] + x[b+1:]
        else:
            break
    return x
a = input()
print(f(a))
