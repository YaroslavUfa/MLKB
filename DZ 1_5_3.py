a = input("Введите первую строку")
b = input("Введите вторую строку")
a = a.replace(" ", "").lower()
b = b.replace(" ", "").lower()
c = set(a)
d = set(b)
if (c == d):
    print("Строки являются анаграммами")
else:
    print("Строки не являются анаграммами")
