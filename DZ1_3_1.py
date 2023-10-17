def f(x):
    a = 0
    b = str(x)
    for i in b:
        a += int(i)
    return a
x = int(input("Введите число"))
t = f(x)
print(f"Сумма цифр числа {x} равна {t}")
